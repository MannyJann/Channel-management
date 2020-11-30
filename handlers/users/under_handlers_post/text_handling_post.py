from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentTypes, ReplyKeyboardRemove

from data.config import channel_s
from handlers.users.using import list_post
from keyboards.default import choosing
from loader import dp, bot
from states import channels_state, content_state


@dp.message_handler(content_types=ContentTypes.TEXT, state=channels_state.channels_post)
async def creating_post(message: types.Message, state: FSMContext):

    await state.update_data(creating_posting=message.text)
    list_post.append(message.text)
    await message.answer("Когда вы хотите выложить этот пост", reply_markup=choosing)
    await channels_state.creating_post.set()


@dp.message_handler(Text(equals="Выложить прямо сейчас"), state=channels_state.creating_post)
async def create_instantly(message: types.Message, state: FSMContext):

    await message.answer("Пост выложен", reply_markup=ReplyKeyboardRemove())
    data = await state.get_data()

    post_accept = data.get("creating_posting")
    await bot.send_message(text=post_accept, chat_id=channel_s[0])

    await state.finish()
