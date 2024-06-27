#!/usr/bin/env python3

import aws_cdk as cdk

from inventory_api.inventory_api_stack import InventoryApiStack

app = cdk.App()


InventoryApiStack(
    app,
    "InventoryApiStack",
)

app.synth()
