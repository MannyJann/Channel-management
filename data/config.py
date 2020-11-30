import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    872264536
    # os.getenv("ADMIN_ID"),
    # os.getenv("ADMIN_ID2")
]

channel_s = ["-1001473640888"]

ip = os.getenv("ip")

list_times = []  # В этот список будет добавляться переменная times_message[0, 1,...]

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
