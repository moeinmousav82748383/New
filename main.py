import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN پیدا نشد! لطفا در Variables Railway اضافه کنید.")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# ==================== بیش از ۴۲ پاسخ حرفه‌ای ====================

responses = {
    "greeting": [
        "سلام دوست عزیز 👋 به خدمات ربات‌های هوشمند کازینو خوش آمدی",
        "درود! خیلی خوشحالیم که اینجایی. چطور می‌تونم کمکت کنم؟",
        "سلامت باشی! آماده‌ام برات بهترین خدمات رو ارائه بدم",
        "هلو! منتظر پیامت بودم. بگو چطور کمکت کنم",
        "خوش اومدی! ما اینجا هستیم تا سودت رو چند برابر کنیم"
    ],
    "price": [
        "لیست قیمت:\nبرنزی ۱۲ساعته ۶۰ هزار - ۲۴ساعته ۱۰۰ هزار\nنقره‌ای ۱۲ساعته ۸۰ هزار - ۲۴ساعته ۱۲۰ هزار\nطلایی ۱۲ساعته ۱۵۰ هزار - ۲۴ساعته ۲۸۰ هزار\nVIP ۱۲ساعته ۳۰۰ هزار - ۲۴ساعته ۵۰۰ هزار\nبرای جزئیات کامل بگو قیمت",
        "✅ لیست کامل قیمت‌ها آماده است. کدوم سطح و مدت زمان مدنظرت هست؟"
    ],
    "percent": [
        "بازی درصدی: حداقل ۵۰۰ هزار تومان واریز کن. ما بازی میکنیم، حداقل ۱۰ برابر میکنیم و ۷۰ درصد سود مال توست",
        "🎯 بازی درصدی فعاله. مبلغ واریزی رو بگو تا شروع کنیم"
    ],
    "order": [
        "✅ درخواست ثبت شد. لطفا بگو: نام ربات + سطح + مدت زمان",
        "عالی! جزئیات سفارش (ماینز یا انفجار + سطح + زمان) رو بفرست"
    ],
    "payment": [
        "بعد از پرداخت اسکرین شات رسید رو بفرست تا ربات رو فوری فعال کنم",
        "ممنون! رسید پرداخت رو ارسال کن، سریع فعال‌سازی انجام میشه"
    ],
    "thank": [
        "خواهش میکنم! همیشه در خدمتم",
        "ممنون از تو! سؤال دیگه‌ای داشتی بگو",
        "خوشحالیم که کمکتون کردیم"
    ],
    "level": [
        "برنزی: مناسب شروع",
        "نقره‌ای: دقت بالاتر",
        "طلایی: عملکرد عالی",
        "VIP: قوی‌ترین نسخه با دقت بسیار بالا"
    ],
    "support": [
        "پشتیبانی ۲۴ ساعته داریم. هر سوالی داری بپرس",
        "ما تا آخر کنارتم. مشکلی هست بگو"
    ],
    "motivation": [
        "خیلی از مشتری‌ها با این ربات‌ها سود خوبی بردن. نوبت توئه",
        "زمان سود کردن رسیده 🔥",
        "با VIP می‌تونی نتایج خیلی بهتری بگیری"
    ],
    "offline": "👨‍💼 ادمین فعلا آفلاین است. به محض آنلاین شدن جوابتو میدم. ممنون از صبوری"
}

# ==================== هندلر ====================

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(random.choice(responses["greeting"]))

@dp.message(F.text)
async def handler(message: types.Message):
    text = message.text.lower()

    if any(word in text for word in ["سلام", "درود", "هلو", "hi"]):
        await message.answer(random.choice(responses["greeting"]))
    elif any(word in text for word in ["قیمت", "لیست", "چنده"]):
        await message.answer(random.choice(responses["price"]))
    elif any(word in text for word in ["درصدی", "درصد", "واریز", "شارژ"]):
        await message.answer(random.choice(responses["percent"]))
    elif any(word in text for word in ["خرید", "سفارش", "ماینز", "انفجار", "vip", "طلایی", "نقره"]):
        if any(word in text for word in ["پرداخت", "رسید"]):
            await message.answer(random.choice(responses["payment"]))
        else:
            await message.answer(random.choice(responses["order"]))
    elif any(word in text for word in ["سطح", "برنزی", "نقره", "طلایی"]):
        await message.answer(random.choice(responses["level"]))
    elif any(word in text for word in ["کمک", "سوال", "پشتیبانی", "مشکل"]):
        await message.answer(random.choice(responses["support"]))
    elif any(word in text for word in ["ممنون", "مرسی", "تشکر"]):
        await message.answer(random.choice(responses["thank"]))
    elif any(word in text for word in ["سود", "برنده"]):
        await message.answer(random.choice(responses["motivation"]))
    else:
        await message.answer(responses["offline"])

async def main():
    logging.basicConfig(level=logging.INFO)
    print("ربات با موفقیت شروع به کار کرد!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
