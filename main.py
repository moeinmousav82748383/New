import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import os

# ==================== تنظیمات ====================
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN پیدا نشد! لطفاً در تنظیمات Railway متغیر رو اضافه کنید.")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# ==================== بانک پاسخ‌ها (بیش از ۲۵ پاسخ) ====================

responses = {
    "greeting": [
        "سلام دوست عزیز 👋\nبه خدمات ربات‌های هوشمند کازینو خوش آمدی 🔥",
        "درود! خیلی خوشحالیم که اینجایی. چطور می‌تونم کمکت کنم؟ 💰",
        "سلامت باشی! آماده‌ام برات بهترین خدمات رو ارائه بدم.",
        "هلو! 👋 منتظر پیامت بودم."
    ],
    
    "price": [
        """✅ <b>لیست کامل قیمت ربات‌ها</b>

<b>ربات ماینز یا انفجار (جداگانه):</b>

<b>اشتراک برنزی:</b>
• ۱۲ ساعته: ۶۰ هزار تومان
• ۲۴ ساعته: ۱۰۰ هزار تومان
• هفتگی: ۵۰۰ هزار تومان
• ماهانه: ۱,۵۰۰,۰۰۰ تومان

<b>اشتراک نقره‌ای:</b>
• ۱۲ ساعته: ۸۰ هزار تومان
• ۲۴ ساعته: ۱۲۰ هزار تومان
• هفتگی: ۵۳۰ هزار تومان
• ماهانه: ۱,۶۰۰,۰۰۰ تومان

<b>اشتراک طلایی:</b>
• ۱۲ ساعته: ۱۵۰ هزار تومان
• ۲۴ ساعته: ۲۸۰ هزار تومان
• هفتگی: ۱,۷۰۰,۰۰۰ تومان
• ماهانه: ۴,۵۰۰,۰۰۰ تومان

<b>اشتراک VIP:</b>
• ۱۲ ساعته: ۳۰۰ هزار تومان
• ۲۴ ساعته: ۵۰۰ هزار تومان
• هفتگی: ۳,۳۰۰,۰۰۰ تومان
• ماهانه: ۱۰,۰۰۰,۰۰۰ تومان

برای سفارش بگو مثلاً: «ماینز طلایی ماهانه»""",
        "✅ لیست قیمت‌ها رو برات فرستادم. کدوم پکیج رو می‌خوای؟"
    ],
    
    "percent": [
        "✅ <b>بازی درصدی</b>\n\nحداقل واریز: ۵۰۰ هزار تومان\nما به جات بازی می‌کنیم (حداقل ۱۰ برابر) و ۷۰٪ سود مال توئه.\nمبلغ واریزی رو بگو.",
        "🎯 بازی درصدی فعاله! از ۵۰۰ هزار شروع کن. ۷۰٪ سود به حسابت برمی‌گرده."
    ],
    
    "order": [
        "✅ درخواست ثبت شد! لطفاً بگو:\n• ربات (ماینز یا انفجار)\n• سطح\n• مدت زمان",
        "عالیه! 🚀 جزئیات سفارش رو بگو (مثلاً: انفجار نقره‌ای هفتگی)"
    ],
    
    "payment": [
        "✅ بعد از پرداخت، اسکرین شات رسید رو بفرست تا فوری ربات رو فعال کنم.",
        "ممنون! رسید پرداخت رو بفرست، سریع فعال‌سازی می‌کنم 🔥"
    ],
    
    "thank": ["خواهش می‌کنم! ❤️", "ممنون از تو!", "خوشحالیم که کمکتون کردیم 💙"],
    
    "offline": "👨‍💼 ادمین در حال حاضر آفلاین است.\nبه محض آنلاین شدن، پیامت رو بررسی و جواب می‌ده.\nممنون از صبوری‌ات ❤️"
}

# ==================== هندلرها ====================

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(random.choice(responses["greeting"]))

@dp.message(F.text)
async def smart_handler(message: types.Message):
    text = message.text.lower().strip()
    
    if any(w in text for w in ["سلام", "درود", "هلو", "hi", "hey"]):
        await message.answer(random.choice(responses["greeting"]))
        return
    
    if any(w in text for w in ["قیمت", "لیست", "هزینه", "تعرفه", "چنده"]):
        await message.answer(random.choice(responses["price"]))
        return
    
    if any(w in text for w in ["درصدی", "درصد", "واریز", "شارژ"]):
        await message.answer(random.choice(responses["percent"]))
        return
    
    if any(w in text for w in ["خرید", "سفارش", "ماینز", "انفجار", "crash", "طلایی", "نقره", "برنز", "vip"]):
        if any(w in text for w in ["پرداخت", "رسید", "واریز کردم"]):
            await message.answer(random.choice(responses["payment"]))
        else:
            await message.answer(random.choice(responses["order"]))
        return
    
    if any(w in text for w in ["ممنون", "مرسی", "تشکر"]):
        await message.answer(random.choice(responses["thank"]))
        return
    
    # پاسخ پیش‌فرض
    await message.answer(responses["offline"])

# ==================== اجرا ====================

async def main():
    logging.basicConfig(level=logging.INFO)
    print("🤖 ربات هوشمند با موفقیت راه‌اندازی شد!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())• ۱۲ ساعته: ۸۰ هزار تومان
• ۲۴ ساعته: ۱۲۰ هزار تومان
• هفتگی: ۵۳۰ هزار تومان
• ماهانه: ۱,۶۰۰,۰۰۰ تومان

<b>اشتراک طلایی:</b>
• ۱۲ ساعته: ۱۵۰ هزار تومان
• ۲۴ ساعته: ۲۸۰ هزار تومان
• هفتگی: ۱,۷۰۰,۰۰۰ تومان
• ماهانه: ۴,۵۰۰,۰۰۰ تومان

<b>اشتراک VIP (قوی‌ترین):</b>
• ۱۲ ساعته: ۳۰۰ هزار تومان
• ۲۴ ساعته: ۵۰۰ هزار تومان
• هفتگی: ۳,۳۰۰,۰۰۰ تومان
• ماهانه: ۱۰,۰۰۰,۰۰۰ تومان

برای ثبت سفارش بگو مثلاً: «ماینز طلایی ماهانه»""",
        
        "✅ لیست قیمت‌ها رو برات فرستادم. کدوم پکیج مدنظرت هست؟"
    ],
    
    "percent_game": [
        "✅ <b>بازی درصدی</b>\n\nحداقل واریز: ۵۰۰ هزار تومان\nما به جات بازی می‌کنیم (حداقل ۱۰ برابر) و ۷۰٪ سود رو بهت برمی‌گردونیم.\nمبلغ مورد نظرت رو بگو تا راهنمایی کنم.",
        "🎯 بازی درصدی فعاله!\nاز ۵۰۰ هزار تومان شروع کن. ۷۰٪ سود مال توئه. آماده‌ای؟ مبلغ واریزی رو بگو."
    ],
    
    "order": [
        "✅ درخواستت ثبت شد!\nلطفاً دقیق بگو:\n• نام ربات (ماینز یا انفجار)\n• سطح (برنزی، نقره‌ای، طلایی، VIP)\n• مدت زمان\nتا فاکتور برات آماده کنم.",
        "عالی! 🚀 کدوم ربات، چه سطحی و برای چه مدتی می‌خوای؟"
    ],
    
    "payment": [
        "✅ لطفاً مبلغ رو پرداخت کن و اسکرین شات رسید رو برام بفرست.\nبعد از تأیید، ربات رو فوری برات فعال می‌کنم.",
        "ممنون! بعد از پرداخت، رسید رو بفرست تا سریع فعال‌سازی کنم 🔥"
    ],
    
    "thank": [
        "خواهش می‌کنم! همیشه در خدمتم 💙",
        "ممنون از تو! اگر سؤال دیگه‌ای داشتی بگو.",
        "خوشحالیم که تونستیم کمک کنیم ❤️"
    ],
    
    "goodbye": [
        "موفق باشی! منتظر سفارش بعدی‌ات هستیم 💰",
        "تا دیدار بعدی، مراقب خودت باش 🔥"
    ]
}

# ==================== هندلرها ====================

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(random.choice(responses["greeting"]))

@dp.message(F.text)
async def smart_handler(message: types.Message):
    text = message.text.lower().strip()
    
    # سلام و احوالپرسی
    if any(w in text for w in ["سلام", "درود", "سلامت", "خوش", "هلو", "hi", "hey"]):
        await message.answer(random.choice(responses["greeting"]))
        return
    
    # قیمت و لیست
    if any(w in text for w in ["قیمت", "لیست", "هزینه", "تعرفه", "چنده", "چند", "بده"]):
        await message.answer(random.choice(responses["price"]))
        return
    
    # بازی درصدی
    if any(w in text for w in ["درصدی", "درصد", "واریز", "شارژ حساب", "بازی درصد", "سود"]):
        await message.answer(random.choice(responses["percent_game"]))
        return
    
    # درخواست سفارش / خرید
    if any(w in text for w in ["خرید", "سفارش", "بخوام", "میخوام", "بده", "فعال", "ماینز", "انفجار", "crash", "طلایی", "نقره", "برنز", "vip"]):
        if "پرداخت" in text or "رسید" in text or "واریز" in text:
            await message.answer(random.choice(responses["payment"]))
        else:
            await message.answer(random.choice(responses["order"]))
        return
    
    # تشکر و خداحافظی
    if any(w in text for w in ["ممنون", "مرسی", "تشکر", "خداحافظ", "بای", "خدانگهدار"]):
        if any(w in text for w in ["خداحافظ", "بای", "خدانگهدار"]):
            await message.answer(random.choice(responses["goodbye"]))
        else:
            await message.answer(random.choice(responses["thank"]))
        return
    
    # پاسخ پیش‌فرض (ادمین آفلاین)
    await message.answer(
        "👨‍💼 ادمین در حال حاضر آفلاین است.\n"
        "به محض اینکه آنلاین شد، پیام شما رو بررسی و سریع جواب می‌ده.\n\n"
        "ممنون از صبوری‌ات ❤️"
    )

# ==================== راه‌اندازی ====================

async def main():
    logging.basicConfig(level=logging.INFO)
    print("🤖 ربات پاسخگوی هوشمند با موفقیت فعال شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
