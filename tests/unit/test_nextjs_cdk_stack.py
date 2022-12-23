import aws_cdk as core
import aws_cdk.assertions as assertions

from infra.nextjs_cdk_stack import NextjsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in nextjs_cdk/nextjs_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NextjsCdkStack(app, "nextjs-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
