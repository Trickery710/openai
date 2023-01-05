import requests

# Set the API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set the API key
api_key ="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"

# Set the headers
headers = {
    "Authorization": "sk-zM6yTy3FgAdeSfUnXyObT3BlbkFJVKnLUuF17XcsekURy9k",
    "Content-Type": "application/json",
}

# Set the request data
data = '{"model": "image-alpha-001", "prompt": "Generate an image of a cat sitting on a couch.", "num_images":1, "size":"1024x1024", "response_format":"url"}'

# Send the request
response = requests.post(url, headers=headers, data=data)

# Print the response
print(response.json())
