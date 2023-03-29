import telebot 
token = '6143992001:AAFQf8icyHT6XlgUn4qY9HvAH2sRy0G4vc8'
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start_message(message):
  bot.send_message(message.chat.id, 'ЫЫЫЫЫ!!!! Здарова!!\nКороче, /button -- Чо те надо, /stop -- Стоп.\nНадеюсь, понятно объяснил')
@bot.message_handler(commands = ['button'])
def next_message(message):
  markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = telebot.types.KeyboardButton('Ютубчик')
  item2 = telebot.types.KeyboardButton('И-НЕТ')
  markup.add(item1, item2)
  bot.send_message(message.chat.id, 'Чо надо? Говори!', reply_markup = markup)
@bot.message_handler(commands = ['stop'])
def stop_message(message):
  bot.send_message(message.chat.id, 'Будь здоров, дорогой!')
@bot.message_handler(content_types = 'text')
def message_reply(message):
  if message.text == 'Ютубчик':
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item3 = telebot.types.KeyboardButton('Спортишка')
    item4 = telebot.types.KeyboardButton('Музон')
    item5 = telebot.types.KeyboardButton('Назад')
    markup.add(item3, item4, item5)
    bot.send_message(message.chat.id,'Ок, чо смотреть хочешь?', reply_markup = markup)
  if message.text == 'Спортишка':
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item6 = telebot.types.KeyboardButton('Дзюдо')
    item7 = telebot.types.KeyboardButton('Футбол')
    item8 = telebot.types.KeyboardButton('Назаaд')
    markup.add(item6, item7, item8)
    bot.send_message(message.chat.id,'Ок, выбирай спорт', reply_markup = markup) 
  if message.text == 'Дзюдо':
    bot.send_message(message.from_user.id, '[Дзюдо](https://www.youtube.com/channel/UCEgdi0XIXXZ-qJOFPf4JSKw)', parse_mode='Markdown') 
  if message.text == 'Назаaд':
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item3 = telebot.types.KeyboardButton('Спортишка')
    item4 = telebot.types.KeyboardButton('Музон')
    item5 = telebot.types.KeyboardButton('Назад')
    markup.add(item3, item4, item5)
    bot.send_message(message.chat.id,'Ок, чо смотреть хочешь?', reply_markup = markup) 
  if message.text == 'Назад':
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = telebot.types.KeyboardButton('Ютубчик')
    item2 = telebot.types.KeyboardButton('И-НЕТ')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Чо надо? Говори!', reply_markup = markup)
  if message.text == 'И-НЕТ':
     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
     item9 = telebot.types.KeyboardButton('Фильмы')
     item10 = telebot.types.KeyboardButton('Сайт игры')
     item11 = telebot.types.KeyboardButton('Назад')
     markup.add(item9, item10, item11) 
     bot.send_message(message.chat.id, 'Ок, чо хочешь?', reply_markup = markup)
bot.infinity_polling()