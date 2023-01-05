import openai
import requests
from PIL import Image
from io import BytesIO

YOUR_KEY="Authorization: Bearer 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"

# Read the API key from the api_key.txt file
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# Set the API key
openai.api_key = api_key

def generate_image(prompt):
  model_engine = "image-alpha-001"
  prompt = (f"{prompt}")

  completions = openai.Image.create(
      engine=model_engine,
      prompt=prompt,
      n=1,
      size="1024x1024",
      response_format="url"
  )

  return completions.data[0].url

# Get the image prompt from the user
prompt = input("Enter a description of the image that you want to generate: ")

# Generate the image
image_url = generate_image(prompt)

# Download the image and display it
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
