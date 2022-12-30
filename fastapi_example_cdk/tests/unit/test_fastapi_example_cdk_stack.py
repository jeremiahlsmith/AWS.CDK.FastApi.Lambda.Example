import aws_cdk as core
import aws_cdk.assertions as assertions

from fastapi_example_cdk.fastapi_example_cdk_stack import FastapiExampleCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in fastapi_example_cdk/fastapi_example_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FastapiExampleCdkStack(app, "fastapi_example_cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
