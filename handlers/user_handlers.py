from aiogram import Router, types
from aiogram.filters import Command, Text
from config.config import state

router: Router = Router()


# Реакция на команду старт
@router.message(Command(commands='start'))
async def start_bot(msg: types.Message):
    await msg.answer('Working on this crap')
    state['in_game'] = True



