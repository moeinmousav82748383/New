import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN
from keyboards import start_keyboard, next_keyboard
from image_generator import generator
from states import MinesStates

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 <b>سلام امیر جان!</b>\n\n"
        "به بات تشخیص ضریب Mines خوش آمدی ⚡\n\n"
        "✅ دقت تشخیص:\n"
        "• تعداد الماس زیر ۱۰ → خطای حدود ۳٪\n"
        "• تعداد الماس بالای ۱۰ → خطای حدود ۸٪\n\n"
        "روی دکمه زیر بزن و تعداد الماس مورد نظرت رو وارد کن:",
        reply_markup=start_keyboard(),
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "detect_mines")
async def detect_mines(callback: CallbackQuery, state: FSMContext):
    """هندلر مشترک برای شروع تشخیص"""
    await callback.message.edit_text(
        "💎 تعداد الماس را وارد کنید (۱ تا ۲۰):\n\n"
        "دقت کن: زیر ۱۰ تا دقت بالاتر، بالای ۱۰ دقت کمی کمتره."
    )
    await state.set_state(MinesStates.waiting_for_diamonds)
    await callback.answer("✅ شروع شد")

@dp.message(MinesStates.waiting_for_diamonds)
async def get_number(message: Message, state: FSMContext):
    try:
        num = int(message.text.strip())
        if not 1 <= num <= 20:
            raise ValueError
    except:
        await message.answer("❌ لطفاً یک عدد صحیح بین ۱ تا ۲۰ وارد کنید.")
        return

    await message.answer("⏳ در حال ساخت تصویر...")

    try:
        img_path = generator.generate(num)
        photo = FSInputFile(img_path)
        
        await message.answer_photo(
            photo=photo,
            caption="✅ نتیجه تشخیص ضریب آماده شد!",
            reply_markup=next_keyboard()
        )
        
        if os.path.exists(img_path):
            os.remove(img_path)
            
    except Exception as e:
        logging.error(f"Error: {e}")
        await message.answer("❌ خطا در ساخت تصویر. دوباره امتحان کن.")

    await state.clear()

async def main():
    print("🚀 بات شروع شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
