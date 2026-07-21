import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_multiplier() -> str:
    """تولید ضریب رندوم بین ۱.۰۱ تا ۳.۱۷"""
    multiplier = round(random.uniform(1.01, 3.17), 2)
    return f"{multiplier:.2f}"


def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 تشخیص ضریب", callback_data="detect_crash")]
    ])


def next_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 تشخیص ضریب دست بعدی", callback_data="detect_crash")]
    ])


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 <b>سلام Moein جان!</b>\n\n"
        "🔰 <b>من Moein هستم</b>، دستیار تست اختصاصی تو.\n\n"
        "📊 <b>اشتراک تست - مدت نامحدود</b>\n"
        "⏳ این اشتراک برای تست و بدون محدودیت زمانی فعال است.\n\n"
        "⚠️ <b>توجه:</b> این تشخیص ضریب مخصوص سایت <b>ناسا بت</b> هست\n"
        "روی سایر سایت‌ها ممکن است دقت کمتری داشته باشد.\n\n"
        "برای شروع تشخیص ضریب روی دکمه زیر بزن 👇",
        reply_markup=main_keyboard(),
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "detect_crash")
async def detect_crash(callback):
    multiplier = get_multiplier()
    
    await callback.message.edit_text(
        "🔍 <b>در حال تشخیص ضریب...</b>",
        parse_mode="HTML"
    )
    
    await asyncio.sleep(1.5)
    
    await callback.message.answer(
        f"✅ <b>ضریب تشخیص داده شد!</b>\n\n"
        f"🔥 <code>{multiplier}</code> x\n\n"
        f"موفق باشی Moein جان ⚡",
        parse_mode="HTML",
        reply_markup=next_keyboard()
    )
    
    await callback.answer("ضریب تولید شد")


@dp.message()
async def other_messages(message: Message):
    await message.answer(
        "لطفاً از دکمه‌های موجود استفاده کن Moein جان.",
        reply_markup=main_keyboard()
    )


async def main():
    print("🚀 ربات تست شروع شد...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())        "👋 <b>سلام Amir جان!</b>\n\n"
        "🔰 <b>من Mamali هستم</b>، دستیار تشخیص ضریب اختصاصی تو.\n\n"
        "📊 <b>سطح نقره‌ای - اشتراک ۱۲ ساعته</b>\n"
        "⏳ اشتراک تا پایان ۱۲ ساعت معتبر است.\n\n"
        "⚠️ <b>توجه:</b> این تشخیص ضریب مخصوص سایت <b>ناسا بت</b> هست\n"
        "روی سایر سایت‌ها ممکن است دقت کمتری داشته باشد.\n\n"
        "برای شروع تشخیص ضریب روی دکمه زیر بزن 👇",
        reply_markup=main_keyboard(),
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "detect_crash")
async def detect_crash(callback):
    multiplier = get_multiplier()
    
    await callback.message.edit_text(
        "🔍 <b>در حال تشخیص ضریب...</b>",
        parse_mode="HTML"
    )
    
    await asyncio.sleep(1.5)
    
    await callback.message.answer(
        f"✅ <b>ضریب تشخیص داده شد!</b>\n\n"
        f"🔥 <code>{multiplier}</code> x\n\n"
        f"موفق باشی Amir جان ⚡",
        parse_mode="HTML",
        reply_markup=next_keyboard()
    )
    
    await callback.answer("ضریب تولید شد")


@dp.message()
async def other_messages(message: Message):
    await message.answer(
        "لطفاً از دکمه‌های موجود استفاده کن Amir جان.",
        reply_markup=main_keyboard()
    )


async def main():
    print("🚀 ربات Mamali شروع شد...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
