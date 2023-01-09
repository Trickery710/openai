import requests

# Set the API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Read the API key from the api_key.txt file
with open(".key", "r") as f:
    api_key = f.read().strip()


headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}

# Set the request data
data = '{"model": "image-alpha-001", "prompt": "Generate an image of a savana cat umping over a couch.", "num_images":1, "size":"1024x1024", "response_format":"url"}'

# Send the request
response = requests.post(url, headers=headers, data=data)
print(headers)
# Print the response
print(response.json())
