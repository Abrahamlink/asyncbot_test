from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Home', callback_data='page_home')],

    [InlineKeyboardButton(text='catalog', callback_data='page_catalog'),
     InlineKeyboardButton(text='Contacts', callback_data='page_contacts')]
])

settings_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Expense', callback_data='op_expense'), InlineKeyboardButton(text='Income', callback_data='op_income')]
])

# Keyboards created with builder
cars = ['ChepbIrka', 'Niva', 'GAZel']

async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car.lower()}'))
    return keyboard.adjust(2).as_markup()