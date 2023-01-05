#!/bin/bash
YOUR_KEY="Authorization: Bearer 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"



curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
  "model": "code-davinci-002",
  "prompt": "\"\"\"\nUtil exposes the following:\nutil.openai() -> authenticates & returns the openai module, which has the following functions:\nopenai.Completion.create(\n    prompt=\"<my prompt>\", # The prompt to start completing from\n    max_tokens=123, # The max number of tokens to generate\n    temperature=1.0 # A measure of randomness\n    echo=True, # Whether to return the prompt in addition to the generated completion\n)\n\"\"\"\nimport util\n\"\"\"\nCreate an OpenAI completion starting from the prompt \"Once upon an AI\", no more than 5 tokens. Does not include the prompt.\n\"\"\"\n",
  "temperature": 0,
  "max_tokens": 64,
  "top_p": 1.0,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0,
  "stop": ["\"\"\""]
}'