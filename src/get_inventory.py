import json
import boto3
import os

from decimal import Decimal


def convert_decimal_to_python(obj):
    """
    DynamoDB returns numeric values as Decimal objects.
    Converts Decimal to int if the value is an integer, otherwise to float.
    """
    if isinstance(obj, list):
        return [convert_decimal_to_python(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    else:
        return obj


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    """Function to get an inventory item"""
    try:
        # Parse the input for product_id
        path_parameters = event.get("pathParameters", {})
        product_id = path_parameters.get("product_id")

        if product_id is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing product_id"}),
            }

        # Get the item from DynamoDB
        response = table.get_item(Key={"product_id": product_id})

        if "Item" not in response:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Product not found"}),
            }

        item = response["Item"]
        product_details = convert_decimal_to_python(item)
        return {"statusCode": 200, "body": json.dumps(product_details)}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
