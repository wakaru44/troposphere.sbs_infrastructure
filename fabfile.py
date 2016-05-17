#!/usr/bin/python
# -*- utf-8 -*-

from fabric.api import local,task


def do(command):
    """
    fabric is still uncomfortable
    """
    output=local(command,capture=True)
    return output


def current_version():
    with open("version.md") as fh:
        return fh.readline()


def show_table(content):
    """
    try to paint a table with labels
    """
    #print "{:<8} {:<15} {:<10}".format('Key','Label','Number') #Headers
    for k, v in content.iteritems():
        num = v
        print "{:<8} {:<15}".format(k, num)


@task
def describe():
    """
    show the minimum details required for an stack
    """
    query="""  'Reservations[*].Instances[*].[InstanceId,PublicDnsName,KeyName]' """
    filters = """ "Name=tag-value,Values=personal$(cat version.md )" """
    output = do("""aws  ec2 describe-instances  --query {query}  --output json --filters {filters} """.format(query=query,filters=filters))
    import json
    details=json.loads(output)
    key = details[0][0][2]
    dns = details[0][0][1]
    print("ssh -i ~/.ssh/{0} ubuntu@{1}".format(key,dns))


@task
def long_describe():
    """
    show the interesting details for all the instances
    """
    query="""  'Reservations[*].Instances[*].[InstanceId,Tags,PublicDnsName,KeyName]' """
    filters = ""
    output = do("""aws  ec2 describe-instances  --query {query}  --output json --filters {filters} """.format(query=query,filters=filters))
    import json
    details=json.loads(output)
    print details
    datad= {"key":  details[0][0][2],
            "Public DNS":  details[0][0][3],
            "Tags": details[0][0][1]
            }
    show_table(datad)

 
