import requests

# Set the API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set the API key
#YOUR_KEY="Authorization: Bearer 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"# Set the headers
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}

# Set the request data
data = '{"model": "image-alpha-001", "prompt": "Generate an image of a cat sitting on a couch.", "num_images":1, "size":"1024x1024", "response_format":"url"}'

# Send the request
response = requests.post(url, headers=headers, data=data)

# Print the response
print(response.json())
