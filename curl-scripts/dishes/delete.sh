#!/bin/bash

curl "http://localhost:8000/dishes/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
