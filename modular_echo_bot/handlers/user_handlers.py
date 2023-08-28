from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU  
from aiogram import Router, F

router: Router = Router()

button_1: KeyboardButton = KeyboardButton(text='Собак')
button_2: KeyboardButton = KeyboardButton(text='Огурцов')

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True)

#Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard, resize_keyboard=True)

#Этот хэндлер срабатывает ан команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard)

#Этот хэндлер будет срабатывать на ответ "Собак" и удалять клавиатуру
@router.message(F.text == 'Собак')
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. Но вы видели как они боятся огурцов?', reply_markup=ReplyKeyboardRemove())

#Этот хэндлер будет срабатывать на ответ "Огурцов" и удалять клавиатуру
@router.message(F.text == 'Огурцов')
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов кошки боятся больше', reply_markup=ReplyKeyboardRemove())

