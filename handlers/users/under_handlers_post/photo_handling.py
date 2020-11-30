from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentTypes, ReplyKeyboardRemove

from data.config import channel_s, list_post_photo, list_photo_caption
from keyboards.default import choosing
from loader import dp, bot
from states import channels_state, content_state


@dp.message_handler(content_types=ContentTypes.PHOTO, state=channels_state.channels_post)
async def creating_post(message: types.Message, state: FSMContext):

    if message.caption:
        await state.update_data(caption_post=message.caption)
        list_photo_caption.append(message.caption)

    list_post_photo.append(message.photo[-1].file_id)
    print(list_post_photo)

    await state.update_data(creating_posting=message.photo[-1].file_id)
    await message.answer("Когда вы хотите выложить этот пост", reply_markup=choosing)
    await content_state.content_photo.set()


@dp.message_handler(Text(equals="Выложить прямо сейчас"), state=content_state.content_photo)
async def create_instantly_photo(message: types.Message, state: FSMContext):
    data = await state.get_data()

    post_accept = data.get("creating_posting")
    post_caption = data.get("caption_post")

    await bot.send_photo(chat_id=channel_s[0],
                         photo=post_accept,
                         caption=post_caption)
    list_post_photo.pop(0)

    await message.answer("Пост выложен", reply_markup=ReplyKeyboardRemove())

    await state.finish()
