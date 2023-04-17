# Импорт всего необходимого
from aiogram import Router, types
from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Text, Command
from config.config import state
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


# Запускает игру
@router.message(Command(commands='play'))
async def play(msg: types.Message):
    await msg.answer(text='Game started! Make your move.', reply_markup=kb_builder.as_markup(resize_keyboard=True))
    state['attempts_total'] = 0
    state['score_user'] = 0
    state['score_bot'] = 0


# Реагирует на ход игрока "ножницы"
@router.message(Text(text=sc))
async def scissors(msg: types.Message):
    state['attempts_total'] += 1
    bot_move = random.choice([sc, paper, rock])
    if bot_move == rock:
        await msg.reply('One point to me!')
        state['score_bot'] += 1
    elif bot_move == paper:
        await msg.reply('One point to you!')
        state['score_user'] += 1
    else:
        await msg.reply('Draw(')
    if state['attempts_total'] >= 3:
        if state['score_user'] > state['score_bot']:
            await msg.reply('You win!', reply_markup=ReplyKeyboardRemove())
        elif state['score_bot'] > state['score_user']:
            await msg.reply('You lost(', reply_markup=ReplyKeyboardRemove())
        else:
            await msg.reply('Draw(', reply_markup=ReplyKeyboardRemove())
    print(bot_move)
    print(state)


# Реагирует на ход игрока "камень".
@router.message(Text(text=rock))
async def scissors(msg: types.Message):
    bot_move = random.choice([sc, paper, rock])
    state['attempts_total'] += 1
    if bot_move == rock:
        await msg.reply('Draw(')
    elif bot_move == paper:
        await msg.reply('One point to me!')
        state['score_bot'] += 1
    else:
        await msg.reply('One point to you!')
        state['score_user'] += 1
    if state['attempts_total'] >= 3:
        if state['score_user'] > state['score_bot']:
            await msg.reply('You win!', reply_markup=ReplyKeyboardRemove())
        elif state['score_bot'] > state['score_user']:
            await msg.reply('You lost(', reply_markup=ReplyKeyboardRemove())
        else:
            await msg.reply('Draw(', reply_markup=ReplyKeyboardRemove())
    print(bot_move)
    print(state)


# Реагирует на ход игрока "бумага"
@router.message(Text(text=paper))
async def scissors(msg: types.Message):
    bot_move = random.choice([sc, paper, rock])
    state['attempts_total'] += 1
    if bot_move == rock:
        await msg.reply('One point to you!')
        state['score_user'] += 1
    elif bot_move == paper:
        await msg.reply('Draw(')
    else:
        await msg.reply('One point to me!')
        state['score_bot'] += 1
    if state['attempts_total'] >= 3:
        if state['score_user'] > state['score_bot']:
            await msg.reply('You win!', reply_markup=ReplyKeyboardRemove())
        elif state['score_bot'] > state['score_user']:
            await msg.reply('You lost(', reply_markup=ReplyKeyboardRemove())
        else:
            await msg.reply('Draw(', reply_markup=ReplyKeyboardRemove())
    print(bot_move)
    print(state)


