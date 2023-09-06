from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import  KeyboardButton, KeyboardButtonPollType, Message
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU  
from aiogram import Router, F

router: Router = Router()
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons_1: list[KeyboardButton] = [KeyboardButton(
                text=f'Кнопка {i + 1}') for i in range(6)]

buttons_2: KeyboardButton = KeyboardButton(text='Огурцов')
buttons_3: KeyboardButton = KeyboardButton(text='Собак')
contact_btn: KeyboardButton = KeyboardButton(
        text='Отправить телефон',
        request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(
        text='Отправить геолокацию',
        request_location=True)
poll_btn: KeyboardButton = KeyboardButton(
        text='Создать опрос',
        request_poll=KeyboardButtonPollType(
            type='regular'))

quiz_btn: KeyboardButton = KeyboardButton(
        text='Создать викторину',
        request_poll=KeyboardButtonPollType(
            type='quiz'))

web_app_btn: KeyboardButton = KeyboardButton(
        text='Start Web App',
        web_app=WebAppInfo(url="https://stepik.org/"))

kb_builder.row(*buttons_1, width=3)

kb_builder.row(buttons_2, buttons_3, width=3)

kb_builder.row(contact_btn, geo_btn, poll_btn, quiz_btn, web_app_btn, width=5)

#Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='bubuubububu'))

#Этот хэндлер срабатывает ан команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

#Этот хэндлер будет срабатывать на ответ "Собак" и удалять клавиатуру
@router.message(F.text == 'Собак')
async def process_dog_answer(message: Message):
    await message.answer(text=LEXICON_RU['Собак'])

#Этот хэндлер будет срабатывать на ответ "Огурцов" и удалять клавиатуру
@router.message(F.text == 'Огурцов')
async def process_cucumber_answer(message: Message):
    await message.answer(text=LEXICON_RU['Огурцов'])

