import base64
import os
import io

here = os.path.dirname(os.path.realpath(__file__))

def get_image(image_path):
  with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    decoded_image_bytes = base64.b64decode(encoded_image)
    image = io.BytesIO(decoded_image_bytes)
    return image