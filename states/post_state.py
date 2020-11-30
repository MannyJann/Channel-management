from aiogram.dispatcher.filters.state import State, StatesGroup


class channels_state(StatesGroup):
    channels_post = State()
    creating_post = State()
    accept_post = State()


class content_state(StatesGroup):
    content_text = State()
    content_photo = State()
