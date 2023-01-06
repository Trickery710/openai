#!/bin/bash

#YOUR_KEY="Authorization: Bearer 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"
YOUR_KEY="Authorization: Bearer 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"
# Use the API key in a curl command to make a request to the OpenAI API
response=$(curl -H "Authorization: Bearer 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" -X POST -H "Content-Type: application/json" -d '{"prompt": "What is the capital of France?", "model": "text-davinci-002"}' "https://api.openai.com/v1/completions?api_key=$YOUR_KEY")

echo "API response: $response"

