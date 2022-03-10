from aws_lambda.lambda_helper import LambdaHelper

lambda_helper = LambdaHelper(deployed)

if previousDeployed.bucketName != deployed.bucketName or previousDeployed.s3Key != deployed.s3Key or previousDeployed.s3ObjectVersion != deployed.s3ObjectVersion:
    print "Updating lambda function code..."
    update_res = lambda_helper.update_function_code_s3()
    if update_res['ResponseMetadata']['HTTPStatusCode'] == 201:
        deployed.functionARN = update_res['FunctionArn']

if deployed.lambdaWait:
    time.sleep(int(deployed.lambdaWait))

update_res = lambda_helper.update_function_configurations()

if update_res['ResponseMetadata']['HTTPStatusCode'] == 201:
    deployed.functionARN = update_res['FunctionArn']

if previousDeployed.lambdaTags != deployed.lambdaTags:
    tags_update = lambda_helper.add_tags_to_function()

print "Lambda function with function ARN %s is updated." % deployed.functionARN
