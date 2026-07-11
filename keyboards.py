from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ تشخیص ضریب", callback_data="detect_mines")]
    ])

def next_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ تشخیص ضریب دست بعدی", callback_data="detect_mines")]
    ])