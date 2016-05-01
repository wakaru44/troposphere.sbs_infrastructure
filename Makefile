# A simple makefile to make things simpler

help:
	@echo "Troposphere code to generate a personal workstation in the cloud";
	@echo "";
	@echo "generate     - generate the cloud formation stack";
	@echo "create       - make the call to the AWS cli to spin up the instance";
	@echo "bump         - Bump the version of the stack";
	@echo "";

generate:
	python personal_stack.py > personal_stack.json

create:
	bash tool_createstack.sh

bump:
	bash tool_bump_version.sh
