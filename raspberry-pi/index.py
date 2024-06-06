import requests
import base64
import os

here = os.path.dirname(os.path.realpath(__file__))
lambda_url = os.environ['LAMBDA_URL']

# Input: bytes
def forward_image(image, caption):
  encoded_image = base64.b64encode(image).decode('utf-8')
  payload = {
    "image": encoded_image,
    "caption": caption
  }

  response = requests.post(lambda_url, json=payload)
  print(response.json())

# SAMPLE USAGE:
def get_image(image_path):
  with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    return image_data

forward_image(get_image(os.path.join(here, "../lambda/tests/monkey.jpg")), "this is a monkey")