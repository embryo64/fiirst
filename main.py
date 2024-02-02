import pandas as pd
import sqlite3 as sq
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from keybords import first_panel
import random
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
#from keybords import builder
from keybords import forinlinebuttonstate
from keybords import parser_state
from keybords import builder_for_basket
from keybords import balanc

token = "6517098042:AAGCl0HumXcfDjj49FUsIEp-qoOm2tTS9bE"
storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(storage=MemoryStorage())

class Сondition(StatesGroup):
    balance_first = State()
    Start = State()
    AL = State()
    AK = State()
    AZ = State()
    AR = State()
    CA = State()
    CO = State()
    CT = State()
    DC = State()
    DE = State()
    FL = State()
    GA = State()
    HI = State()
    ID = State()
    IL = State()
    IN = State()
    IA = State()
    KS = State()
    KY = State()
    LA = State()
    ME = State()
    MD = State()
    MA = State()
    MI = State()
    MN = State()
    MS = State()
    MO = State()
    MT = State()
    NE = State()
    NV = State()
    NH = State()
    NJ = State()
    NM = State()
    NY = State()
    NC = State()
    ND = State()
    OH = State()
    OK = State()
    OR = State()
    PA = State()
    RI = State()
    SC = State()
    SD = State()
    TN = State()
    TX = State()
    UT = State()
    VT = State()
    VA = State()
    WA = State()
    WV = State()
    WI = State()
    WY = State()

db = sq.connect('new.db')
cur = db.cursor()
async def db_start():
    db = sq.connect('new.db')
    cur = db.cursor()
    print(cur)
    cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, balance FLOAT, buy INT, referal INT statusbuy INT)')
    db.commit()

async def on_startup(_):
    await db_start()

def generate_random_string(length):
    letters = '1234567890'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return float(rand_string)

async def create_profile(user_id):
    db = sq.connect('new.db')
    cur = db.cursor()
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    #    print(user)
    if not user:
        cur.execute("INSERT INTO profile(user_id, balance, buy, referal, statusbuy) VALUES({0}, {1}, {2}, {3}, {4})".format(user_id, "0.0", "0.0", generate_random_string(8), "0"))
        cur.execute("INSERT INTO history_order_user(user_id) VALUES({0})".format(user_id))
        db.commit()




@dp.message(F.text == '/start')
async def inline(message: types.Message, state: FSMContext):
    await create_profile(user_id=message.from_user.id)
    await state.set_state(Сondition.Start)
    qwe = str(message.from_user.username)
    qwe2 = f"Привет, {qwe}\nТорчать хуево "
    await message.answer(text=qwe2,
                        reply_markup=first_panel)


@dp.message(F.text == '/xuy')
async def inline2(message: types.Message):
    await parser_state()
    await message.answer(text = 'успешно')


@dp.message(Сondition.Start, F.text == 'Full Info')
async def usualy_full(message: types.Message):
    rrr = await forinlinebuttonstate()
    rrrr = rrr.as_markup()
    await message.answer(text= "Some text here", reply_markup=rrrr)

#'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', \
#'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', \
#'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', \
#'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', \
#'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
@dp.callback_query(F.data == 'AL1')
async def al11(x: types.CallbackQuery, state: FSMContext):
    await state.set_state(Сondition.AL)
    sss = await parser_state('AL')
    ssss = sss.count()
    await x.message.edit_text(text = f'''В данном штате {ssss} FULL INFO''', )
    await x.message.edit_reply_markup(reply_markup=builder_for_basket.as_markup())

#@dp.callback_query(Сondition.AL, F.data == 'INSTOCK1')
#async def al12(x: types.CallbackQuery, state: FSMContext):


@dp.message(Сondition.Start, F.text == 'Баланс/Пополнить')
async def balance(message: types.Message, state: FSMContext):
    await state.set_state(Сondition.balance_first)
    zxc = cur.execute("SELECT balance FROM profile WHERE user_id = '{x}'".format(x=message.from_user.id)).fetchone()
    await message.answer(text=f'''Ваш баланс {zxc[0]} рублей.''', reply_markup=balanc)

@dp.message(Сondition.balance_first, F.text == 'Back')
async def balance_back(message: types.Message, state: FSMContext):
    await state.set_state(Сondition.Start)
    await message.answer(text = 'Select a tab', reply_markup=first_panel)

async def main():
    await dp.start_polling(bot, skip_updates=True, on_startup=on_startup)
#on_startup=on_startup

if __name__ == '__main__':
    asyncio.run(main())



