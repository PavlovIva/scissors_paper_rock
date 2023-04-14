from aiogram import Router, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import BaseFilter
from config.config import state

router = Router()
kb_builder = ReplyKeyboardBuilder()

button_scissors = (KeyboardButton(text='✂'))
button_rock = (KeyboardButton(text='🗿'))
button_paper = (KeyboardButton(text='🧻'))

kb_builder.row(button_scissors, button_paper, button_rock)


# Проверка состояние игры
class IsInGame(BaseFilter):
    def __init__(self, state) -> None:
        self.state = state

    async def __call__(self, statte) -> bool:
        if self.state['in_game']:
            return True


# Вызов кнопок
@router.message(IsInGame(state))
async def make_move(msg: types.Message):
    await msg.answer(text='Make your move', reply_markup=kb_builder.as_markup(resize_keyboard=True,
                                                                              one_time_keyboard=True))


