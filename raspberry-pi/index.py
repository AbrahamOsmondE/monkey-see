import requests
import base64
import os

here = os.path.dirname(os.path.realpath(__file__))
lambda_url = os.environ['LAMBDA_URL']

# Input: bytes
def forward_image(image):
  encoded_image = base64.b64encode(image).decode('utf-8')
  payload = {
    "image": encoded_image
  }

  requests.post(lambda_url, json=payload)
