from aiogram import Router, types
from aiogram.filters import Command
from config.config import state
from lexica.lexica import START, HELP


router: Router = Router()


# Реакция на команду старт
@router.message(Command(commands='start'))
async def start_bot(msg: types.Message):
    await msg.answer(START)
    state['in_game'] = True


# Реакция на комманду /help
@router.message(Command(commands='help'))
async def help_user(msg: types.Message):
    await msg.reply(HELP)


# Обработка неправильных сообщений.
@router.message()
async def errors(msg: types.Message):
    await msg.reply('Я ограниченный в возможностях бот, понимаю только команды.')


