# from telegram.ext import Updater, CommandHandler

# # Функция для команды /start
# def start(update, context):
#     update.message.reply_text('Привет! Я твой первый бот!')

# # Основная функция
# def main():
#     # Вставьте сюда ваш токен
#     TOKEN = "7533579309:AAFbLsuBCurZJ1JSR9heP1HJscR-ZkMQxHU"

#     # Настройка бота
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     # Добавляем команду /start
#     dp.add_handler(CommandHandler('start', start))

#     # Запуск бота
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()

import requests
from telegram import Update
from telegram.ext import Application, CommandHandler

# Ваш API-ключ от OpenWeatherMap
API_KEY = "ваш_API_ключ"

# Функция для получения погоды
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Yakutsk&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"Погода в Якутске: {weather}, температура: {temperature}°C"
    else:
        return "Не удалось получить данные о погоде."

# Функция для команды /start
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я бот, который поможет узнать погоду в Якутске. Используйте команду /weather для получения информации о текущей погоде.")

# Функция для команды /weather
async def weather(update: Update, context):
    weather_info = get_weather()
    await update.message.reply_text(weather_info)

# Основная функция
def main():
    TOKEN = "7533579309:AAFbLsuBCurZJ1JSR9heP1HJscR-ZkMQxHU"

    # Настройка приложения
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('weather', weather))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
