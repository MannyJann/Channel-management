from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choosing = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выложить прямо сейчас"),
            KeyboardButton(text="Назначить время")
        ],
        [
            KeyboardButton(text="Отменить")
        ]

    ],
    resize_keyboard=True
)