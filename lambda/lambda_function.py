import base64
import telepot
import json
import os
import io

def send_to_telegram(image):
  TOKEN = os.environ['TELEGRAM_TOKEN']
  CHAT_ID = os.environ['CHAT_ID']

  bot = telepot.Bot(TOKEN)
  try:
    bot.sendPhoto(CHAT_ID, image)
  except Exception as e:
     print("error sending image to telegram channel")
     print(e)

def lambda_handler(event, context):
  try: 
    body = json.loads(event['body'])
    encoded_image = body['image']
    decoded_image_bytes = base64.b64decode(encoded_image)
    image = io.BytesIO(decoded_image_bytes)

    send_to_telegram(image)
  except Exception as e: 
        print(e)
        return





