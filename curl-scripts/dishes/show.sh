#!/bin/bash

curl "http://localhost:8000/dishes/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
