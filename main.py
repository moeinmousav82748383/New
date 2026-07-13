from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random

# ==================== تنظیمات ====================
API_ID = 12345678          # ← این رو با API_ID خودت عوض کن
API_HASH = "your_api_hash_here"  # ← این رو با API_HASH خودت عوض کن
PHONE = "+989055136616"

app = Client("MoeinAgent", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)

# ==================== بیش از ۱۲۰ پاسخ قوی، طبیعی و فروشنده ====================

responses = {
    "greeting": [
        "سلام دوست عزیز 👋 خیلی خوشحالیم که پیام دادی. چطور می‌تونم کمکت کنم؟",
        "درود! 🔥 آماده‌ام برات بهترین خدمات ربات‌های کازینو رو ارائه بدم",
        "سلامت باشی! من اینجام تا سود کردن رو برات راحت و مطمئن کنم",
        "هلو! 👋 بگو ببینم دنبال ربات ماینز، انفجار یا بازی درصدی هستی؟",
        "خوش اومدی! ما اینجا هستیم تا سرمایه‌ات رو چند برابر کنیم",
        "سلام! چطور می‌تونم بهت کمک کنم تا سود خوبی ببری؟",
        "درود بر تو! آماده کمک بهت هستم"
    ],
    "price": [
        "✅ لیست کامل قیمت ربات‌ها:\n\nبرنزی: ۱۲ ساعته ۶۰ | ۲۴ ساعته ۱۰۰ | هفتگی ۵۰۰ | ماهانه ۱.۵ میلیون\nنقره‌ای: ۱۲ ساعته ۸۰ | ۲۴ ساعته ۱۲۰ | هفتگی ۵۳۰ | ماهانه ۱.۶ میلیون\nطلایی: ۱۲ ساعته ۱۵۰ | ۲۴ ساعته ۲۸۰ | هفتگی ۱.۷ میلیون | ماهانه ۴.۵ میلیون\nVIP: ۱۲ ساعته ۳۰۰ | ۲۴ ساعته ۵۰۰ | هفتگی ۳.۳ میلیون | ماهانه ۱۰ میلیون\n\nکدوم پکیج رو می‌خوای شروع کنیم؟",
        "✅ قیمت‌ها رو برات فرستادم. کدوم سطح و مدت زمان برات جذاب‌تره؟",
        "همه پکیج‌ها با تحویل فوری آماده‌ست. بگو کدوم رو می‌خوای",
        "لیست قیمت به روز شد. آماده‌ای یکی رو انتخاب کنی؟"
    ],
    "percent": [
        "🎯 بازی درصدی: حداقل ۵۰۰ هزار تومان واریز کن. ما به جات بازی می‌کنیم (حداقل ۱۰ برابر) و ۷۰٪ سود مال توئه",
        "بازی درصدی بهترین گزینه برای کسانیه که نمی‌خوان خودشون ریسک کنن",
        "با بازی درصدی سرمایه‌ات رو به دست تیم حرفه‌ای ما بسپار",
        "بازی درصدی خیلی پرطرفداره. مبلغ واریزی رو بگو"
    ],
    "order": [
        "عالی! 🚀 بگو: ماینز یا انفجار؟ سطح (برنزی، نقره‌ای، طلایی، VIP) و مدت زمان رو هم بگو",
        "ثبت شد. جزئیات کامل سفارش رو بفرست تا فاکتور برات آماده کنم",
        "خیلی خوب! سطح و مدت زمان مورد نظرت رو اعلام کن",
        "درخواستت ثبت شد. حالا بگو کدوم ربات و چه مدتی می‌خوای"
    ],
    "payment": [
        "ممنون! بعد از پرداخت اسکرین شات رسید رو بفرست. ربات رو فوری برات فعال می‌کنم",
        "پرداخت رو انجام بده. به محض تأیید رسید، ربات اختصاصی آماده میشه 🔥",
        "رسید پرداخت رو بفرست، ظرف حداکثر ۱۰ دقیقه ربات رو برات راه میندازم",
        "ممنون از اعتمادت. رسید رو بفرست تا سریع فعال‌سازی کنم"
    ],
    "thank": [
        "خواهش میکنم! همیشه در خدمتم ❤️",
        "ممنون از اعتمادت. هر لحظه آماده کمکم",
        "خوشحالیم که تونستیم راهنمایی کنیم",
        "مرسی! منتظر سفارش بعدی‌ات هستیم"
    ],
    "level": [
        "VIP قوی‌ترین و دقیق‌ترین نسخه ماست. اگر جدی هستی، این بهترین انتخابه",
        "طلایی تعادل عالی بین قیمت و عملکرد داره",
        "برنزی برای شروع و تست خیلی مناسبه",
        "نقره‌ای دقت خوبی داره و برای اکثر کاربرها کافیه"
    ],
    "support": [
        "هر سوالی داری بپرس. کامل و شفاف جواب میدم",
        "پشتیبانی ما ۲۴ ساعته فعاله.放心 باش",
        "هر مشکلی داشتی بگو سریع حلش می‌کنیم",
        "من اینجام تا همه سوالاتت رو جواب بدم"
    ],
    "motivation": [
        "خیلی از مشتری‌ها با ربات ما روزانه سود خوب می‌کنن. تو هم می‌تونی",
        "زمان جبران ضررها و شروع سود کردن رسیده 🔥",
        "با نسخه VIP نتایج خیلی بهتری می‌گیری",
        "هر روز مشتری‌های جدید دارن با این ربات‌ها سود می‌کنن"
    ],
    "offline": "👨‍💼 فعلا مشغولم. به محض فرصت سریع جوابتو میدم. ممنون از صبوری ❤️"
}

# ==================== هندلر ====================

@app.on_message(filters.private & \~filters.me)
async def reply_handler(client, message: Message):
    if not message.text:
        return
    
    text = message.text.lower().strip()
    
    if any(w in text for w in ["سلام", "درود", "هلو", "hi", "hey", "سلامت", "خوش"]):
        await message.reply(random.choice(responses["greeting"]))
    elif any(w in text for w in ["قیمت", "لیست", "تعرفه", "چنده", "چند"]):
        await message.reply(random.choice(responses["price"]))
    elif any(w in text for w in ["درصدی", "درصد", "واریز", "شارژ"]):
        await message.reply(random.choice(responses["percent"]))
    elif any(w in text for w in ["خرید", "سفارش", "بخوام", "میخوام", "ماینز", "انفجار", "crash", "vip", "طلایی", "نقره"]):
        if any(w in text for w in ["پرداخت", "رسید", "واریز"]):
            await message.reply(random.choice(responses["payment"]))
        else:
            await message.reply(random.choice(responses["order"]))
    elif any(w in text for w in ["سطح", "برنزی", "نقره", "طلایی"]):
        await message.reply(random.choice(responses["level"]))
    elif any(w in text for w in ["کمک", "سوال", "پشتیبانی", "مشکل", "نمیفهمم"]):
        await message.reply(random.choice(responses["support"]))
    elif any(w in text for w in ["ممنون", "مرسی", "تشکر"]):
        await message.reply(random.choice(responses["thank"]))
    elif any(w in text for w in ["سود", "برنده", "درآمد"]):
        await message.reply(random.choice(responses["motivation"]))
    else:
        await message.reply(responses["offline"])

async def main():
    await app.start()
    print("✅ User Bot با موفقیت فعال شد! حالا از اکانت خودت جواب می‌ده")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())    ],
    "order": [
        "عالی! 🚀 بگو: ماینز یا انفجار؟ سطح و مدت زمان رو هم بگو",
        "ثبت شد. جزئیات سفارش رو بفرست تا فاکتور برات آماده کنم",
        "خیلی خوب! سطح (برنزی، نقره‌ای، طلایی، VIP) و مدت زمان رو بگو"
    ],
    "payment": [
        "ممنون! بعد از پرداخت اسکرین شات رسید رو بفرست. ربات رو فوری فعال می‌کنم",
        "پرداخت رو انجام بده. به محض تأیید، ربات اختصاصی آماده میشه",
        "رسید رو بفرست، ظرف چند دقیقه ربات رو برات راه میندازم 🔥"
    ],
    "thank": [
        "خواهش میکنم! همیشه در خدمتم ❤️",
        "ممنون از اعتمادت. هر لحظه آماده کمکم",
        "خوشحالیم که تونستیم راهنمایی کنیم"
    ],
    "level": [
        "VIP قوی‌ترین نسخه‌ست. دقت و عملکردش خیلی بالاست",
        "طلایی تعادل عالی بین قیمت و کیفیت داره",
        "برنزی برای شروع و تست عالیه"
    ],
    "support": [
        "هر سوالی داری بپرس. کامل راهنمایی می‌کنم",
        "پشتیبانی ۲۴ ساعته داریم.放心 باش",
        "هر مشکلی داشتی بگو سریع حلش می‌کنیم"
    ],
    "motivation": [
        "خیلی از مشتری‌ها با ربات ما روزانه سود خوب می‌کنن",
        "زمان جبران ضررها رسیده. شروع کنیم؟ 🔥",
        "با VIP نتایج خیلی بهتری می‌گیری"
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
    elif any(w in text for w in ["کمک", "سوال", "پشتیبانی", "مشکل", "نمیفهمم"]):
        await message.answer(random.choice(responses["support"]))
    elif any(w in text for w in ["ممنون", "مرسی", "تشکر"]):
        await message.answer(random.choice(responses["thank"]))
    elif any(w in text for w in ["سود", "برنده", "درآمد"]):
        await message.answer(random.choice(responses["motivation"]))
    else:
        await message.answer(responses["offline"])

async def main():
    logging.basicConfig(level=logging.INFO)
    print("ربات هوشمند فعال شد!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
