import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    "ADMIN_ID"
]

channel_s = ["CHANNELS_ID"]

ip = os.getenv("ip")

list_times = []  # to this list will add var times_message[0, 1,...]

list_post = []

list_post_photo = []
list_photo_caption = []


loop = asyncio.get_event_loop()

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
