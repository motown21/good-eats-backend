#!/bin/bash

curl "http://localhost:8000/dishes/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "mango": {
      "name": "'"${NAME}"'",
      "price": "'"${PRICE}"'",
      "description": "'"${DESCRIPTION}"'",
      "upload": "'"${UPLOAD}"'"
    }
  }'

echo
