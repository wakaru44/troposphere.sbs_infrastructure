# A simple makefile to make things simpler

help:
	@echo "Troposphere code to generate a personal workstation in the cloud";
	@echo "";
	@echo "generate       - generate the cloud formation stack from py to json";
	@echo "bump           - Bump the version of the stack, as it will be identified in AWS";
	@echo "create         - make the call to the AWS cli to spin up the instance";
	@echo "spinup         - Do everything. From the generation to the creation";
	@echo "describe       - describe AWS instances in a nice way";
	@echo "long-describe  - describe AWS instances in a LONG way";
	@echo "";

generate:
	python personal_stack.py > personal_stack.json

create:
	bash tool_createstack.sh

bump:
	bash tool_bump_version.sh

spinup: bump generate create
	
long-describe:
	 aws  ec2 describe-instances  --query 'Reservations[*].Instances[*].[InstanceId,Tags,PublicDnsName,KeyName]'

describe:
	#aws  ec2 describe-instances  --query 'Reservations[*].Instances[*].[InstanceId,Tags,PublicDnsName,KeyName]'  --output text | grep -B 1 stack-name
	aws  ec2 describe-instances  --query 'Reservations[*].Instances[*].[InstanceId,PublicDnsName,KeyName]'  --output json --filters "Name=tag-value,Values=personal$(shell cat version.md )" | grep -v "\]\|\["


