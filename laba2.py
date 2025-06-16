import asyncio
import random
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

TOKEN = "7574033900:AAG_bBi2CZuFKCnnabjh_CyIOHII5xlDkqU"  # @SAdasdzxc_bot

IMAGES = [
    "https://i.pinimg.com/736x/3f/c4/91/3fc491a0db36060192c3f614fc9ccf07.jpg",
    "https://i.pinimg.com/736x/12/06/87/120687a77dd6ed7b7626a9ee23941ca2.jpg",
    "https://i.pinimg.com/736x/27/ba/77/27ba77ca62bf612475371e9619d0f431.jpg",
    "https://i.pinimg.com/736x/c5/3f/63/c53f637fdc343c0e1ae85d93d1544f4d.jpg",
    "https://i.pinimg.com/736x/5d/55/67/5d55673187edb98ee11b4d183c1c5f9b.jpg"
]

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text="Мотивации", callback_data="go")]]
    )
    await message.answer("Нажми кнопку и получи мотивацию!", reply_markup=kb)

@dp.callback_query(F.data == "go")
async def motivate(callback: types.CallbackQuery):
    await callback.message.answer_photo(random.choice(IMAGES), caption="Вот твоя мотивация!")
    await callback.answer()

async def main():
    print("Бот запущен!")  # видно, что бот стартовал
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
