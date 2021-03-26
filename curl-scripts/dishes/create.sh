#!/bin/bash

curl "http://localhost:8000/dishes" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "dish": {
      "name": "'"${NAME}"'",
      "price": "'"${PRICE}"'",
      "description": "'"${DESCRIPTION}"'",
      "upload": "'"${UPLOAD}"'"
    }
  }'

echo
