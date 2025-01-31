import aws_cdk as core
import aws_cdk.assertions as assertions

from inventory_api.inventory_api_stack import InventoryApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in inventory_api/inventory_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InventoryApiStack(app, "inventory-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
