
# Import troposphere
from troposphere import Template, Ref, Output, Join, GetAtt, Parameter, Base64
import troposphere.ec2 as ec2
from troposphere.route53 import RecordSetType

# Create a template for resources to live in
template = Template()

keypair = template.add_parameter(Parameter(
    "KeyPair",
    Type="String",
    Description="The name of the keypair to use for SSH access",
))

# Create a security group
sg = ec2.SecurityGroup('PersonalSecurityGroup')
sg.GroupDescription = "Allow access to the Personal project instances from anywhere"
sg.SecurityGroupIngress = [
    ec2.SecurityGroupRule(
        IpProtocol="tcp",
        FromPort="22",
        ToPort="22",
        CidrIp="0.0.0.0/0",
    )]

# Add security group to template
template.add_resource(sg)

# Create an instance
instance = ec2.Instance("PersonalInstance")
instance.ImageId = "ami-5a60c229" # oficial aws ubuntu 14.04 ami for ireland eu-west
instance.InstanceType = "m1.small"
instance.SecurityGroups = [Ref(sg)]
instance.KeyName = Ref(keypair)
instance.UserData = Base64("""
#!/bin/bash
curl http://juanantonio.fm/HIBOY
echo "this should be a script or sumzin"
""")

# Add instance to template
template.add_resource(instance)

# Add the machine to a nicer dns name
hostedzone = template.add_parameter(Parameter(
    "HostedZone",
    Description="The DNS name of an existing Amazon Route 53 hosted zone",
    Type="String",
))


personalDNSRecord = template.add_resource(RecordSetType(
    "personalDNSRecord",
    HostedZoneName=Join("", [Ref(hostedzone), "."]),
    Comment="DNS name for the personal instance.",
    Name=Join("", [Ref(instance), ".", Ref("AWS::Region"), ".",
              Ref(hostedzone), "."]),
    Type="A",
    TTL="900",
    ResourceRecords=[GetAtt("PersonalInstance", "PublicIp")],
))


# Add output to template
template.add_output(Output(
    "InstanceAccess",
    Description="Command to use to SSH to instance",
    Value=Join("", ["ssh -i ", Ref(keypair), " ubuntu@", GetAtt(instance, "PublicDnsName")])
))

# Add DNS to the output too
template.add_output(Output("DomainName", Value=Ref(personalDNSRecord)))


# Print out CloudFormation template in JSON
print template.to_json()
