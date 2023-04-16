# Импорт всего необходимого
from aiogram import Router, types
from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Text, Command
from config.config import user_move, bot_move, likes_count, state
import random


# Объявление переменных и присвоение им значений
router = Router()
kb_builder = ReplyKeyboardBuilder()

sc: str = '✂'
rock: str = '🗿'
paper: str = '🧻'
button_scissors = (KeyboardButton(text=sc))
button_rock = (KeyboardButton(text=rock))
button_paper = (KeyboardButton(text=paper))

kb_builder.row(button_scissors, button_paper, button_rock)


# Генерация хода бота
def pick_random() -> str:
    return random.choice([sc, rock, paper])


# Запускает игру
@router.message(Command(commands='play'))
async def play(msg: types.Message):
    await msg.answer(text='Game started! Make your move.', reply_markup=kb_builder.as_markup(resize_keyboard=True))
    if msg.from_user.id not in likes_count:
        likes_count[msg.from_user.id] = 0
    state['attempts_total'] = 0
    bot_move[1] = pick_random()
    print(bot_move)


# Реагирует на ход игрока "ножницы"
@router.message(Text(text=sc))
async def scissors(msg: types.Message):
    state['attempts_total'] += 1
    await msg.reply('So let it be!')
    likes_count[msg.from_user.id] += 1
    if msg.from_user.id not in user_move:
        user_move[msg.from_user.id] = {}
    user_move[msg.from_user.id][likes_count[msg.from_user.id]] = sc
    if state['attempts_total'] == 3:
        await msg.reply('Game is finished! Try again!', reply_markup=ReplyKeyboardRemove())
    print(user_move)


# Реагирует на ход игрока "камень".
@router.message(Text(text=rock))
async def scissors(msg: types.Message):
    state['attempts_total'] += 1
    await msg.reply('So let it be!')
    likes_count[msg.from_user.id] += 1
    if msg.from_user.id not in user_move:
        user_move[msg.from_user.id] = {}
    user_move[msg.from_user.id][likes_count[msg.from_user.id]] = rock
    if state['attempts_total'] == 3:
        await msg.reply('Game is finished! Try again!', reply_markup=ReplyKeyboardRemove())
    print(user_move)


# Реагирует на ход игрока "бумага"
@router.message(Text(text=paper))
async def scissors(msg: types.Message):
    state['attempts_total'] += 1
    await msg.reply('So let it be!')
    likes_count[msg.from_user.id] += 1
    if msg.from_user.id not in user_move:
        user_move[msg.from_user.id] = {}
    user_move[msg.from_user.id][likes_count[msg.from_user.id]] = paper
    if state['attempts_total'] == 3:
        await msg.reply('Game is finished! Try again!', reply_markup=ReplyKeyboardRemove())
    print(user_move)

