import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN
from image_generator import generator
from states import MinesStates

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def show_subscription_expired(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 تماس برای تمدید", url="https://t.me/moein481")]
    ])
    
    await message.answer(
        "⚠️ <b>اشتراک شما به پایان رسیده است!</b>\n\n"
        "برای تمدید اشتراک و ادامه استفاده از بات،\n"
        "به آیدی زیر پیام بده:\n\n"
        "@moein481",
        reply_markup=keyboard,
        parse_mode="HTML"
    )


@dp.message(Command("start"))
async def start(message: Message):
    await show_subscription_expired(message)


# اگر کسی بعد از استارت عدد فرستاد، دوباره پیام اشتراک رو نشون بده
@dp.message()
async def any_message(message: Message):
    await show_subscription_expired(message)


async def main():
    print("🚀 بات شروع شد...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())async def renew_subscription(callback: CallbackQuery):
    await callback.message.edit_text(
        "✅ اشتراک با موفقیت تمدید شد!\n\n"
        "حالا می‌تونی از بات استفاده کنی امیر جان ⚡\n\n"
        "تعداد الماس مورد نظرت رو وارد کن (۱ تا ۲۰):"
    )
    # اینجا می‌تونی استیت رو ست کنی اگر خواستی مستقیم بره به دریافت عدد
    await callback.answer("اشتراک تمدید شد")

# برای سادگی فعلاً بدون FSM کامل نگه داشتم
# اگر خواستی FSM کامل باشه بگو

@dp.message()
async def handle_messages(message: Message):
    # اگر بعد از تمدید عدد فرستاد
    if message.text and message.text.isdigit():
        num = int(message.text)
        if 1 <= num <= 20:
            await message.answer("⏳ در حال ساخت تصویر...")
            try:
                img_path = generator.generate(num)
                photo = FSInputFile(img_path)
                
                await message.answer_photo(
                    photo=photo,
                    caption="✅ نتیجه تشخیص ضریب آماده شد!",
                    reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="✅ تشخیص ضریب دست بعدی", callback_data="renew_subscription")]
                    ])
                )
                if os.path.exists(img_path):
                    os.remove(img_path)
            except:
                await message.answer("❌ خطا در ساخت تصویر.")
            return
    
    await message.answer("ابتدا /start بزن.")

async def main():
    print("🚀 بات شروع شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())        "دقت کن: زیر ۱۰ تا دقت بالاتر، بالای ۱۰ دقت کمی کمتره."
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
