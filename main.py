import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import F, types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command

bot = Bot(token='8002930832:AAEVm8oyibKYnwwcu9RTccUB-8J-nMKmdjY')
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="да", callback_data='yes')],
    [InlineKeyboardButton(text="нет", callback_data='no')],
])

@dp.message(CommandStart())
async def handle_start(msg: types.Message):
    await msg.answer(text='Привет,  Я тестовый бот')

@dp.message()
async def handle_msg(msg: types.Message):
    text = msg.text
    if text.lower() in ['стикер', 'sticker']:
        await msg.answer('Отправить стикер?', reply_markup=keyboard)
    else:
        await msg.answer(text=msg.text)

@dp.callback_query(F.data == 'yes')
async def handle_data_yes(callback: CallbackQuery):
    await callback.message.answer_sticker(r'CAACAgIAAxkBAAEJGidnCOJiaFk6NT3pZoILOMHxyjxIbQACnkAAAqjo8EglPHFxzfya7zYE')
@dp.callback_query(F.data == 'no')
async def handle_data_yes(callback: CallbackQuery):
    await callback.message.answer(text='ok')

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot, allowed_updates=['message, edited_message'])

if __name__ == '__main__':
    asyncio.run(main())