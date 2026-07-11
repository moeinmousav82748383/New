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
        "👋 <b>خوش آمدی به بات تشخیص ضریب Mines!</b>\n\n"
        "روی دکمه زیر کلیک کن و تعداد الماس مورد نظرت رو وارد کن:",
        reply_markup=start_keyboard(),
        parse_mode="HTML"
    )

@dp.callback_query(F.data == "detect_mines")
async def detect(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("💎 تعداد الماس را وارد کنید (۱ تا ۲۰):")
    await state.set_state(MinesStates.waiting_for_diamonds)
    await callback.answer()

@dp.message(MinesStates.waiting_for_diamonds)
async def get_number(message: Message, state: FSMContext):
    try:
        num = int(message.text.strip())
        if not 1 <= num <= 20:
            raise ValueError
    except:
        await message.answer("❌ لطفاً یک عدد بین ۱ تا ۲۰ وارد کنید.")
        return

    await message.answer("⏳ در حال ساخت تصویر...")

    try:
        img_path = generator.generate(num)
        
        # استفاده از FSInputFile برای Railway
        photo = FSInputFile(img_path)
        
        await message.answer_photo(
            photo=photo,
            caption="✅ نتیجه تشخیص ضریب آماده شد!",
            reply_markup=next_keyboard()
        )
        
        # پاک کردن فایل بعد از ارسال
        if os.path.exists(img_path):
            os.remove(img_path)
            
    except Exception as e:
        logging.error(f"Error generating image: {e}")
        await message.answer("❌ خطا در ساخت تصویر. دوباره امتحان کنید.")

    await state.clear()

async def main():
    print("🚀 بات شروع شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
