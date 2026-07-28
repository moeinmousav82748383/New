# ============================================================
# ربات پشتیبانی هوشمند آکادمی لونا
# نسخه: ۱.۱
# قابلیت‌ها: پاسخ خودکار + دکمه‌های اینلاین + ارسال به ادمین
# MADE BY @Moein481
# ============================================================

import asyncio
import logging
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from telethon.tl.types import User

# ============================================================
# بخش ۱: تنظیمات اصلی (حتماً این مقادیر را پر کنید)
# ============================================================

API_ID = 26183570                  # از my.telegram.org بگیرید
API_HASH = "77d151edb70ba4a170c25e8c814bc972"    # از my.telegram.org بگیرید
SESSION_NAME = "luna_support_session"

OWNER_ID = 8007177524               # آیدی عددی خودت (ادمین)

# ============================================================
# بخش ۲: پیام‌های ثابت سیستم
# ============================================================

WELCOME_MESSAGE = """سلام 🌟
به پشتیبانی آکادمی لونا خوش اومدی!

ما در حال جذب و آموزش **ادمین فروش** هستیم.
آموزش‌ها کاملاً رایگان و توسط خود آکادمی ارائه می‌شه.

از دکمه‌های زیر می‌تونی سوالات رایج رو بپرسی یا سوال خودت رو بنویسی:"""

OFFLINE_MESSAGE = """پیامتون دریافت شد ✅

در حال حاضر ادمین آفلاینه.
پیامتون به ادمین ارسال شد و به محض آنلاین شدن پاسخ کامل رو دریافت می‌کنید.

ممنون از صبوریتون 🙏"""

ADMIN_NOTIFY_TEMPLATE = """🔔 **پیام جدید از کاربر**

👤 نام: {name}
🆔 آیدی: `{user_id}`
🔗 یوزرنیم: @{username}

📝 متن پیام:
{text}

──────────────
برای پاسخ دادن مستقیم به کاربر کلیک کنید."""

# ============================================================
# بخش ۳: سیستم پاسخ‌دهی با کلیدواژه + دکمه‌های اینلاین
# ============================================================
# هر آیتم شامل:
#   keywords  → لیست کلمات کلیدی (اگر هر کدوم توی پیام باشه این پاسخ ارسال می‌شه)
#   reply     → متن پاسخ
#   button    → متن دکمه اینلاین (اختیاری - اگر بذاری دکمه ساخته می‌شه)

RESPONSES = [
    {
        "keywords": ["استخدام", "شرایط استخدام", "نیرو میخواید", "جذب نیرو", "شرایط کار"],
        "reply": """شرایط استخدام ادمین فروش در آکادمی لونا:

✅ علاقه به فروش و مذاکره
✅ گوشی هوشمند و اینترنت پایدار
✅ حداقل 13 سال سن
✅ وقت گذاشتن روزانه حداقل 1 ساعت

آموزش کامل توسط خود آکادمی داده می‌شه و نیازی به سابقه قبلی نیست.
اگر علاقه‌مندی، بگو تا راهنمای ثبت‌نام رو برات بفرستم.""",
        "button": "شرایط استخدام"
    },
    {
        "keywords": ["آموزش", "آموزشات", "کلاس", "یادگیری", "رایگان"],
        "reply": """آموزش‌های آکادمی لونا کاملاً **رایگان** هستن.

شامل:
• آموزش اصول فروش
• آموزش کار با پنل‌ها و ابزارها
• تمرین عملی با پشتیبانی مربی

بعد از ثبت‌نام، دسترسی به دوره برات فعال می‌شه.""",
        "button": "آموزش‌ها رایگانه؟"
    },
    {
        "keywords": ["حقوق", "درآمد", "کمیسیون", "پول", "چقدر درمیارم"],
        "reply": """سیستم درآمد در آکادمی لونا ترکیبی از حقوق پایه + کمیسیون فروش هست.

جزئیات دقیق بعد از مصاحبه و شروع همکاری اعلام می‌شه.
 به طور میانگین همکاران فعال درآمد خوبی دارن. تو میتونی توی چنل زیر لیست واریزی هارو مشاهده کنی :
 💬 کانال رضایت اعضا: 
https://t.me/ozviatacademy

""",
        "button": "حقوق و درآمد"
    },
    {
        "keywords": ["ثبت نام", "ثبت‌نام", "چطور ثبت نام کنم", "میخوام شروع کنم", "عضویت"],
        "reply": """برای ثبت ‌نام کافیه این اطلاعات رو بفرستی:

۱. نام و نام خانوادگی
۲. سن
۳. شهر محل سکونت
۴. شماره تماس

بعد از دریافت و بررسی اطلاعات ادمین بهت پیام میده.""",
        "button": "ثبت‌ نام / شروع همکاری"
    },
    {
        "keywords": ["دورکار", "حضوری", "از خونه", "لوکیشن"],
        "reply": """کار به صورت **کاملاً دورکار** هست.
نیازی به حضور فیزیکی نیست و از هر شهری می‌تونی همکاری کنی.""",
        "button": "دورکاره یا حضوری؟"
    },
    {
        "keywords": ["سابقه", "تجربه", "کار قبلی", "نیاز به سابقه"],
        "reply": """نیازی به سابقه قبلی نیست.
آکادمی از صفر آموزش می‌ده و همه چیز رو مرحله به مرحله یاد می‌گیری.""",
        "button": "نیاز به سابقه داره؟"
    },
    # ----- پاسخ مخصوص ارتباط با ادمین -----
    {
        "keywords": ["ادمین", "پشتیبانی", "انسان", "اپراتور", "مسئول", "با ادمین حرف بزنم"],
        "reply": """پیامتون به ادمین ارسال شد ✅

به محض آنلاین شدن، ادمین مستقیم بهتون پاسخ می‌ده.
لطفاً کمی صبور باشید.""",
        "button": "صحبت با ادمین"
    },
    # -----پاسخ اطلاعات بیشتر -----
        {
        "keywords": ["اعتماد", "اطمینان", "شرکت", "آکادمی", "مدرک", "اثبات"],
        "reply": """دوست دارم قبل از هر صحبتی، اول خودت با مجموعه آشنا بشی. 🌷
🌐 سایت مجموعه: 
https://zil.ink/academyluna
💬 کانال رضایت اعضا: 
https://t.me/ozviatacademy

✨ کانال آلفای درون: 
https://t.me/academyluna1
با خیال راحت همه رو ببین، بعد هر سوالی داشتی ازم بپرس، با حوصله جواب میدم.""",
        "button": "تماس با ما"
    },
]

# ============================================================
# بخش ۴: تنظیمات لاگ
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("luna_support.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================
# بخش ۵: کلاینت تلگرام
# ============================================================

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# ============================================================
# بخش ۶: توابع کمکی
# ============================================================

def find_response(text: str):
    """جستجوی کلیدواژه و برگرداندن پاسخ"""
    text_lower = text.lower().strip()
    for item in RESPONSES:
        for keyword in item["keywords"]:
            if keyword.lower() in text_lower:
                return item["reply"]
    return None


def build_faq_buttons():
    """ساخت دکمه‌های اینلاین از روی لیست RESPONSES"""
    buttons = []
    row = []
    for idx, item in enumerate(RESPONSES):
        if "button" in item and item["button"]:
            # data به صورت faq_0 ، faq_1 و ... ذخیره می‌شه
            btn = Button.inline(item["button"], data=f"faq_{idx}")
            row.append(btn)
            if len(row) == 2:  # هر ردیف ۲ دکمه
                buttons.append(row)
                row = []
    if row:
        buttons.append(row)
    return buttons


async def notify_admin(event, user_text: str):
    """ارسال نوتیفیکیشن به ادمین"""
    sender = await event.get_sender()
    name = sender.first_name or "بدون نام"
    if sender.last_name:
        name += f" {sender.last_name}"
    username = sender.username or "ندارد"

    text = ADMIN_NOTIFY_TEMPLATE.format(
        name=name,
        user_id=sender.id,
        username=username,
        text=user_text
    )

    try:
        await client.send_message(
            OWNER_ID,
            text,
            buttons=[[Button.url("چت با کاربر", f"tg://user?id={sender.id}")]]
        )
        logger.info(f"نوتیفیکیشن به ادمین ارسال شد | کاربر: {sender.id}")
    except Exception as e:
        logger.error(f"خطا در ارسال نوتیفیکیشن به ادمین: {e}")


async def send_welcome(event):
    """ارسال پیام خوش‌آمدگویی + دکمه‌های اینلاین"""
    buttons = build_faq_buttons()
    await event.reply(WELCOME_MESSAGE, buttons=buttons)


# ============================================================
# بخش ۷: هندلر اصلی پیام‌ها (پیوی + گروه با منشن/ریپلای)
# ============================================================

@client.on(events.NewMessage(incoming=True))
async def handle_message(event):
    sender = await event.get_sender()

    # ---------- فیلترهای مهم ----------
    # ۱. اگر فرستنده ربات باشد → نادیده بگیر
    if getattr(sender, 'bot', False):
        return

    # ۲. اگر فرستنده یا چت مورد نظر @lunaa_support باشد → نادیده بگیر
    if getattr(sender, 'username', None) and sender.username.lower() == "lunaa_support":
        return
    if event.chat and getattr(event.chat, 'username', None) and event.chat.username.lower() == "lunaa_support":
        return

    # ۳. اگر پیام از خودت باشد → نادیده بگیر
    if sender.id == OWNER_ID:
        return

    user_text = (event.raw_text or "").strip()
    if not user_text:
        return

    # ---------- تشخیص نوع چت ----------
    is_private = event.is_private
    is_group = event.is_group or event.is_channel

    should_reply = False

    if is_private:
        # در پیوی همیشه جواب بده (به جز فیلترهایی که بالاتر زدیم)
        should_reply = True

    elif is_group:
        # در گروه فقط اگر منشن شده باشی یا روی پیامت ریپلای زده باشند
        if event.mentioned:
            should_reply = True
        elif event.is_reply:
            try:
                replied_msg = await event.get_reply_message()
                if replied_msg and replied_msg.sender_id == OWNER_ID:
                    should_reply = True
            except:
                pass

    if not should_reply:
        return

    # ---------- از اینجا به بعد منطق پاسخ‌دهی قبلی ----------
    logger.info(f"پیام معتبر از {sender.id} ({getattr(sender, 'first_name', '')}): {user_text[:60]}...")

    # سلام یا استارت
    if user_text.lower() in ["سلام", "سلام علیکم", "درود", "/start", "استارت", "hi", "hello"]:
        await send_welcome(event)
        return

    # جستجوی پاسخ
    response = find_response(user_text)

    if response:
        await event.reply(response)
        # اگر مربوط به ادمین بود، نوتیفیکیشن هم بفرست
        if any(k in user_text.lower() for k in ["ادمین", "پشتیبانی", "انسان", "اپراتور"]):
            await notify_admin(event, user_text)
    else:
        # هیچ پاسخی پیدا نشد
        await event.reply(OFFLINE_MESSAGE)
        await notify_admin(event, user_text)

# ============================================================
# بخش ۸: هندلر دکمه‌های اینلاین (Callback)
# ============================================================

@client.on(events.CallbackQuery)
async def handle_callback(event):
    data = event.data.decode("utf-8")

    if data.startswith("faq_"):
        try:
            idx = int(data.split("_")[1])
            if 0 <= idx < len(RESPONSES):
                reply_text = RESPONSES[idx]["reply"]
                await event.answer()  # لودینگ دکمه رو برمی‌داره
                await event.reply(reply_text)

                # اگر دکمه «صحبت با ادمین» بود، نوتیفیکیشن هم بفرست
                if "ادمین" in RESPONSES[idx]["keywords"] or "پشتیبانی" in RESPONSES[idx]["keywords"]:
                    # برای callback باید اطلاعات کاربر رو جدا بگیریم
                    sender = await event.get_sender()
                    fake_event = type('obj', (object,), {
                        'get_sender': lambda: asyncio.coroutine(lambda: sender)(),
                        'raw_text': RESPONSES[idx]["button"]
                    })()
                    await notify_admin(event, f"[کلیک روی دکمه] {RESPONSES[idx]['button']}")
            else:
                await event.answer("این گزینه دیگر معتبر نیست.", alert=True)
        except Exception as e:
            logger.error(f"خطا در پردازش دکمه: {e}")
            await event.answer("خطایی رخ داد.", alert=True)


# ============================================================
# بخش ۹: شروع برنامه
# ============================================================

async def main():
    logger.info("در حال اتصال به تلگرام...")
    await client.start()

    me = await client.get_me()
    logger.info(f"وارد شدید: {me.first_name} | ID: {me.id}")
    logger.info("ربات پشتیبانی آکادمی لونا با موفقیت فعال شد.")

    await client.run_until_disconnected()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("ربات متوقف شد.")
    except Exception as e:
        logger.error(f"خطای کلی: {e}")
