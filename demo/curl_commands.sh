# commands 

# Example deployed API endpoint:
# https://irh7tzw74g.execute-api.us-east-1.amazonaws.com/dev

# GET /inventory/{product_id}:
curl -X GET "https://irh7tzw74g.execute-api.us-east-1.amazonaws.com/dev/inventory/tshirt001"

# POST /inventory/reserve:
curl -X POST "https://irh7tzw74g.execute-api.us-east-1.amazonaws.com/dev/inventory/reserve" \
-H "Content-Type: application/json" \
-d '{"product_id": "tshirt001", "quantity": 10}'

# POST /inventory/restock:
curl -X POST "https://irh7tzw74g.execute-api.us-east-1.amazonaws.com/dev/inventory/restock" \
-H "Content-Type: application/json"
