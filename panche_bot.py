import asyncio
from msilib.schema import File
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = "5116576559:AAGTRGGrmIMZJ8ESuQdfobiEXPERsx4Ngek"
bot = Bot(token=BOT_TOKEN)

button_prova = InlineKeyboardButton("text",url='https://vk.com/feed')
start_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(button_prova)

async def start_handler(event: types.Message):
  
    await event.answer(f"Profilo:\n {event.from_user.get_mention(as_html=True)}", parse_mode=types.ParseMode.HTML)
    await event.answer(f"Informazioni:\n {event.from_user.get_mention()}")
    await event.answer(f"Username: {event.from_user.username}", parse_mode=types.ParseMode.HTML)
    await event.answer(f"Lingua:  {event.from_user.language_code}", parse_mode=types.ParseMode.HTML)
    await event.answer(f"Sei un bot?  {event.from_user.is_bot}", parse_mode=types.ParseMode.HTML, reply_markup=start_keyboard)
    #metodo api telegram
    await bot.send_photo(chat_id= event.chat.id, photo=open("logo.png","rb"))
    
    await event.answer_photo("https://avatars.githubusercontent.com/u/104194632?v=4","Prova foto")

async def start_pippo(event: types.Message):
    await event.bot.answer_web_app_query()

async def main():

    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        disp.register_message_handler(start_pippo, commands={"pippo"})
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())
