import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lambda_function import send_to_telegram
from test_utils import get_image

here = os.path.dirname(os.path.realpath(__file__))

def should_send_image_to_telegram():
  try:
    image = get_image(os.path.join(here, 'monkey.jpg'))

    send_to_telegram(image, "file name: monkey.jpg")
  except Exception as e:
    print(e)
    return


should_send_image_to_telegram()