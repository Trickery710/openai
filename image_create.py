import openai
import requestsc
from PIL import Image
from io import BytesIO


# Read the API key from the api_key.txt file
with open(".key", "r") as f:
    OPENAI_API_KEY = f.read().strip()

# Set the API key
def generate_image(prompt):
  model_engine = "image-alpha-001"
  prompt = (f"{prompt}")

  completions = openai.Image.create(
      #engine=model_engine,
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
