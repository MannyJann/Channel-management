import asyncio
import datetime

from data.config import list_times, list_post, list_post_photo, list_photo_caption, loop, channel_s
from loader import bot


async def breaking():
    while True:
        break


async def time_monitoring(loop):
    while True:
        await asyncio.sleep(1)
        if datetime.datetime.now().strftime("%H:%M") == list_times[0]:
            list_times.pop(0)
                        
            if list_post:
                await bot.send_message(chat_id=channel_s[0], text=list_post[0])
                list_post.pop(0)

            if list_post_photo:
                if list_photo_caption:
                    await bot.send_photo(chat_id=channel_s[0], photo=list_post_photo[0], caption=list_photo_caption[0])
                    list_post_photo.pop(0)
                    list_photo_caption.pop(0)

                elif not list_photo_caption:
                    await bot.send_photo(chat_id=channel_s[0], photo=list_post_photo[0])
                    list_post_photo.pop(0)

            break
    print("(10)")
