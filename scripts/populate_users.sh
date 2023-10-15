#!/bin/bash

# Define the base URL and endpoint
BASE_URL="http://localhost:4000/api/users/register"

# Array of JSON data
data=(
  '{
    "username": "JohnOkoro",
    "email": "john.okoro@example.com",
    "password": "password",
    "first_name": "John",
    "last_name": "Okoro"
  }'
  '{
    "username": "SarahSmith",
    "email": "sarah.smith@example.com",
    "password": "securepass456",
    "first_name": "Sarah",
    "last_name": "Smith"
  }'
  '{
    "username": "JohnDoe77",
    "email": "john.doe@example.net",
    "password": "myp@ssw0rd",
    "first_name": "John",
    "last_name": "Doe"
  }'
  '{
    "username": "EmilyJohnson",
    "email": "emily.johnson@example.org",
    "password": "P@ssw0rd123",
    "first_name": "Emily",
    "last_name": "Johnson"
  }'
  '{
    "username": "AlexBrown",
    "email": "alex.brown@example.com",
    "password": "Brownie987",
    "first_name": "Alex",
    "last_name": "Brown"
  }'
  '{
    "username": "LindaWilson",
    "email": "linda.wilson@example.net",
    "password": "L1nd@Pass",
    "first_name": "Linda",
    "last_name": "Wilson"
  }'
  '{
    "username": "MichaelClark",
    "email": "michael.clark@example.org",
    "password": "M1k3yP@ss",
    "first_name": "Michael",
    "last_name": "Clark"
  }'
  '{
    "username": "HannahMiller",
    "email": "hannah.miller@example.com",
    "password": "Mill3rPwd",
    "first_name": "Hannah",
    "last_name": "Miller"
  }'
  '{
    "username": "DanielSmith",
    "email": "daniel.smith@example.net",
    "password": "D@ni3lPass",
    "first_name": "Daniel",
    "last_name": "Smith"
  }'
  '{
    "username": "SophiaBrown",
    "email": "sophia.brown@example.org",
    "password": "Br0wniePie",
    "first_name": "Sophia",
    "last_name": "Brown"
  }'
)

total_items=${#data[@]}

# Loop through the data and make CURL POST requests
for ((i = 0; i < total_items; i++)); do
  json_data="${data[i]}"
  curl -X POST \
    "$BASE_URL" \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d "$json_data" &

  # Calculate progress
  progress=$((i * 100 / total_items))
  echo -ne "Progress: $progress% \r"
done

# Wait for all background CURL calls to finish
wait

echo "All requests completed."
