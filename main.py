import telebot
from telebot import types
from background import keep_alive

token = '6577586367:AAG-6ZIXWiSaPLBEMgb8Ve2ZPSDSucnwQdU'
bot = telebot.TeleBot(token)
item1 = types.KeyboardButton("Видеоролик")
item2 = types.KeyboardButton("Записаться На Медиацию")
video = open('Medetation.mp4', 'rb')
Admin = ["6176370055"]


@bot.message_handler(commands=['start'])
def start_message(message):
  hello = open('AnimatedSticker.tgs', 'rb')
  bot.send_sticker(message.chat.id, hello)
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  markup.add(item1, item2)
  bot.send_message(message.chat.id,
                   'Выберите действие\n⬇️',
                   reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
  reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           one_time_keyboard=False)
  if message.text == "Записаться На Медиацию":
    ok = open('AnimatedStickerOk.tgs', 'rb')
    bot.send_sticker(message.chat.id, ok)
    bot.send_message(message.chat.id, "ваша заявка принята")
    reply_markup = reply_markup.row(item1)
    if message.chat.type == "group" or message.chat.type == "supergroup":
      for i in Admin:
        bot.send_message(i,
                         "участник группы" + "(" + message.chat.title + ")" +
                         " " + "@" + message.from_user.username + " " +
                         "хочет записаться на медиацию",
                         reply_markup=reply_markup)
    else:
      for i in Admin:
        bot.send_message(i,
                         "@" + message.from_user.username + " " +
                         "хочет записаться на медиацию",
                         reply_markup=reply_markup)

  elif message.text == "Видеоролик":
    reply_markup = reply_markup.row(item2)
    bot.send_message(message.chat.id,
                     "одну секунду...",
                     reply_markup=reply_markup)
    video = open('Medetation.mp4', 'rb')
    bot.send_video(message.chat.id, video)

  bot.send_message(message.chat.id, "что-то еще?", reply_markup=reply_markup)


keep_alive()
bot.infinity_polling()
