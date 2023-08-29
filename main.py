import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
import sqlite3 as sq
#from text2 import first_text
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests




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
        cur.execute("INSERT INTO profile VALUES({0}, {1}, {2})".format(user_id, "0.0", "0.0"))
        db.commit()


token = "6517098042:AAGCl0HumXcfDjj49FUsIEp-qoOm2tTS9bE"
TEXT_HELP = 'придумать текст!'
#async def main() -> None:

storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(bot=bot, storage=storage)

class FSMToken(StatesGroup):
    forma = State()



first_panel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
vitrina = KeyboardButton(text = 'vit')
Balance = KeyboardButton(text = "Баланс/Пополнить")
Ticket = KeyboardButton(text = "Тикеты")
History = KeyboardButton(text= 'История покупок/Рефералка')
first_panel.add(vitrina, Balance).add(Ticket, History)

balanc = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btc = KeyboardButton(text = 'Пополнить через BTC')
card = KeyboardButton(text = "Пополнить через перевод на карту")
back = KeyboardButton(text = "Назад")
balanc.add(btc, card).add(back)




keyboard = InlineKeyboardMarkup(row_width=2)
bt1 = InlineKeyboardButton(text='Ворошиловский',
                           callback_data='vorosh')
bt2 = InlineKeyboardButton(text='Первомай',
                           callback_data='perv')
keyboard.add(bt1, bt2)

keyboard2 = InlineKeyboardMarkup(row_width=2)
twobt1 = InlineKeyboardButton(text='ДА',
                           callback_data='1da')
twobt2 = InlineKeyboardButton(text='НЕТ',
                           callback_data='1net')
twobt3 = InlineKeyboardButton(text='Назад',
                           callback_data='Nazad')
keyboard2.add(twobt1, twobt2).add(twobt3)

keyboard3 = InlineKeyboardMarkup(row_width=2)
trebt1 = InlineKeyboardButton(text='ДА',
                           callback_data='2da')
trebt2 = InlineKeyboardButton(text='НЕТ',
                           callback_data='2net')
keyboard3.add(trebt1, trebt2).add(twobt3)

otmena = ReplyKeyboardMarkup(resize_keyboard=True)
otmena_bt = KeyboardButton(text = 'Отмена')
otmena.add(otmena_bt)





@dp.message_handler(commands=['start'])
async def inline(message: types.Message):
    await create_profile(user_id=message.from_user.id)
    qwe = str(message.from_user.username)
    qwe2 = f"Привет, {qwe}"
    await message.answer(text=qwe2,
                        reply_markup=first_panel)


@dp.message_handler(Text(equals='Назад'))
async def inline(message: types.Message):
    qwe = str(message.from_user.username)
    qwe2 = f"Привет, {qwe}"
    await message.answer(text=qwe2,
                        reply_markup=first_panel)








@dp.message_handler(Text(equals='vit'))
async def vitrina_q(message: types.Message):
    await message.answer(text='Выберите район', reply_markup=keyboard)
    await bot.delete_message(message.chat.id, message.message_id)

@dp.callback_query_handler(text = 'Nazad')
async def vitrina_q(xx: types.CallbackQuery):
    await xx.message.answer(text='Выберите район', reply_markup=keyboard)


@dp.message_handler(Text(equals='Баланс/Пополнить'))
async def balance(message: types.Message):
    await message.answer(text='Ваш баланс 0 рублей.', reply_markup=balanc)


@dp.callback_query_handler(text = 'vorosh')
async def otvet(x: types.CallbackQuery):
    await x.message.answer(text='Выберите район', reply_markup=keyboard2)


@dp.callback_query_handler(text='perv')
async def otvet2(xx: types.CallbackQuery):
   await xx.message.answer(text='Выберите район', reply_markup=keyboard3)




@dp.message_handler(Text(equals='Тикеты'), state = None)
async def ticket(message: types.Message):
    await FSMToken.forma.set()
    await message.answer('Введите код покупки:')


@dp.message_handler(Text(equals='Отмена'), state=FSMToken.forma)
async def otmena2(message: types.Message, state: FSMContext):
    qwe = str(message.from_user.username)
    qwe2 = f"Привет, {qwe}"
    await message.answer(text=qwe2,
                        reply_markup=first_panel)
    await state.reset_state(with_data=False)


@dp.message_handler(state=FSMToken.forma)
async def load_token(message: types.Message):
    await message.answer('Такого кода не существует',reply_markup=otmena)


def scrape():
    response = requests.get(URL)
    response_json = response.json()
    return float(response_json["RUB"]["last"])

URL = 'https://blockchain.info/ru/ticker'
last_price = None

while True:
    latest_price = scrape()
    if latest_price != last_price:
        #print("Последняя цена BTC: ", latest_price)
        last_price = latest_price









if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)










