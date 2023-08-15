import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
import sqlite3 as sq

async def db_start():
    global db, cur
    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, balance FLOAT, buy FLOAT)')
    db.commit()

async def on_startup(_):
    await db_start()

async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute(("INSERT INTO profile VALUES(?, ?, ?"), (user_id, "0.0", "0.0"))
        db.commit()


token = "6610342706:AAE_yh89hFgo4Y2izb6S-mkreNubhG51V0k"
TEXT_HELP = 'придумать текст!'
#async def main() -> None:

bot = Bot(token)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup(row_width=2)
bt1 = InlineKeyboardButton(text='Ворошиловский',
                           callback_data='vorosh')
bt2 = InlineKeyboardButton(text='Первомай',
                           callback_data='perv')
keyboard.add(bt1, bt2)

keyboard2 = InlineKeyboardMarkup(row_width=2)
twobt1 = InlineKeyboardButton(text='да',
                           callback_data='1da')
twobt2 = InlineKeyboardButton(text='нет',
                           callback_data='1net')
keyboard2.add(twobt1, twobt2)

keyboard3 = InlineKeyboardMarkup(row_width=2)
trebt1 = InlineKeyboardButton(text='да',
                           callback_data='2da')
trebt2 = InlineKeyboardButton(text='нет',
                           callback_data='2net')
keyboard3.add(trebt1, trebt2)

#@dp.message_handler()
#async def echo(message: types.Message):
#    if message.text != '/help':
#        await message.answer(text = 'poshel naxuy')
#    else:
#        await message.answer(text=TEXT_HELP)

@dp.message_handler(commands=['start'])
async def inline(message: types.Message):
    await message.answer(text='Выберите район',
                        reply_markup=keyboard)
    await create_profile(user_id=message.from_user.id)

@dp.callback_query_handler(text = 'vorosh')
async def otvet(x: types.CallbackQuery):
    await x.message.answer(text='Выберите район', reply_markup=keyboard2)


@dp.callback_query_handler(text='perv')
async def otvet2(xx: types.CallbackQuery):
   await xx.message.answer(text='Выберите район', reply_markup=keyboard3)




#@dp.message_handler(commands=['help'])
#async def echo(message: types.Message):
#    await message.answer(text = TEXT_HELP)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)


#def avarege():
#
#def inner(number):

#    numbers.append(number)
#    return sum(numbers)
#inner(5)
#inner(10)
#print(inner(5))



#def hadler(func):
#    aa = func
#    aa()
#    print("lolololo1")
#@hadler
#def q():
#    print("someth")








