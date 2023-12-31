import random
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter

BOT_TOKEN: str = '' 

admin_ids: list[int] = 

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 5

users: dict = {}

def get_random_number() -> int:
    return random.randint(1, 100)

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='You are greate admin!')

@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):

    if message.from_user.id not in users:
        await message.reply('You havent played yet')
    else:
        await message.answer(f'Total games: {users[message.from_user.id]["total_games"]}\n'
                             f'games won: {users[message.from_user.id]["wins"]}')	
        
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Rules of the game\n\n I guess the number from 1 to 100,'
                         f'And you have to guess\nYou have {ATTEMPTS}'
   	                     f'attemps\n\nAvailable commands:\n/help - game '
                         f'rooles and command list\n/cancel - exit the game\n'
                         f'/stat - see statistics\n\nLets play?')

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    print(message.from_user.id)
    await message.answer('Hello!\nLets play game "Guess a number"?\n\n'
                         'To get the rules of the game and the list of available'
                         'commands - send command /help')
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}


@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
	
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}
    else:
        if users[message.from_user.id]['in_game']:
            await message.answer('You are out of the game. If you want to play'
                                 'again - write about it')
            users[message.from_user.id]['in_game'] = False
        else:
            await message.answer('But we dont play with you.'
                                 'Maybe well play a game?')

@dp.message(F.text.lower().in_(['yes','lets play','game']))
async def process_positive_answer(message: Message):
    
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}

    if not users[message.from_user.id]['in_game']:
        await message.answer('Hooray!\n\nI guessed a number from 1 to 100,'
                             'try to guess!')
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = ATTEMPTS
    else:
        await message.answer('As long as we play the game I can'
                             'react only on numbers from 1 to 100'
                             'and the commands /cancel and /stat')

@dp.message(F.text.lower().in_(['no','dont won']))
async def process_negative_answer(message: Message):
	
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}

    if not users[message.from_user.id]['in_game']:
        await message.answer('Too bad:(\n\nIf you want to play,'
                             'just write about it')
    else:
        await message.answer('We are playing with you right now.'
                             'Send please numbers from 1 to 100')

@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            await message.answer('Hooray!!!You guessed the number!\n\n'
                                 'Can we play some more?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            await message.answer('My number is less')
            users[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            await message.answer('My number is greater')
            users[message.from_user.id]['attempts'] -= 1
        if users[message.from_user.id]['attempts'] == 0:
            await message.answer(f'Unfortunately you have no more'
       	                         f'tries. You lost\n\nMy number is'
                                 f'was {users[message.from_user.id]["secret_number"]}\n\n'
                                 f'Lets will we play again?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
    else:
        await message.answer('We are not playing yet. You want to play?')

@dp.message()
async def process_other_text_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('We are playing with you now\n'
                             'Please send numbers from 1 to 100')
    else:
        await message.answer('I am a pretty limited bot, come on\n'
                             'just play a game?')

if __name__ == '__main__':
    dp.run_polling(bot)
