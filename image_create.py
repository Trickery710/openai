import openai
import requests
import json

openai.api_key = "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"


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

prompt = "Generate an image of a cat sitting on a couch."
image_url = generate_image(prompt)
print(image_url)
