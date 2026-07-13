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

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ==================== بیش از ۵۵ پاسخ حرفه‌ای و جذاب ====================

responses = {
    "greeting": [
        "سلام دوست عزیز 👋 به خدمات ربات‌های هوشمند کازینو خوش آمدی",
        "درود! خیلی خوشحالیم که اینجایی. چطور می‌تونم کمکت کنم؟",
        "سلامت باشی! آماده‌ام برات بهترین خدمات رو ارائه بدم",
        "هلو! 👋 منتظر پیامت بودم. بگو چی نیاز داری",
        "خوش اومدی! ما اینجا هستیم تا سودت رو چند برابر کنیم"
    ],
    "price": [
        "✅ لیست کامل قیمت ربات‌ها:\nبرنزی ۱۲ ساعته ۶۰ هزار - ۲۴ ساعته ۱۰۰ هزار\nنقره‌ای ۱۲ ساعته ۸۰ هزار - ۲۴ ساعته ۱۲۰ هزار\nطلایی ۱۲ ساعته ۱۵۰ هزار - ۲۴ ساعته ۲۸۰ هزار\nVIP ۱۲ ساعته ۳۰۰ هزار - ۲۴ ساعته ۵۰۰ هزار",
        "✅ لیست قیمت به روز شد. کدوم سطح و مدت زمان رو می‌خوای؟",
        "همه قیمت‌ها آماده است. بگو کدوم پکیج مدنظرت هست"
    ],
    "percent": [
        "✅ بازی درصدی: حداقل واریز ۵۰۰ هزار تومان. ما به جات بازی میکنیم حداقل ۱۰ برابر و ۷۰ درصد سود مال توست",
        "🎯 بازی درصدی یکی از بهترین خدمات ماست. مبلغ واریزی رو بگو",
        "بازی درصدی فعاله. آماده‌ای سرمایه‌ات رو چند برابر کنیم؟"
    ],
    "order": [
        "✅ درخواستت ثبت شد. لطفا بگو: نام ربات (ماینز یا انفجار) + سطح + مدت زمان",
        "عالی! جزئیات سفارش رو بفرست تا فاکتور برات آماده کنم",
        "ثبت شد. سطح و مدت زمان مورد نظرت رو بگو"
    ],
    "payment": [
        "✅ بعد از پرداخت اسکرین شات رسید رو بفرست تا ربات رو فوری برات فعال کنم",
        "ممنون! رسید پرداخت رو ارسال کن، ظرف چند دقیقه ربات اختصاصی آماده میشه",
        "پرداخت انجام بده. بعد از تأیید رسید، ربات رو برات می‌سازم"
    ],
    "thank": [
        "خواهش میکنم! همیشه در خدمتم ❤️",
        "ممنون از تو! هر سوالی داشتی بپرس",
        "خوشحالیم که تونستیم کمک کنیم",
        "مرسی! منتظر سفارش بعدی‌ات هستیم"
    ],
    "level": [
        "برنزی: مناسب شروع با دقت خوب",
        "نقره‌ای: دقت بالاتر و سیگنال بیشتر",
        "طلایی: عملکرد عالی برای حرفه‌ای‌ها",
        "VIP: قوی‌ترین نسخه با دقت بسیار بالا و الگوریتم اختصاصی"
    ],
    "support": [
        "پشتیبانی ۲۴ ساعته داریم. هر سوالی داری بپرس",
        "ما تا آخر کنارتم. هر مشکلی داشتی بگو",
        "سوالی در مورد ربات یا بازی درصدی داری؟ راحت بپرس"
    ],
    "motivation": [
        "خیلی از مشتری‌ها با این ربات‌ها سود عالی بردن. نوبت توئه",
        "زمان جبران ضررها و شروع سود کردن رسیده 🔥",
        "با نسخه VIP نتایج خیلی بهتری می‌گیری",
        "هر روز مشتری‌های جدید دارن با ربات ما سود می‌کنن"
    ],
    "offline": "👨‍💼 ادمین فعلا آفلاین است.\nبه محض آنلاین شدن پیامت رو بررسی و جواب میدم.\nممنون از صبوری‌ات ❤️"
}

# ==================== هندلر هوشمند ====================

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(random.choice(responses["greeting"]))

@dp.message(F.text)
async def handler(message: types.Message):
    text = message.text.lower().strip()
    
    # سلام
    if any(w in text for w in ["سلام", "درود", "هلو", "hi", "hey", "سلامت"]):
        await message.answer(random.choice(responses["greeting"]))
    
    # قیمت
    elif any(w in text for w in ["قیمت", "لیست", "تعرفه", "چنده", "چند"]):
        await message.answer(random.choice(responses["price"]))
    
    # بازی درصدی
    elif any(w in text for w in ["درصدی", "درصد", "واریز", "شارژ"]):
        await message.answer(random.choice(responses["percent"]))
    
    # سفارش
    elif any(w in text for w in ["خرید", "سفارش", "بخوام", "میخوام", "ماینز", "انفجار", "crash", "vip"]):
        if any(w in text for w in ["پرداخت", "رسید", "واریز کردم"]):
            await message.answer(random.choice(responses["payment"]))
        else:
            await message.answer(random.choice(responses["order"]))
    
    # سطوح
    elif any(w in text for w in ["برنزی", "نقره", "طلایی", "سطح"]):
        await message.answer(random.choice(responses["level"]))
    
    # پشتیبانی
    elif any(w in text for w in ["کمک", "سوال", "پشتیبانی", "مشکل", "نمیفهمم"]):
        await message.answer(random.choice(responses["support"]))
    
    # تشکر
    elif any(w in text for w in ["ممنون", "مرسی", "تشکر"]):
        await message.answer(random.choice(responses["thank"]))
    
    # انگیزشی
    elif any(w in text for w in ["سود", "برنده", "درآمد"]):
        await message.answer(random.choice(responses["motivation"]))
    
    # پیش‌فرض
    else:
        await message.answer(responses["offline"])

async def main():
    logging.basicConfig(level=logging.INFO)
    print("ربات هوشمند با موفقیت شروع به کار کرد!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
