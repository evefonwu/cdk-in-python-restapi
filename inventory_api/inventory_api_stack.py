import os

"""Import CDK Construct Libraries"""
from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
)
from constructs import Construct


class InventoryApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        current_dir = os.path.dirname(__file__)
        src = os.path.join(current_dir, "../src")

        """DynamoDB table with a partition key product_id of type string"""
        ddb_table = ddb.TableV2(
            self,
            "DynamoDBTable",
            partition_key=ddb.Attribute(
                name="product_id", type=ddb.AttributeType.STRING
            ),
        )

        """Lambda functions to process the API requests"""

        get_inventory_fn = _lambda.Function(
            self,
            "GetInventoryFn",
            code=_lambda.Code.from_asset(src),
            handler="get_inventory.lambda_handler",  # filename.functionname
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={"TABLE_NAME": ddb_table.table_name},
        )
        ddb_table.grant_read_data(get_inventory_fn)

        reserve_inventory_fn = _lambda.Function(
            self,
            "ReserveInventoryFn",
            code=_lambda.Code.from_asset(src),
            handler="reserve_inventory.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={"TABLE_NAME": ddb_table.table_name},
        )
        ddb_table.grant_read_data(reserve_inventory_fn)
        ddb_table.grant_write_data(reserve_inventory_fn)

        restock_inventory_fn = _lambda.Function(
            self,
            "RestockInventoryFn",
            code=_lambda.Code.from_asset(src),
            handler="restock_inventory.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={"TABLE_NAME": ddb_table.table_name},
        )
        ddb_table.grant_write_data(restock_inventory_fn)

        """
        For each of the above lambda functions, an API Gateway LambdaIntegration.
        """
        integration_get = apigateway.LambdaIntegration(get_inventory_fn)
        integration_reserve = apigateway.LambdaIntegration(reserve_inventory_fn)
        integration_restock = apigateway.LambdaIntegration(restock_inventory_fn)

        """
        The API and a dev stage. Build paths with add_resource and add_method.
        """
        api = apigateway.RestApi(
            self,
            "inventory-api",
            deploy=True,
            deploy_options=apigateway.StageOptions(stage_name="dev"),
        )

        # GET /inventory/{product_id}
        inventory = api.root.add_resource("inventory")
        item = inventory.add_resource("{product_id}")
        item.add_method("GET", integration_get)

        # POST /inventory/reserve/
        reserve = inventory.add_resource("reserve")
        reserve.add_method("POST", integration_reserve)

        # POST /inventory/restock
        restock = inventory.add_resource("restock")
        restock.add_method("POST", integration_restock)
