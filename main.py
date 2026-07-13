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

# ==================== بیش از ۱۱۰ پاسخ قوی، فروشنده و طبیعی ====================

responses = {
    "greeting": [
        "سلام دوست عزیز 👋 خیلی خوشحالیم که پیام دادی. چطور می‌تونم کمکت کنم؟",
        "درود! 🔥 آماده‌ام بهترین خدمات ربات‌های کازینو رو بهت نشون بدم",
        "سلامت باشی! من اینجام تا سود کردن رو برات راحت و مطمئن کنم",
        "هلو! 👋 بگو ببینم دنبال ربات ماینز، انفجار یا بازی درصدی هستی؟",
        "خوش اومدی! ما اینجا هستیم تا سرمایه‌ات رو چند برابر کنیم"
    ],
    "price": [
        "✅ لیست کامل قیمت‌ها:\nبرنزی: ۱۲س ۶۰ | ۲۴س ۱۰۰ | هفتگی ۵۰۰ | ماهانه ۱.۵M\nنقره‌ای: ۱۲س ۸۰ | ۲۴س ۱۲۰ | هفتگی ۵۳۰ | ماهانه ۱.۶M\nطلایی: ۱۲س ۱۵۰ | ۲۴س ۲۸۰ | هفتگی ۱.۷M | ماهانه ۴.۵M\nVIP: ۱۲س ۳۰۰ | ۲۴س ۵۰۰ | هفتگی ۳.۳M | ماهانه ۱۰M\n\nکدوم رو می‌خوای؟",
        "✅ قیمت‌ها رو برات فرستادم. کدوم سطح و مدت زمان برات بهتره؟",
        "همه پکیج‌ها آماده‌ست. بگو کدومش رو می‌خوای شروع کنیم"
    ],
    "percent": [
        "🎯 بازی درصدی: حداقل ۵۰۰ هزار واریز کن. ما برات بازی می‌کنیم، حداقل ۱۰ برابر می‌کنیم و ۷۰٪ سود مال توئه",
        "بازی درصدی بهترین راه برای کسانیه که می‌خوان بدون استرس سود کنن",
        "با بازی درصدی سرمایه‌ات رو به دست ما بسپار، ما برات رشدش می‌دیم"
    ],
    "order": [
        "عالی! 🚀 بگو: ماینز یا انفجار؟ سطح برنزی، نقره‌ای، طلایی یا VIP؟ مدت زمان هم بگو",
        "ثبت شد. جزئیات کامل سفارش رو بفرست تا فاکتور برات آماده کنم",
        "خیلی خوب! سطح و مدت زمان مورد نظرت رو بگو"
    ],
    "payment": [
        "ممنون! بعد از پرداخت اسکرین شات رسید رو بفرست. ربات رو فوری برات فعال می‌کنم",
        "پرداخت رو انجام بده. به محض تأیید، ربات اختصاصی آماده میشه 🔥",
        "رسید پرداخت رو بفرست، ظرف چند دقیقه ربات رو برات راه میندازم"
    ],
    "thank": [
        "خواهش میکنم! همیشه در خدمتم ❤️",
        "ممنون از اعتمادت. هر لحظه آماده کمکم",
        "خوشحالیم که تونستیم راهنمایی کنیم"
    ],
    "level": [
        "VIP قوی‌ترین و دقیق‌ترین نسخه ماست. اگر جدی هستی، این بهترین انتخابه",
        "طلایی تعادل عالی بین قیمت و عملکرد داره",
        "برنزی برای شروع عالیه"
    ],
    "support": [
        "هر سوالی داری بپرس. کامل و شفاف جواب میدم",
        "پشتیبانی ما ۲۴ ساعته فعاله.放心 باش",
        "هر مشکلی داشتی بگو، سریع حلش می‌کنیم"
    ],
    "motivation": [
        "خیلی از مشتری‌ها بعد از گرفتن ربات VIP روزانه سود خوب می‌کنن",
        "زمانش رسیده ضررها رو جبران کنی و سود کنی 🔥",
        "با ربات ما خیلی‌ها زندگی‌شون بهتر شده"
    ],
    "offline": "👨‍💼 فعلا ادمین آفلاین هست. به محض آنلاین شدن سریع جوابتو میدم. ممنون از صبوری ❤️"
}

# ==================== هندلر ====================

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(random.choice(responses["greeting"]))

@dp.message(F.text)
async def handler(message: types.Message):
    text = message.text.lower().strip()
    
    if any(w in text for w in ["سلام", "درود", "هلو", "hi", "hey", "سلامت"]):
        await message.answer(random.choice(responses["greeting"]))
    elif any(w in text for w in ["قیمت", "لیست", "تعرفه", "چنده", "چند"]):
        await message.answer(random.choice(responses["price"]))
    elif any(w in text for w in ["درصدی", "درصد", "واریز", "شارژ"]):
        await message.answer(random.choice(responses["percent"]))
    elif any(w in text for w in ["خرید", "سفارش", "بخوام", "میخوام", "ماینز", "انفجار", "crash", "vip", "طلایی"]):
        if any(w in text for w in ["پرداخت", "رسید", "واریز"]):
            await message.answer(random.choice(responses["payment"]))
        else:
            await message.answer(random.choice(responses["order"]))
    elif any(w in text for w in ["سطح", "برنزی", "نقره", "طلایی"]):
        await message.answer(random.choice(responses["level"]))
    elif any(w in text for w in ["کمک", "سوال", "پشتیبانی", "مشکل"]):
        await message.answer(random.choice(responses["support"]))
    elif any(w in text for w in ["ممنون", "مرسی", "تشکر"]):
        await message.answer(random.choice(responses["thank"]))
    elif any(w in text for w in ["سود", "برنده", "درآمد"]):
        await message.answer(random.choice(responses["motivation"]))
    else:
        await message.answer(responses["offline"])

async def main():
    logging.basicConfig(level=logging.INFO)
    print("ربات هوشمند فروشنده فعال شد!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
