from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType

API_TOKEN: str = '5937214811:AAFEvE7hKAUwTCuVMJSBt1YMiEm_DY7HxVg'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

#@dp.message(F.voice)
#async def send_voice_echo(message:Message):
#    await message.reply_voice(message.voice.file_id)

#@dp.message(F.audio)
#async def send_audio_echo(message:Message):
#    await message.reply_audio(message.audio.file_id)

#@dp.message(F.video)
#async def send_video_echo(message:Message):
#    await message.reply_video(message.video.file_id)

#@dp.message(F.animation)
#async def send_animation_echo(message:Message):
#    await message.reply_animation(message.animation.file_id)

@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)

#@dp.message(F.photo)
#async def send_photo_echo(message: Message):
#    await message.reply_photo(message.photo[0].file_id)

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nПиши')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Пиши')

@dp.message()
async def send_echo(message: Message):
    try:
        print(message.model_dump_json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='This type not allow send_copy metod--------++++++++++++++++++++++++++++++--------------------')


if __name__=='__main__':
    dp.run_polling(bot)
