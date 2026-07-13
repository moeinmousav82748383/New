import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from config import BOT_TOKEN
from image_generator import generator

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def show_expired(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 تماس برای تمدید", url="https://t.me/moein481")]
    ])
    
    await message.answer(
        "⚠️ <b>اشتراک شما به پایان رسیده است!</b>\n\n"
        "برای تمدید اشتراک و استفاده دوباره از بات،\n"
        "به آیدی زیر پیام بده:\n\n"
        "@moein481",
        reply_markup=keyboard,
        parse_mode="HTML"
    )


@dp.message(Command("start"))
async def start(message: Message):
    await show_expired(message)


@dp.message()
async def any_message(message: Message):
    await show_expired(message)


async def main():
    print("🚀 بات شروع شد...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
