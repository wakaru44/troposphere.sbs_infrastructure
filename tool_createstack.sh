#!/bin/bash

echo "create a stack"
echo "Any parameter passed after calling the script will be appended to the aws cloudformation command"
NAME=personal005
TMPL=template003.json
CFNPARAMS=create-stack-parameters.json

# full version with manual params
#aws cloudformation create-stack  --stack-name $NAME --template-body file://$TMPL  --parameters='{"ParameterKey":"KeyPair","ParameterValue":"jenkinsWakaru"}'  --tags='{"Key":"Environment","Value":"dev"}' | tee -a stack_id.log

# swetter version with file based parameters
aws cloudformation create-stack  --stack-name $NAME --template-body file://$TMPL  --cli-input-json file://$CFNPARAMS ${@:2} | tee -a stack_id.log

