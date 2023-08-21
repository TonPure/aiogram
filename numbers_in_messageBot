from config import load_config
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import BaseFilter 
from environs import Env

config = load_config('.env')

bot: Bot = Bot(config.tg_bot.token)
dp: Dispatcher = Dispatcher()


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = {}
        words: [] = message.text.split()
        for word in words:
            print(word)
            if word.isdigit():
                if int(word) in numbers:
                    numbers[int(word)]+=1
                else:
                    numbers[int(word)]=1
        if numbers:
            return {'numbers': numbers}
        return False

@dp.message(NumbersInMessage())
async def process_if_not_numbers(message: Message, numbers: list[int]):
    await message.answer( text = 'Вот что-то')
    print(message.from_user.id)

if __name__ == '__main__':
    dp.run_polling(bot)
