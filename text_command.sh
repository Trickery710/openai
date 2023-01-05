#!/bin/bash
user_input=($1)
api_key="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"
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $api_key" \
  -d '{
  "model": "text-davinci-003",
  "prompt": "$user_input",
  "temperature": 0,
  "max_tokens": 100,
  "top_p": 1.0,
  "frequency_penalty": 0.2,
  "presence_penalty": 0.0,
  "stop": ["\n"]
}'
