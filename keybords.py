from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import pandas as pd
import sqlite3 as sq


db = sq.connect('new.db')
cur = db.cursor()

keyboard = [
    [KeyboardButton(text = 'Full Info'),
    KeyboardButton(text = 'Корзина')],
    [KeyboardButton(text = 'Баланс/Пополнить'),
    KeyboardButton(text = 'History')]
]
first_panel = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,one_time_keyboard=True)

keyboard2 = [
    [KeyboardButton(text = 'BTC'),
    KeyboardButton(text = 'USDT')],
    [KeyboardButton(text = 'Back')]]
balanc = ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True,one_time_keyboard=True)


async def parser_state():
    a = open('full.txt')
    f = a.read()
    d = f.split("\n")
    df = pd.DataFrame(d)
    df.to_sql("fullinfo_us", db, if_exists="append", index=False)
#    vvv = df[df.str.contains(f""" {state} """)]
#    return vvv

async def forinlinebuttonstate():
    list_state = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    builder = InlineKeyboardBuilder()
    for i in list_state:
        fifty_one = await parser_state(i)
        print(fifty_one)
        if fifty_one.empty == False:

            builder.button(text=f'{i}', callback_data=f'{i}1')
        else:
            continue
    return builder

keyboard2 = [
    [InlineKeyboardButton(text = 'BACK', callback_data= 'BACK1'),
     InlineKeyboardButton(text = 'IN STOCK', callback_data= 'INSTOCK1')]
]
builder_for_basket = InlineKeyboardBuilder()
markup = InlineKeyboardMarkup(inline_keyboard = keyboard2)
builder_for_basket.attach(InlineKeyboardBuilder.from_markup(markup))
