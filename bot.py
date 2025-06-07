from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message
from config import BOT_TOKEN
import asyncio
from keyboard import keyboard, inline_kb_links, inline_kb_dynamic, new_kb_dynamic

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Задание 1: простое меню с кнопками "Привет" и "Пока"
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Нажмите на одну из предлагаемых кнопок", reply_markup=keyboard)

@dp.message(F.text == "Привет")
async def on_hello(message: Message):
    name = message.from_user.first_name or "пользователь"
    await message.answer(f"Привет, {name}!")

@dp.message(F.text == "Пока")
async def on_bye(message: Message):
    name = message.from_user.first_name or "пользователь"
    await message.answer(f"До свидания, {name}!")

# Задание 2: инлайн-кнопки с URL-ссылками
@dp.message(Command("links"))
async def cmd_links(message: Message):
    await message.answer("Полезные ссылки:", reply_markup=inline_kb_links)

# Задание 3: динамическое изменение клавиатуры
@dp.message(Command("dynamic"))
async def cmd_dynamic(message: Message):
    await message.answer("Нажмите кнопку:", reply_markup=inline_kb_dynamic)

@dp.callback_query(F.data == "show_more")
async def on_show_more(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=new_kb_dynamic)
    await call.answer()

@dp.callback_query(F.data.in_(["opt1", "opt2"]))
async def on_option_selected(call: CallbackQuery):
    option_text = "Опция 1" if call.data == "opt1" else "Опция 2"
    await call.message.edit_reply_markup(reply_markup=inline_kb_dynamic)
    await call.message.answer(f"Вы выбрали {option_text}")
    await call.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
