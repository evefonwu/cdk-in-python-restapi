import json
import boto3

"""Inventory Demo Seed Data"""

dynamodb = boto3.resource("dynamodb")

"""
TODO - after infra deployed: 
update TABLE_NAME with CDK generated table name
"""
TABLE_NAME = "<pending-table-name>"

table = dynamodb.Table(TABLE_NAME)

INVENTORY_DATA = [
    {
        "product_id": "tshirt001",
        "location": "Warehouse A",
        "quantity": 100,
        "description": "T-shirt A",
    },
    {
        "product_id": "tshirt002",
        "location": "Warehouse A",
        "quantity": 100,
        "description": "T-shirt B",
    },
    {
        "product_id": "tshirt003",
        "location": "Warehouse A",
        "quantity": 100,
        "description": "T-shirt C",
    },
]


def lambda_handler(event, context):
    """Populate initial DynamoDB table for inventory stock"""
    for item in INVENTORY_DATA:
        table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps("Initial database populated successfully."),
    }
