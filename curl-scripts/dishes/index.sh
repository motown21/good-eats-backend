#!/bin/bash

curl "http://localhost:8000/dishes" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
