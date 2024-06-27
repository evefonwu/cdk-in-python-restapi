import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    """Function to reserve inventory with product_id and quantity, if there is available stock."""
    try:
        # Parse the input for product_id and quantity values
        body = json.loads(event["body"])
        product_id = body.get("product_id")
        quantity_to_reserve = body.get("quantity")

        if not product_id or not quantity_to_reserve:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing product_id or quantity"}),
            }

        # Get the current inventory for the product
        response = table.get_item(Key={"product_id": product_id})

        if "Item" not in response:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Product not found"}),
            }

        item = response["Item"]
        current_quantity = item["quantity"]

        # Check if there is enough stock
        if current_quantity < quantity_to_reserve:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Insufficient stock"}),
            }

        # Update the inventory
        new_quantity = current_quantity - quantity_to_reserve
        table.update_item(
            Key={"product_id": product_id},
            UpdateExpression="SET quantity = :new_quantity",
            ExpressionAttributeValues={":new_quantity": new_quantity},
        )

        return {"statusCode": 200, "body": json.dumps({"success": True})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
