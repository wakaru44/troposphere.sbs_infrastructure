# A simple makefile to make things simpler

help:
	@echo "Troposphere code to generate a personal workstation in the cloud";
	@echo "";
	@echo "generate     - generate the cloud formation stack";
	@echo "create       - make the call to the AWS cli to spin up the instance";
	@echo "";

generate:
	python personal_stack.py

create:
	bash tool_createstack.sh
