#!/bin/bash

# Set the API key
YOUR_KEY="Authorization: Bearer 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"

# Set the model and temperature for code completion
model="davinci"
temperature=0.5

# Function to get code completion from the API
get_completion() {
  local prompt=$1
  local model=$2
  local temperature=$3
  local response
  response=$(curl -X POST -H "Content-Type: application/json" -d "{\"prompt\": \"$prompt\", \"model\": \"$model\", \"max_tokens\": 1024, \"n\": 1, \"stop\": null, \"temperature\": $temperature}" "https://api.openai.com/v1/completions?api_key=$YOUR_KEY")
  local message=$(echo "$response" | jq -r '.choices[0].text')
  echo "$message"
}

# Loop to prompt the user for input and generate code completion
while true; do
  read -p "Enter your code: " user_input
  completion=$(get_completion "$user_input" "$model" "$temperature")
  echo "Code completion: $completion"
done
