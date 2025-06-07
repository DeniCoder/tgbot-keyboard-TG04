from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

inline_kb_links = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://mail.ru/")],
        [InlineKeyboardButton(text="Музыка", url="https://zaycev.net/pages/250362/25036214.shtml")],
        [InlineKeyboardButton(text="Видео", url="https://rutube.ru/video/f91bc57872bb347bdf1920e22dcc3056/?r=plemwd")],
    ]
)

inline_kb_dynamic = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
        ]
    )

new_kb_dynamic = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Опция 1", callback_data="opt1"),
                InlineKeyboardButton(text="Опция 2", callback_data="opt2")
            ]
        ]
    )