from aiogram import Router, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import BaseFilter, Text, Command
from config.config import user_move, bot_move, likes_count
import random


router = Router()
kb_builder = ReplyKeyboardBuilder()

sc: str = '✂'
rock: str = '🗿'
paper: str = '🧻'
button_scissors = (KeyboardButton(text=sc))
button_rock = (KeyboardButton(text=rock))
button_paper = (KeyboardButton(text=paper))

kb_builder.row(button_scissors, button_paper, button_rock)


def pick_random() -> str:
    return random.choice([sc, rock, paper])


@router.message(Command(commands='play'))
async def play(msg: types.Message):
    await msg.answer(text='Game started! Make your move.', reply_markup=kb_builder.as_markup(resize_keyboard=True,
                                                                              one_time_keyboard=True))
    if msg.from_user.id not in likes_count:
        likes_count[msg.from_user.id] = 0
    bot_move[1] = pick_random()
    print(bot_move)


@router.message(Text(text=sc))
async def scissors(msg: types.Message):
    await msg.reply('So let it be!', reply_markup=ReplyKeyboardRemove())
    likes_count[msg.from_user.id] += 1
    if msg.from_user.id not in user_move:
        user_move[msg.from_user.id] = {}
    user_move[msg.from_user.id][likes_count[msg.from_user.id]] = sc
    print(user_move)


@router.message(Text(text=rock))
async def scissors(msg: types.Message):
    await msg.reply('So let it be!', reply_markup=ReplyKeyboardRemove())
    likes_count[msg.from_user.id] += 1
    if msg.from_user.id not in user_move:
        user_move[msg.from_user.id] = {}
    user_move[msg.from_user.id][likes_count[msg.from_user.id]] = rock
    print(user_move)


@router.message(Text(text=paper))
async def scissors(msg: types.Message):
    await msg.reply('So let it be!', reply_markup=ReplyKeyboardRemove())
    likes_count[msg.from_user.id] += 1
    if msg.from_user.id not in user_move:
        user_move[msg.from_user.id] = {}
    user_move[msg.from_user.id][likes_count[msg.from_user.id]] = paper
    print(user_move)

