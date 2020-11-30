import asyncio
import threading

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, ContentTypes

from data.config import admins, list_times, list_post, loop, list_photo_caption, list_post_photo
from loader import dp, bot
from states import channels_state, state_time, content_state
from utils.misc.time_control import time_monitoring, breaking


@dp.message_handler(Command("np"))
async def message_control(message: types.Message):
    for admin in admins:
        if message.from_user.id in admins:
            await bot.send_message(chat_id=admin,
                                   text="Отправьте мне пост который хотите опубликовать в канале.")
            await channels_state.channels_post.set()


@dp.message_handler(Text(equals="Назначить время"), state=(channels_state.creating_post, content_state.content_photo))
async def selection_time(message: types.Message):
    await message.answer("Назначьте время, в формате hh:mm", reply_markup=ReplyKeyboardRemove())

    await state_time.one_time.set()


@dp.message_handler(content_types=ContentTypes.TEXT, state=state_time.one_time)
async def warning_time(message: types.Message, state: FSMContext):
    times_message = message.text

    list_times.append(times_message)
    print(list_times)
    print(list_post)
    if times_message:
        asyncio.ensure_future(time_monitoring(loop))
        asyncio.ensure_future(breaking())

    await state.finish()


@dp.message_handler(Text(equals="Отменить"), state="*")
async def cancel_posting(message: types.Message, state: FSMContext):
    await message.answer("Вы отменили", reply_markup=ReplyKeyboardRemove())
    list_post.pop(0)

    await state.finish()
