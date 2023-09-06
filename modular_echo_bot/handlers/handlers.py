from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from lexicon.lexicon import LEXICON_RU 

router: Router = Router()

keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]]

keyboard.append([KeyboardButton(text='7')])

my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

#Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=my_keyboard)
