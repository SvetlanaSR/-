import telebot
#import os
# import markups
# markup = markups.get_markup_for_file_name("main.py")
from telebot import types
TOKEN = ('5750906280:AAFBtTgOtuuYULJNKXHCrpIVGANspnShIJw')
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('О боте')
    item2 = types.KeyboardButton('Я хочу узнать свое расписание')
    help_item = telebot.types.KeyboardButton("/help")
    markup.add(item1, item2,help_item)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!Я LYCEYM_BOT,смогу помочь тебе быстро узнать твое "
                                          "расписание ".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Я хочу узнать свое расписание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('1 класс')
        item2 = types.KeyboardButton('2 класс')
        item3 = types.KeyboardButton('3 класс')
        item4 = types.KeyboardButton('4 класс')
        item5 = types.KeyboardButton('5 класс')
        item6 = types.KeyboardButton('6 класс')
        item7 = types.KeyboardButton('7 класс')
        item8 = types.KeyboardButton('8 класс')
        item9 = types.KeyboardButton('9 класс')
        item10 = types.KeyboardButton('10 класс')
        item11 = types.KeyboardButton('11 класс')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
        bot.send_message(message.chat.id, 'Укажите свой класс', reply_markup=markup)
    elif message.text == "О боте":
        bot.send_message(message.chat.id, text="Привет, Я lyceym бот! Смогу помочь тебе быстро узнать свое расписание♡ ")
    elif message.text == "/help":
        bot.send_message(message.chat.id, text="Eсли у вас возникли проблемы  обратитесь к https://t.me/YarmAlsu ")

    elif message.text == "1 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1a_btn = types.KeyboardButton("1А")
        item1b_btn = types.KeyboardButton("1Б")
        item1v_btn = types.KeyboardButton("1В")
        item1g_btn = types.KeyboardButton("1Г")
        start_btn = types.KeyboardButton("/start")
        markup.add(item1a_btn, item1b_btn, item1v_btn,item1g_btn,start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "2 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2a_btn = telebot.types.KeyboardButton("2А")
        item2b_btn = telebot.types.KeyboardButton("2Б")
        item2v_btn = telebot.types.KeyboardButton("2В")
        item2g_btn = telebot.types.KeyboardButton("2Г")
        item2d_btn = telebot.types.KeyboardButton("2Д")

        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item2a_btn, item2b_btn, item2v_btn,item2g_btn,item2d_btn, start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "3 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3a_btn = telebot.types.KeyboardButton("3А")
        item3b_btn = telebot.types.KeyboardButton("3Б")
        item3v_btn = telebot.types.KeyboardButton("3В")
        item3g_btn = telebot.types.KeyboardButton("3Г")
        item3d_btn = telebot.types.KeyboardButton("3Д")

        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item3a_btn, item3b_btn, item3v_btn,item3g_btn, item3d_btn,start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "4 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item4a_btn = telebot.types.KeyboardButton("4А")
        item4b_btn = telebot.types.KeyboardButton("4Б")
        item4v_btn = telebot.types.KeyboardButton("4В")
        item4g_btn = telebot.types.KeyboardButton("4Г")
        item4d_btn = telebot.types.KeyboardButton("4Д")

        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item4a_btn, item4b_btn, item4v_btn,item4g_btn, item4d_btn,start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "5 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5a_btn = telebot.types.KeyboardButton("5А")
        item5b_btn = telebot.types.KeyboardButton("5Б")
        item5v_btn = telebot.types.KeyboardButton("5В")
        item5g_btn = telebot.types.KeyboardButton("5Г")


        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item5a_btn, item5b_btn, item5v_btn, item5g_btn, start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "6 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6a_btn = telebot.types.KeyboardButton("6А")
        item6b_btn = telebot.types.KeyboardButton("6Б")
        item6v_btn = telebot.types.KeyboardButton("6В")
        item6g_btn = telebot.types.KeyboardButton("6Г")
        item6d_btn = telebot.types.KeyboardButton("6Д")

        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item6a_btn, item6b_btn, item6v_btn, item6g_btn, item6d_btn, start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "7 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item7a_btn = telebot.types.KeyboardButton("7А")
        item7b_btn = telebot.types.KeyboardButton("7Б")
        item7v_btn = telebot.types.KeyboardButton("7В")
        item7g_btn = telebot.types.KeyboardButton("7Г")


        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item7a_btn, item7b_btn, item7v_btn, item7g_btn, start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "8 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item8a_btn = telebot.types.KeyboardButton("8А")
        item8b_btn = telebot.types.KeyboardButton("8Б")
        item8v_btn = telebot.types.KeyboardButton("8В")
        item8g_btn = telebot.types.KeyboardButton("8Г")


        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item8a_btn, item8b_btn, item8v_btn, item8g_btn, start_btn)
        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "9 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item9a_btn = telebot.types.KeyboardButton("9А")
        item9b_btn = telebot.types.KeyboardButton("9Б")
        item9v_btn = telebot.types.KeyboardButton("9В")
        item9g_btn = telebot.types.KeyboardButton("9Г")


        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item9a_btn, item9b_btn, item9v_btn, item9g_btn, start_btn)

        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "10 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item10a_btn = telebot.types.KeyboardButton("10А")
        item10b_btn = telebot.types.KeyboardButton("10Б")


        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item10a_btn, item10b_btn, start_btn)

        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)

    elif message.text == "11 класс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item11a_btn = telebot.types.KeyboardButton("11А")
        item11b_btn = telebot.types.KeyboardButton("11Б")



        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(item11a_btn, item11b_btn,  start_btn)

        bot.send_message(message.chat.id, 'Выбери номер класса, и я тебе отправлю расписание! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)
    elif (message.text == "1А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_1А")
        btn1aV = types.KeyboardButton("ВТОРНИК_1А")
        btn1aS = types.KeyboardButton("СРЕДА_1А")
        btn1aCH = types.KeyboardButton("ЧЕТВЕРГ_1А")
        btn1aPT = types.KeyboardButton("ПЯТНИЦА_1А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1aP, btn1aV, btn1aS,btn1aCH,btn1aPT,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_1А"):
        bot.send_message(message.chat.id,"1️⃣8:30-9.10/разгов\n2️⃣9.20-10:00/литер.чтение\n3️⃣10.10-10.50/русс.яз\n")
    elif (message.text == "ВТОРНИК_1А"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/русс.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/физ-ра\n")
    elif (message.text == "СРЕДА_1А"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/русс.яз\n2️⃣ 9:20-10:00/литр.чтение\n3️⃣10:10-10:50/математика\n")
    elif (message.text == "ЧЕТВЕРГ_1А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/русс.яз\n2️⃣9:20-10:00/литер.чтение\n3️⃣10:10-10:50/математика\n")
    elif (message.text == "ПЯТНИЦА_1А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/русс.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/род.яз\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "1Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_1Б")
        btn1bV = types.KeyboardButton("ВТОРНИК_1Б")
        btn1bS = types.KeyboardButton("СРЕДА_1Б")
        btn1bCH= types.KeyboardButton("ЧЕТВЕРГ_1Б")
        btn1bPT = types.KeyboardButton("ПЯТНИЦА_1Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1bP, btn1bV, btn1bS,btn1bCH,btn1bPT,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_1Б"):
        bot.send_message(message.chat.id,"1️⃣8:30-9.10/разгов\n2️⃣9.20-10:00/литер.чтение\n3️⃣10.10-10.50/русс.яз\n")
    elif (message.text == "ВТОРНИК_1Б"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/математика\n2️⃣9:20-10:00/физ-ра\n3️⃣10:10-10:50/рус.яз\n")
    elif (message.text == "СРЕДА_1Б"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/математика\n2️⃣9:20-10:00/литр.чтение\n3️⃣10:10-10:50/русс.яз\n")
    elif (message.text == "ЧЕТВЕРГ_1Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика\n2️⃣9:20-10:00/литр.чтение\n3️⃣10:10-10:50/русс.яз\n")
    elif (message.text == "ПЯТНИЦА_1Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика\n2️⃣9:20-10:00/русский\n3️⃣10:10-10:50/род.яз\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "1В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_1В")
        btn1vV = types.KeyboardButton("ВТОРНИК_1В")
        btn1vS = types.KeyboardButton("СРЕДА_1В")
        btn1vCH= types.KeyboardButton("ЧЕТВЕРГ_1В")
        btn1vPT = types.KeyboardButton("ПЯТНИЦА_1В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1vP, btn1vV, btn1vS,btn1vCH,btn1vPT,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_1В"):
        bot.send_message(message.chat.id,"1️⃣8:30-9.10/разгов\n2️⃣9.20-10:00/литер.чтение\n3️⃣10.10-10.50/русс.яз\n")
    elif (message.text == "ВТОРНИК_1В"):
        bot.send_message(message.chat.id," 1️⃣8:30-9:10/математика\n2️⃣9:20-10:10литр.чтение\n3️⃣10:10-10:50/рус.яз\n")
    elif (message.text == "СРЕДА_1В"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/математика\n2️⃣9:20-10:10/рус.яз\n3️⃣10:10-10:50/физ-ра\n")
    elif (message.text == "ЧЕТВЕРГ_1В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика\n2️⃣9:20-10:10/литр.чтение\n3️⃣10:10-10:50/рус.яз\n")
    elif (message.text == "ПЯТНИЦА_1В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика\n2️⃣9:20-10:10/ рус.яз\n3️⃣10:10-10:50/родной язык\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "1Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_1Г")
        btn1gV = types.KeyboardButton("ВТОРНИК_Г")
        btn1gS = types.KeyboardButton("СРЕДА_Г")
        btn1gCH = types.KeyboardButton("ЧЕТВЕРГ_Г")
        btn1gPT = types.KeyboardButton("ПЯТНИЦА_Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1gP, btn1gV, btn1gS, btn1gCH, btn1gPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_Г"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/разгов\n2️⃣9:20-10:10/литер.чтение\n3️⃣10:10-10:50/рус.яз\n")
    elif (message.text == "ВТОРНИК_Г"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/математика\n2️⃣9:20-10:10/литр.чтение\n3️⃣10:10-10:50/рус.яз\n")
    elif (message.text == "СРЕДА_Г"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/литр.чтение\n2️⃣9:20-10:10/рус.яз\n3️⃣10:10-10:50/математика\n")
    elif (message.text == "ЧЕТВЕРГ_Г"):
        bot.send_message(message.chat.id," 1️⃣8:30-9:10/маленький\n2️⃣9:20-10:10/физра\n3️⃣10:10-10:50/рус.яз\n")
    elif (message.text == "ПЯТНИЦА_Г"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/математика\n2️⃣9:20-10:10/рус.яз\n3️⃣10:10-10:50/род.яз\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "2А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_2А")
        btn2aV = types.KeyboardButton("ВТОРНИК_2А")
        btn2aS = types.KeyboardButton("СРЕДА_2А")
        btn2aCH = types.KeyboardButton("ЧЕТВЕРГ_2А")
        btn2aPT = types.KeyboardButton("ПЯТНИЦА_2А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn2aP, btn2aV, btn2aS, btn2aCH, btn2aPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_2А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разг.о важном\n2️⃣14:25-15:05/рус.яз\n3️⃣15:15-15:55/математика\n4️⃣16:05-16:45/физра\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "ВТОРНИК_2А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/родной.язык\n2️⃣14:25-15:05/англ.яз\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/лчнря\n5️⃣16:55-17:35/физра в/д\n")
    elif (message.text == "СРЕДА_2А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/литер.чтение\n2️⃣14:25-15:05/математика\n 3️⃣15:15-15:55/рус.яз\n 4️⃣16:05-16:45/окруж.мир\n 5️⃣16:55-17:35/физра\n6⃣17:45-18:25/изо\n")
    elif (message.text == "ЧЕТВЕРГ_2А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n 2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/англ.яз\n4️⃣16:05-16:45/литер.чтение\n 5️⃣16:55-17:35/технология\n")
    elif (message.text == "ПЯТНИЦА_2А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n 2️⃣14:25-15:05/родной язык\n 3️⃣15:15-15:55/математика\n 4️⃣16:05-16:45/окруж.мир\n 5️⃣16:55-17:35/музыка\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "2Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_2Б")
        btn2bV = types.KeyboardButton("ВТОРНИК_2Б")
        btn2bS = types.KeyboardButton("СРЕДА_2Б")
        btn2bCH = types.KeyboardButton("ЧЕТВЕРГ_2Б")
        btn2bPT = types.KeyboardButton("ПЯТНИЦА_2Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn2bP, btn2bV, btn2bS, btn2bCH, btn2bPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_2Б"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разг.о важном\n 2️⃣14:25-15:05/рус.яз\n 3️⃣15:15-15:55/англ.яз\n4️⃣16:05-16:45/математика\n 5️⃣16:55-17:35/физра\n")
    elif (message.text == "ВТОРНИК_2Б"):
        bot.send_message(message.chat.id, " 1️⃣13:35:14:15/родной язык\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/физра в/д\n4️⃣16:05-16:45/лчнря\n5️⃣16:55-17:35/руз.яз\n6⃣17:45-18:25/музыка\n")
    elif (message.text == "СРЕДА_2Б"):
        bot.send_message(message.chat.id, " 1️⃣13:35:14:15/математика\n2️⃣14:25-15:05/рус.яз\n3️⃣15:15-15:55/окруж.мир\n4️⃣16:05-16:45/физра\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "ЧЕТВЕРГ_2Б"):
        bot.send_message(message.chat.id, " 1️⃣13:35:14:15/рус.яз\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/литер.чтение\n4️⃣16:05-16:45/окруж.мир\n5️⃣16:55-17:35/изо\n6⃣17:45-18:25/изо\n")
    elif (message.text == "ПЯТНИЦА_2Б"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n2️⃣14:25-15:05/родной язык\n3️⃣15:15-15:55/англ.яз\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/технология\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "2В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_2В")
        btn2vV = types.KeyboardButton("ВТОРНИК_2В")
        btn2vS = types.KeyboardButton("СРЕДА_2В")
        btn2vCH = types.KeyboardButton("ЧЕТВЕРГ_2В")
        btn2vPT = types.KeyboardButton("ПЯТНИЦА_2В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn2vP, btn2vV,btn2vS, btn2vCH, btn2vPT,  back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_2В"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разг.о важном\n2️⃣14:25-15:05/рус.яз\n3️⃣15:15-15:55/физра\n4️⃣16:05-16:45/математика\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "ВТОРНИК_2В"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/родной язык\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/англ.яз\n4️⃣16:05-16:45/лчнря\n5️⃣16:55-17:35/рус.яз\n")
    elif (message.text == "СРЕДА_2В"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/литер.чтение\n4️⃣16:05-16:45/окруж.мир\n5️⃣16:55-17:35/музыка\n")
    elif (message.text == "ЧЕТВЕРГ_2В"):
        bot.send_message(message.chat.id,"1️⃣13:35:14:15/математика\n2️⃣14:25-15:05/англ.яз\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/физра\n5️⃣16:55-17:35/литер.чтение\n6⃣17:45-18:25/изо\n")
    elif (message.text == "ПЯТНИЦА_2В"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n2️⃣14:25-15:05/родной язык\n3️⃣15:15-15:55/физра в/д\n4️⃣16:05-16:45/окруж.мир\n5️⃣16:55-17:35/технология\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "2Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_2Г")
        btn2gV = types.KeyboardButton("ВТОРНИК_2Г")
        btn2gS = types.KeyboardButton("СРЕДА_2Г")
        btn2gCH = types.KeyboardButton("ЧЕТВЕРГ_2Г")
        btn2gPT = types.KeyboardButton("ПЯТНИЦА_2Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn2gP, btn2gV, btn2gS, btn2gCH, btn2gPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)
    elif (message.text == "ПОНЕДЕЛЬНИК_2Г"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разг.о важном\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/физра\n5️⃣16:55-17:35/англ.яз\n")
    elif (message.text == "ВТОРНИК_2Г"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/родной язык\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/лчнря\n5️⃣16:55-17:35/окруж.мир\n6⃣17:45-18:25/физра в/д\n")
    elif (message.text == "СРЕДА_2Г"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/математика\n2️⃣14:25-15:05/рус.яз\n3️⃣15:15-15:55/литер.чтение\n4️⃣16:05-16:45/англ.яз\n5️⃣16:55-17:35/технология\n")
    elif (message.text == "ЧЕТВЕРГ_2Г"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n2️⃣14:25-15:05/математика\n3️⃣15:15-15:55/литер.чтение\n4️⃣16:05-16:45/музыка\n5️⃣16:55-17:35/физра\n")
    elif (message.text == "ПЯТНИЦА_2Г"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз\n2️⃣14:25-15:05/окруж.мир\n3️⃣15:15-15:55/родной язык\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/изо\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "3А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_3А")
        btn3aV = types.KeyboardButton("ВТОРНИК_3А")
        btn3aS = types.KeyboardButton("СРЕДА_3А")
        btn3aCH = types.KeyboardButton("ЧЕТВЕРГ_3А")
        btn3aPT = types.KeyboardButton("ПЯТНИЦА_3А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3aP, btn3aV, btn3aS, btn3aCH, btn3aPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)
    elif (message.text == "ПОНЕДЕЛЬНИК_3A"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/разгов\n2️⃣14:25-14:05/математика\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/труды\n")
    elif (message.text == "ВТОРНИК_3A"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/физра\n2️⃣14:25-14:05/родной язык\n3️⃣15:15-15:55/лчнря\n4️⃣16:05-16:45/рус.яз\n5️⃣16:55-17:35/музыка\n6⃣17:45-18:25/Изо\n")
    elif (message.text == "СРЕДА_3A"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/англ.яз\n2️⃣14:25-14:05/математика\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/окруж.мир\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "ЧЕТВЕРГ_3A"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/физра\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/математика\n4️⃣16:05-16:45/родной язык\n5️⃣16:55-17:35/физры в/д\n")
    elif (message.text == "ПЯТНИЦА_3A"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/англ.яз\n2️⃣14:25-14:05/математика\n3️⃣15:15-15:55/рус.яз\n4️⃣16:05-16:45/окруж.мир\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "3Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_3Б")
        btn3bV = types.KeyboardButton("ВТОРНИК_3Б")
        btn3bS = types.KeyboardButton("СРЕДА_3Б")
        btn3bCH = types.KeyboardButton("ЧЕТВЕРГ_3Б")
        btn3bPT = types.KeyboardButton("ПЯТНИЦА_3Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3bP, btn3bV, btn3bS, btn3bCH, btn3bPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_3Б"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/разг.о важном\n2️⃣14:25-14:05/физра в/д\n3️⃣15:15-15:55/математика\n4️⃣16:05-16:45/рус.яз\n5️⃣16:55-17:35/литер.чтение\n6⃣17:45-18:25/музыка\n")
    elif (message.text == "ВТОРНИК_3Б"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/англ.яз\n2️⃣14:25-14:05/родной язык\n3️⃣15:15-15:55/лчнря\n4️⃣16:05-16:45/математика\n5️⃣16:55-17:35/рус.яз\n")
    elif (message.text == "СРЕДА_3Б"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/математика\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/физра\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/изо\n")
    elif (message.text == "ЧЕТВЕРГ_3Б"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/математика\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/физра\n4️⃣16:05-16:45/родной. язык\n5️⃣16:55-17:35/окруж.мир\n")
    elif (message.text == "ПЯТНИЦА_3Б"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/англ.яз\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/окруж.мир\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/технология\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "3В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_3В")
        btn3vV = types.KeyboardButton("ВТОРНИК_3В")
        btn3vS = types.KeyboardButton("СРЕДА_3В")
        btn3vCH = types.KeyboardButton("ЧЕТВЕРГ_3В")
        btn3vPT = types.KeyboardButton("ПЯТНИЦА_3В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3vP, btn3vV, btn3vS, btn3vCH, btn3vPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_3В"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/разг.о важном\n2️⃣14:25-14:05/англ.яз\n3️⃣15:15-15:55/физра\n4️⃣16:05-16:45/математика\n5️⃣16:55-17:35/рус.яз\n")
    elif (message.text == "ВТОРНИК_3В"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/математика\n2️⃣14:25-14:05/родной язык\n3️⃣15:15-15:55/ лчнря\n4️⃣16:05-16:45/рус.яз\n5️⃣16:55-17:35/физра в/д\n")
    elif (message.text == "СРЕДА_3В"):
        bot.send_message(message.chat.id, "0⃣12:50-13:30/музыка\n1️⃣13:35-14:15/математика\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/физра\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/изо\n")
    elif (message.text == "ЧЕТВЕРГ_3В"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/англ.яз\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/литер.чтение\n4️⃣16:05-16:45/родной язык\n5️⃣16:55-17:35/окруж.мир\n")
    elif (message.text == "ПЯТНИЦА_3В"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/рус.яз\n2️⃣14:25-14:05/математика\n3️⃣15:15-15:55/окруж.мир\n4️⃣16:05-16:45/литер.чтение\n 5️⃣16:55-17:35/технология\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "3Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_3Г")
        btn3gV = types.KeyboardButton("ВТОРНИК_3Г")
        btn3gS = types.KeyboardButton("СРЕДА_3Г")
        btn3gCH = types.KeyboardButton("ЧЕТВЕРГ_3Г")
        btn3gPT = types.KeyboardButton("ПЯТНИЦА_3Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3gP, btn3gV, btn3gS, btn3gCH, btn3gPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_3Г"):
        bot.send_message(message.chat.id, " 1️⃣13:35-14:15/разг.о важном\n2️⃣14:25-14:05/рус.яз\n3️⃣15:15-15:55/математика\n4️⃣16:05-16:45/окруж.мир\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "ВТОРНИК_3Г"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/рус.яз\n 2️⃣14:25-14:05/родной язык\n3️⃣15:15-15:55/лчнря\n4️⃣16:05-16:45/англ.яз\n5️⃣16:55-17:35/технология\n")
    elif (message.text == "СРЕДА_3Г"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/рус.яз\n2️⃣14:25-14:05/физра\n3️⃣15:15-15:55/математика\n4️⃣16:05-16:45/литер.чтение\n5️⃣16:55-17:35/изо\n6⃣17:45-18:25/музыка\n")
    elif (message.text == "ЧЕТВЕРГ_3Г"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/рус.яз\n2️⃣14:25-14:05/физра\n3️⃣15:15-15:55/математика\n4️⃣16:05-16:45/родной язык\n5️⃣16:55-17:35/окруж.мир\n")
    elif (message.text == "ПЯТНИЦА_3Г"):
        bot.send_message(message.chat.id, "1️⃣13:35-14:15/рус.яз\n2️⃣14:25-14:05/физра в/д\n3️⃣15:15-15:55/англ.яз\n4️⃣16:05-16:45/математика\n5️⃣16:55-17:35/литер.чтение\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "4А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_4А")
        btn4aV = types.KeyboardButton("ВТОРНИК_4А")
        btn4aS = types.KeyboardButton("СРЕДА_4А")
        btn4aCH = types.KeyboardButton("ЧЕТВЕРГ_4А")
        btn4aPT = types.KeyboardButton("ПЯТНИЦА_4А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4aP, btn4aV, btn4aS, btn4aCH, btn4aPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_4А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разг.о важном\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/физра\n4️⃣11:05-11:45/рус.яз\n5️⃣12:00-12:40/литер.чтение\n")
    elif (message.text == "ВТОРНИК_4А"):
        bot.send_message(message.chat.id, " 1️⃣8:30-9:10/математика\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/литер.чтение\n4️⃣11:05-11:45/англ.яз\n5️⃣12:00-12:40/технология\n")
    elif (message.text == "СРЕДА_4А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/литер.чтение\n4️⃣11:05-11:45/родной язык\n5️⃣12:00-12:40/лчнря\n")
    elif (message.text == "ЧЕТВЕРГ_4А"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/англ.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/рус.яз\n4️⃣11:05-11:45/физра в/д\n5️⃣12:00-12:40/окруж.мир\n6⃣12:50-13:30/музыка\n")
    elif (message.text == "ПЯТНИЦА_4А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физра\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/окруж.мир\n4️⃣11:05-11:45/оркисэ\n5️⃣12:00-12:40/изо\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3,)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "4Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_4Б")
        btn4bV= types.KeyboardButton("ВТОРНИК_4Б")
        btn4bS = types.KeyboardButton("СРЕДА_4Б")
        btn4bCH = types.KeyboardButton("ЧЕТВЕРГ_4Б")
        btn4bPT = types.KeyboardButton("ПЯТНИЦА_4Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4bP, btn4bV, btn4bS, btn4bCH, btn4bPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_4Б"):
        bot.send_message(message.chat.id, " 1️⃣8:30-9:10/разг.о важном\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/математика\n4️⃣11:05-11:45/литер.чтение\n5️⃣12:00-12:40/физра\n")
    elif (message.text == "ВТОРНИК_4Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/литер.чтение\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/рус.яз\n4️⃣11:05-11:45/окруж.мир\n5️⃣12:00-12:40/изо\n")
    elif (message.text == "СРЕДА_4Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/окруж.мир\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/англ.яз\n4️⃣11:05-11:45/родной язык\n5️⃣12:00-12:40/лчнря\n")
    elif (message.text == "ЧЕТВЕРГ_4Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/англ.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/физра\n4️⃣11:05-11:45/рус.яз\n5️⃣12:00-12:40/оркисэ\n6⃣12:50-13:30/музыка\n")
    elif (message.text == "ПЯТНИЦА_4Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/англ.яз\n2️⃣9:20-10:00/физра\n3️⃣10:10-10:50/математика\n4️⃣11:05-11:45/рус.яз\n5️⃣12:00-12:40/технология\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "4В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_4В")
        btn4vV = types.KeyboardButton("ВТОРНИК_4В")
        btn4vS = types.KeyboardButton("СРЕДА_4В")
        btn4vCH = types.KeyboardButton("ЧЕТВЕРГ_4В")
        btn4vPT = types.KeyboardButton("ПЯТНИЦА_4В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4vP, btn4vV, btn4vS, btn4vCH, btn4vPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_4В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разг.о важном\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/рус.яз\n4️⃣11:05-11:45/литер.чтение\n5️⃣12:00-12:40/технология\n")
    elif (message.text == "ВТОРНИК_4В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/окруж.мир\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/физра\n4️⃣11:05-11:45/математика\n5️⃣12:00-12:40/литер.чтение\n")
    elif (message.text == "СРЕДА_4В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/англ.яз\n3️⃣10:10-10:50/физра в/д\n4️⃣11:05-11:45/родной язык\n5️⃣12:00-12:40/лчнря\n6⃣12:50-13:30/изо\n")
    elif (message.text == "ЧЕТВЕРГ_4В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/окруж.мир\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/математика\n4️⃣11:05-11:45/англ.яз\n5️⃣12:00-12:40/музыка\n")
    elif (message.text == "ПЯТНИЦА_4В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/оркисэ\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/физра\n4️⃣11:05-11:45/математика\n5️⃣12:00-12:40/литер.чтение\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "4Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_4Г")
        btn4gV = types.KeyboardButton("ВТОРНИК_4Г")
        btn4gS = types.KeyboardButton("СРЕДА_4Г")
        btn4gCH = types.KeyboardButton("ЧЕТВЕРГ_4Г")
        btn4gPT = types.KeyboardButton("ПЯТНИЦА_4Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4gP, btn4gV, btn4gS, btn4gCH, btn4gPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_4Г"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/разг.о важном\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/математик\n4️⃣11:05-11:45/англ.яз\n5️⃣12:00-12:40/окруж.мир\n")
    elif (message.text == "ВТОРНИК_4Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/литер.чтение\n4️⃣11:05-11:45/физра\n5️⃣12:00-12:40/оркисэ\n6⃣12:50-13:30/музыка\n")
    elif (message.text == "СРЕДА_4Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/окруж.мир\n4️⃣11:05-11:45/родной язык\n 5️⃣12:00-12:40/лчнря\n")
    elif (message.text == "ЧЕТВЕРГ_4Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физра в/д\n2️⃣9:20-10:00/англ.яз\n3️⃣10:10-10:50/рус.яз\n4️⃣11:05-11:45/литер.чтение\n5️⃣12:00-12:40/изо\n")
    elif (message.text == "ПЯТНИЦА_4Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n 2️⃣9:20-10:00/матем\n3️⃣10:10-10:50/литер.чтение\n4️⃣11:05-11:45/физра\n5️⃣12:00-12:40/технология")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "4Д"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4dP = types.KeyboardButton("ПОНЕДЕЛЬНИК_4Д")
        btn4dV = types.KeyboardButton("ВТОРНИК_4Д")
        btn4dS = types.KeyboardButton("СРЕДА_4Д")
        btn4dCH = types.KeyboardButton("ЧЕТВЕРГ_4Д")
        btn4dPT = types.KeyboardButton("ПЯТНИЦА_4Д")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4dP, btn4dV, btn4dS, btn4dCH, btn4dPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_4Д"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разг.о важном\n2️⃣9:20-10:00/рус.яз\n3️⃣10:10-10:50/математика\n4️⃣11:05-11:45/физра\n5️⃣12:00-12:40/физра в/д\n6⃣12:50-13:30/музыка\n")
    elif (message.text == "ВТОРНИК_4Д"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/литер.чтение\n4️⃣11:05-11:45/окруж.мир\n5️⃣12:00-12:40/технология\n")
    elif (message.text == "СРЕДА_4Д"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/литер.чтение\n4️⃣11:05-11:45/родной язык\n5️⃣12:00-12:40/лчнря\n")
    elif (message.text == "ЧЕТВЕРГ_4Д"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/литер.чтение\n3️⃣10:10-10:50/англ.яз\n4️⃣11:05-11:45/окруж.мир\n5️⃣12:00-12:40/оркисэ\n")
    elif (message.text == "ПЯТНИЦА_4Д"):
        bot.send_message(message.chat.id, " 1️⃣8:30-9:10/рус.яз\n2️⃣9:20-10:00/математика\n3️⃣10:10-10:50/англ.яз\n4️⃣11:05-11:45/изо\n5️⃣12:00-12:40/физра\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "5А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_5А")
        btn5aV = types.KeyboardButton("ВТОРНИК_5А")
        btn5aS = types.KeyboardButton("СРЕДА_5А")
        btn5aCH = types.KeyboardButton("ЧЕТВЕРГ_5А")
        btn5aPT = types.KeyboardButton("ПЯТНИЦА_5А")
        btn5aSYB = types.KeyboardButton("СУББОТА")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn5aP, btn5aV, btn5aS, btn5aCH, btn5aPT,btn5aSYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_5А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов\n2️⃣9:20-10:10/матем/318\n3️⃣10:10-10:50/изо/208\n4️⃣11:05-11:45/рус.яз/302\n5️⃣12:00-12:40/литер/302\n6️⃣12:50-13:30/музыку/224\nℹВнеурочка\n13:35/мат/107\n14:25/англ/322\n15:15/ДЮП/114\n16:00/мастерица/114\n")
    elif (message.text == "ВТОРНИК_5А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/англ.яз/322,106\n2️⃣9:20-10:10/история/205\n3️⃣10:10-10:50/рус.яз/302\n4️⃣11:05-11:45/литер/302\n5️⃣12:00-12:40/матем/318\n6️⃣12:50-13:30/ОДНК/121\n")
    elif (message.text == "СРЕДА_5А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/русс.яз/302\n2️⃣9:20-10:10/география/315\n3️⃣10:10-10:50/родной/308/108/224\n4️⃣11:05-11:45/матем/318\n5️⃣12:00-12:40/физ-ра/210\n6️⃣12:50-13:30/труд/124/114\n7️⃣13:35-14:15/труд/124/114\n")
    elif (message.text == "ЧЕТВЕРГ_5А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/литр/302\n2️⃣9:20-10:10/рус.яз/302\n3️⃣10:10-10:50/физ-ра/210\n4️⃣11:05-11:45/матем/318\n5️⃣12:00-12:40/англ.яз/322/107\n6️⃣12:50-13:30/биология/224\nℹВнеурочка\n14:25/Башкирский/308\n")
    elif (message.text == "ПЯТНИЦА_5А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/история/205\n2️⃣9:20-10:10/рус.яз/302\n3️⃣10:10-10:50/англ.яз/322/124\n4️⃣11:05-11:45/матем/318\n5️⃣12:00-12:40/род.яз/308/107/221\n6️⃣12:50-13:30/род.лит/308/107/221\n7️⃣13:35-14:15/ВД ФП/210\nℹВнеурочка\n9:00/ю.армия/205\n14:15/ч.грам/303\n")
    elif (message.text == "СУББОТА_5А"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/3d модел/318-114\n10:00/обж/116\n10:40/обж/116\n10:40/3d модел/318-114\n11:20/3d модел/318-114\n12:00/3d модел/318-114\n13:00/футбол/210\n13:35/ю.армия/210\n")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "5Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_5Б")
        btn5bV = types.KeyboardButton("ВТОРНИК_5Б")
        btn5bS = types.KeyboardButton("СРЕДА_5Б")
        btn5bCH = types.KeyboardButton("ЧЕТВЕРГ_5Б")
        btn5bPT = types.KeyboardButton("ПЯТНИЦА_5Б")
        btn5bSYB = types.KeyboardButton("СУББОТА_5Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn5bP, btn5bV, btn5bS, btn5bCH, btn5bPT,btn5bSYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_5Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/221\n2️⃣9:20-10:10/история/221\n3️⃣10:10-10:50/рус.яз/302\n4️⃣11:05-11:45/изо/208\n5️⃣12:00-12:40/матем/305\n6️⃣12:50-13:30/литер/302\n7️⃣13:35-14:15/физ-ра/210\nℹВнеурочка\n14:25/англ/322\n16:35/Мастерица/124\n")
    elif (message.text == "ВТОРНИК_5Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/302\n2️⃣9:20-10:10/география/219\n3️⃣10:10-10:50/ОДНК/219\n4️⃣11:05-11:45/матем/305\n5️⃣12:00-12:40/англ.яз/322/106\n6️⃣12:50-13:30/литер/302\nℹВнеурочка\n15:15/ДЮП/114\n")
    elif (message.text == "СРЕДА_5Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физ-ра/210\n2️⃣9:20-10:10/матем/305\n3️⃣10:10-10:50/родной/308/107/302\n4️⃣11:05-11:45/рус.яз/302\n5️⃣12:00-12:40/англ/322/124\n6️⃣12:50-13:30/музыка/224\n7️⃣13:35-14:15/ВД ФП/21\n")
    elif (message.text == "ЧЕТВЕРГ_5Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/труды/124/114\n2️⃣9:20-10:10/труды/124/114\n3️⃣10:10-10:50/матем/305\n4️⃣11:05-11:45/рус.яз/302\n5️⃣12:00-12:40/история/221\n6️⃣12:50-13:30/литр/302\nℹВнеурочка\n14:25/башкирский/308\n")
    elif (message.text == "ПЯТНИЦА_5Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/3052️⃣9:20-10:10/биология/219\n3️⃣10:10-10:50/рус.яз/302\n4️⃣11:05-11:45/англ/322/124\n5️⃣12:00-12:40/родной/308/107/302\n6️⃣12:50-13:30/род.лит/308/107/302\nℹВнеурочка\n9:30/ю.армия/205\n")
    elif (message.text == "СУББОТА_5Б"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/3d модел/318-114\n10:00/обж/116\n10:40/обж/116\n10:40/3d модел/318-114\n11:20/3d модел/318-114\n12:00/3d модел/318-114\n13:00/футбол/210\n13:35/ю.армия/210\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "5В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_5В")
        btn5vV = types.KeyboardButton("ВТОРНИК_5В")
        btn5vS = types.KeyboardButton("СРЕДА_5В")
        btn5vCH = types.KeyboardButton("ЧЕТВЕРГ_5В")
        btn5vPT = types.KeyboardButton("ПЯТНИЦА_5В")
        btn5vSYB = types.KeyboardButton("СУББОТА_5В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn5vP, btn5vV, btn5vS, btn5vCH, btn5vPT,btn5vSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_5В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/219\n2️⃣9:20-10:10/изо/208\n3️⃣10:10-10:50/рус.яз/205\n4️⃣11:05-11:45/матем/224\n5️⃣12:00-12:40/англ.яз/322/116\n6️⃣12:50-13:30/литер/208\nℹВнеурочка\n14:25/англ/322\n")
    elif (message.text == "ВТОРНИК_5В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ОДНК/219\n2️⃣9:20-10:10/матем/221\n3️⃣10:10-10:50/англ.яз/322/106\n4️⃣11:05-11:45/рус.яз/208\n5️⃣12:00-12:40/труды/124/114\n6️⃣12:50-13:30/труды/124/114\nℹВнеурочка\n15:15/мат/131\n")
    elif (message.text == "СРЕДА_5В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/география/315\n2️⃣9:20-10:10/матем/308\n3️⃣10:10-10:50/родной/208/308/107\n4️⃣11:05-11:45/физ-ра/210\n5️⃣12:00-12:40/рус.яз/318\n6️⃣12:50-13:30/литер/303\nℹВнеурочка\n15:15/ДЮП/108\n")
    elif (message.text == "ЧЕТВЕРГ_5В"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/матем/308\n2️⃣9:20-10:10/история/221\n3️⃣10:10-10:50/биологию/221\n4️⃣11:05-11:45/физ-ра/210\n5️⃣12:00-12:40/рус.яз/302\n6️⃣12:50-13:30/англ.яз/322/107\n7️⃣13:35-14:15/ВД ФП/210\nℹВнеурочка\n14:25/башкирский/308\n")
    elif (message.text == "ПЯТНИЦА_5В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/208\n2️⃣9:20-10:10/рус.яз/303\n3️⃣10:10-10:50/литер/303\n4️⃣11:05-11:45/история /221\n5️⃣12:00-12:40/родной/303/308/107\n6️⃣12:50-13:30/род.литр/303/308/107\n7️⃣13:35-14:15/музыка/224\nℹВнеурочка\n10:00/ю.армия/205\n15:15/мастерица/124\n")
    elif(message.text == "СУББОТА_5В"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/3d модел/318-114\n10:00/обж/116\n10:40/обж/116\n10:40/3d модел/318-114\n11:20/3d модел/318-114\n12:00/3d модел/318-114\n13:00/футбол/210\n13:35/ю.армия/210\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "5Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_5Г")
        btn5gV = types.KeyboardButton("ВТОРНИК_5Г")
        btn5gS = types.KeyboardButton("СРЕДА_5Г")
        btn5gCH = types.KeyboardButton("ЧЕТВЕРГ_5Г")
        btn5gPT = types.KeyboardButton("ПЯТНИЦА_5Г")
        btn5gSYB = types.KeyboardButton("СУББОТА_5Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn5gP, btn5gV, btn5gS, btn5gCH, btn5gPT,btn5gSYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_5Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/121\n2️⃣9:20-10:10/англ.яз/106\n3️⃣10:10-10:50/ВД ФП/210\n4️⃣11:05-11:45/матем/217\n5️⃣12:00-12:40/рус.яз /124\n6️⃣12:50-13:30/труды/124/114\n7️⃣13:35-14:15/труды/124/114\nℹВнеурочка\n16:00/ДЮП/108\n")
    elif (message.text == "ВТОРНИК_5Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/124\n2️⃣9:20-10:10/литер/124\n3️⃣10:10-10:50/матем/217\n4️⃣11:05-11:45/ОДНК/315\n5️⃣12:00-12:40/физ-ра/210\n6️⃣12:50-13:30/музыка/224\n7️⃣13:35-14:15/изо/104\n")
    elif (message.text == "СРЕДА_5Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/217\n2️⃣9:20-10:10/рус.яз/124\n3️⃣10:10-10:50/родной/308/107/124\n4️⃣11:05-11:45/литер/124\n5️⃣12:00-12:40/история/221\n6️⃣12:50-13:30/англ.яз/116\n")
    elif (message.text == "ЧЕТВЕРГ_5Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/география/221\n2️⃣9:20-10:10/биология/219\n3️⃣10:10-10:50/матем /217\n4️⃣11:05-11:45/история/224\n5️⃣12:00-12:40/рус.яз/217\n6️⃣12:50-13:30/литер /217\nℹВнеурочка\n13:35/мат/307\n14:25/башкирский/308\n15:15/ч.грам/107\n")
    elif (message.text == "ПЯТНИЦА_5Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/217\n2️⃣9:20-10:10/англ.яз/124\n3️⃣10:10-10:50/рус.яз/224\n4️⃣11:05-11:45/физ-ра/210\n5️⃣12:00-12:40/родной/308/107/121\n6️⃣12:50-13:30/род.литр/308/107/121\nℹВнеурочка\n09:00/ю.армия/205\n16:00/мастерица/124\n")
    elif (message.text == "СУББОТА_5Г"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/3d модел/318-114\n10:00/обж/116\n10:40/обж/116\n10:40/3d модел/318-114\n11:20/3d модел/318-114\n12:00/3d модел/318-114\n13:00/футбол/210\n13:35/ю.армия/210\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        button4 = types.KeyboardButton("Меню столовой")
        markup.add(button1, button2, button3,button4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "6А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_6А")
        btn6aV = types.KeyboardButton("ВТОРНИК_6А")
        btn6aS = types.KeyboardButton("СРЕДА_6А")
        btn6aCH = types.KeyboardButton("ЧЕТВЕРГ_6А")
        btn6aPT= types.KeyboardButton("ПЯТНИЦА_6А")
        btn6aSYB = types.KeyboardButton ("СУББОТА_6А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn6aP, btn6aV, btn6aS, btn6aCH, btn6aPT,btn6aSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_6А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разгов/205\n2️⃣14:25-15:05/матем/205\n3️⃣15:15-15:55/ рус.яз/302\n4️⃣16:05-16:45/родной/302\n5️⃣16:55-17:35/изо/208\n6️⃣17:45-18:25/физ-ра/210\n7️⃣18:35-19:15/ВД ФП/210\nℹВнеурочка\n10:00/ю.техник/114\n12:50/башкирский/223\n")
    elif (message.text == "ВТОРНИК_6А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/англ.яз/320/116\n2️⃣14:25-15:05/рус.яз/303\n3️⃣15:15-15:55/ литер/303\n4️⃣16:05-16:45/матем /305\n5️⃣16:55-17:35/музыка/224\n6️⃣17:45-18:25/география/307\nℹВнеурочка\n10:00/черч/209\n12:50/англ/320\n")
    elif (message.text == "СРЕДА_6А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз/304 \n2️⃣14:25-15:05/англ.яз/320/116\n3️⃣15:15-15:55/ рус.яз/308\n4️⃣16:05-16:45/матем/315\n5️⃣16:55-17:35/родной/308\n6️⃣17:45-18:25/литер/308\n7️⃣18:35-19:15/биология/315\nℹВнеурочка\n10:10/ЮИД/223\n")
    elif (message.text == "ЧЕТВЕРГ_6А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/род.лит/305\n2️⃣14:25-15:05/рус.яз/302\n3️⃣15:15-15:55/ история/221\n4️⃣16:05-16:45/общ/221\n5️⃣16:55-17:35/англ.яз/320/116\n6️⃣17:45-18:25/матем/305\nℹВнеурочка\n12:00/мат/208\n")
    elif (message.text == "ПЯТНИЦА_6А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз/224\n2️⃣14:25-15:05/история/221\n3️⃣15:15-15:55/ матем/305\n4️⃣16:05-16:45/физ-ра/210\n5️⃣16:55-17:35/литер/315\n6️⃣17:45-18:25/труды/124/114\n7️⃣18:35-19:15/труды/124/114\nℹВнеурочка\n11:05/англ/116\n")
    elif (message.text == "СУББОТА_6А"):
        bot.send_message(message.chat.id, "ℹВнеурочка\n11:00/баскетбол/210\n11:50/баскетбол/210\n12:40/3d модел/318-114\n13:20/3d модел/318-114\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "6Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_6Б")
        btn6bV = types.KeyboardButton("ВТОРНИК_6Б")
        btn6bS = types.KeyboardButton("СРЕДА_6Б")
        btn6bCH = types.KeyboardButton("ЧЕТВЕРГ_6Б")
        btn6bPT = types.KeyboardButton("ПЯТНИЦА_6Б")
        btn6bSYB = types.KeyboardButton("СУББОТА_6Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn6bP, btn6bV, btn6bS, btn6bCH, btn6bPT,btn6bSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_6Б"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разгов/305\n2️⃣14:25-15:05/рус.яз/224\n3️⃣15:15-15:55/ матем/205\n4️⃣16:05-16:45/литер/221\n5️⃣16:55-17:35/физ-ра/210\n6️⃣17:45-18:25/род.лит/308/224\n7️⃣18:35-19:15/род/308/224\nℹВнеурочка\n10:35/ю.техник/114\n12:50/башкирский/223\n")
    elif (message.text == "ВТОРНИК_6Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/ВД ФП/210\n2️⃣13:35:14:15/история/205\n3️⃣14:25-15:05/рус.яз/224\n4️⃣15:15-15:55/матем/305\n5️⃣16:05-16:45/англ.яз/106\n6️⃣16:55-17:35/география/307\n7️⃣17:45-18:25/музыка/224\nℹВнеурочка\n10:00/черч/209\n12:00/англ/320\n")
    elif (message.text == "СРЕДА_6Б"):
        bot.send_message(message.chat.id,"1️⃣13:35:14:15/англ.яз/303\n2️⃣14:25-15:05/матем/315\n3️⃣15:15-15:55/ рус.яз/224\n4️⃣16:05-16:45/рус.яз/224\n5️⃣16:55-17:35/биология/315\n6️⃣17:45-18:25/литер/224\nℹВнеурочка\n10:50/ЮИД/223\n")
    elif (message.text == "ЧЕТВЕРГ_6Б"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/матем/305\n2️⃣14:25-15:05/история/205\n3️⃣15:15-15:55/ рус.яз/224\n4️⃣16:05-16:45/общ/205\n5️⃣16:55-17:35/родной/308/224\n6️⃣17:45-18:25/труды/114\n7️⃣18:35-19:15/труды/114\n")
    elif (message.text == "ПЯТНИЦА_6Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/изо/208\n2️⃣13:35:14:15/матем/205\n3️⃣14:25-15:05/англ.яз/208\n4️⃣15:15-15:55/ рус.яз/124\n5️⃣16:05-16:45/физ-ра/210\n6️⃣16:55-17:35/литература/121\nℹВнеурочка\n12:00/мат/208\n")
    elif(message.text == "СУББОТА_6Б"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n11:00/баскетбол/210\n11:50/баскетбол/210\n12:40/3d модел/318-114\n13:20/3d модел/318-114\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "6В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6P = types.KeyboardButton("ПОНЕДЕЛЬНИК_6В")
        btn6V = types.KeyboardButton("ВТОРНИК_6В")
        btn6S = types.KeyboardButton("СРЕДА_6В")
        btn6CH = types.KeyboardButton("ЧЕТВЕРГ_6В")
        btn6PT = types.KeyboardButton("ПЯТНИЦА_6В")
        btn6SYB = types.KeyboardButton("СУББОТА_6В")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn6P, btn6V, btn6S, btn6CH, btn6PT,btn6SYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_6В"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разгов/307\n2️⃣14:25-15:05/англ.яз/322/316\n3️⃣15:15-15:55/ рус.яз/208\n4️⃣16:05-16:45/матем/205\n5️⃣16:55-17:35/литер/205\n6️⃣17:45-18:25/род.лит/308/107/303\n7️⃣18:35-19:15/родной/308/107/303\nℹВнеурочка\n10:00/ЮИД/116\n10:35/ю.техник/114\n12:50/башкирский/223\n")
    elif (message.text == "ВТОРНИК_6В"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз/208\n2️⃣14:25-15:05/матем/305\n3️⃣15:15-15:55/ литер/302\n4️⃣16:05-16:45/изо/208\n5️⃣16:55-17:35/история/205\n6️⃣17:45-18:25/труды/124\n7️⃣18:35-19:15/труды/124\nℹВнеурочка\n10:40/черч/209\n12:50/англ/322\n")
    elif (message.text == "СРЕДА_6В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/биология/315\n2️⃣13:35:14:15/матем/305\n3️⃣14:25-15:05/рус.яз/303\n4️⃣15:15-15:55/литер/303\n5️⃣16:05-16:45/физ-ра/210\n6️⃣16:55-17:35/география/219\nℹВнеурочка\n12:00/мат/208\n")
    elif (message.text == "ЧЕТВЕРГ_6В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/рус.яз/205\n2️⃣13:35:14:15/англ.яз/322/116\n3️⃣14:25-15:05/рус.яз/208\n4️⃣15:15-15:55/история/205\n5️⃣16:05-16:45/матем/304\n6️⃣16:55-17:35/род/308/107/121\n7️⃣17:45-18:25/ВД ФП/210\n")
    elif (message.text == "ПЯТНИЦА_6В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/общ/205\n2️⃣13:35:14:15/рус/108\n3️⃣14:25-15:05/англ.яз/322/116\n4️⃣15:15-15:55/музыка /224\n5️⃣16:05-16:45/матем/305\n6️⃣16:55-17:35/физ-ра /210\nℹВнеурочка\n11:05/англ/116\n")
    elif(message.text == "СУББОТА_6В"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n11:00/баскетбол/210\n11:50/баскетбол/210\n12:40/3d модел/318-114\n13:20/3d модел/318-114\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "6Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_6Г")
        btn6gV = types.KeyboardButton("ВТОРНИК_6Г")
        btn6gS = types.KeyboardButton("СРЕДА_6Г")
        btn6gCH = types.KeyboardButton("ЧЕТВЕРГ_6Г")
        btn6gPT = types.KeyboardButton("ПЯТНИЦА_6Г")
        btn6gSYB = types.KeyboardButton ("СУББОТА_6Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn6gP, btn6gV, btn6gS, btn6gCH, btn6gPT,btn6gSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_6Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/ВД ФП/210\n2️⃣13:35:14:15/разгов/208\n3️⃣14:25-15:05/рус.яз/208\n4️⃣15:15-15:55/англ/107/116\n5️⃣16:05-16:45/музыка/224\n6️⃣16:55-17:35/матем/119\n7️⃣17:45-18:25/род.лит/302/308/107\n8️⃣18:35-19:15/род/302/308/107\nℹВнеурочка\n10:40/ЮИД/116\n11:10/ю.техник/114\n12:50/башкирский/223\n")
    elif (message.text == "ВТОРНИК_6Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/рус.яз/208\n2️⃣13:35:14:15/матем/305\n3️⃣14:25-15:05/общ/221\n4️⃣15:15-15:55/география/205\n5️⃣16:05-16:45/литер/302\n6️⃣16:55-17:35/англ.яз/106/116\nℹВнеурочка\n10:40/черч/209\n12:00/мат/208\n")
    elif (message.text == "СРЕДА_6Г"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/рус.яз/208 \n2️⃣14:25-15:05/англ/208/116\n3️⃣15:15-15:55/ биология/219\n4️⃣16:05-16:45/матем/315\n5️⃣16:55-17:35/рус.яз/303\n6️⃣17:45-18:25/труды/114/124\n7️⃣18:35-19:15/труды/114/124\n")
    elif (message.text == "ЧЕТВЕРГ_6Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/история/221\n2️⃣13:35:14:15/рус.яз/208\n3️⃣14:25-15:05/матем/217\n4️⃣15:15-15:55/физ-ра/210\n5️⃣16:05-16:45/литер/208\n6️⃣16:55-17:35/род/208/308/107\n")
    elif (message.text == "ПЯТНИЦА_6Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/матем/305\n2️⃣13:35:14:15/изо/208\n3️⃣14:25-15:05/история/221\n4️⃣15:15-15:55/рус.яз/303\n5️⃣16:05-16:45/литер/303\n6️⃣16:55-17:35/физ-ра/210\nℹВнеурочка\n11:05/англ/116\n")
    elif (message.text == "СУББОТА_6Г"):
        bot.send_message(message.chat.id, "ℹВнеурочка\n11:00/баскетбол/210\n11:50/баскетбол/210\n12:40/3d модел/318-114\n13:20/3d модел/318-114\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "6Д"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6dP = types.KeyboardButton("ПОНЕДЕЛЬНИК_6Д")
        btn6dV = types.KeyboardButton("ВТОРНИК_6Д")
        btn6dS = types.KeyboardButton("СРЕДА_6Д")
        btn6dCH = types.KeyboardButton("ЧЕТВЕРГ_6Д")
        btn6dPT = types.KeyboardButton("ПЯТНИЦА_6Д")
        btn6dSYB = types.KeyboardButton("СУББОТА_6Д")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn6dP, btn6dV, btn6dS, btn6dCH, btn6dPT,btn6dSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_6Д"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/разгов/308\n2️⃣13:35:14:15/англ/217/121\n3️⃣14:25-15:05/рус.яз/224\n4️⃣15:15-15:55/матем/217\n5️⃣16:05-16:45/история/221\n6️⃣16:55-17:35/род.лит/302/107/308\n7️⃣17:45-18:25/родной/302/107/308\nℹВнеурочка\n11:10/ю.техник/114\n12:00/мат/205\n12:50/башкирский/223\n")
    elif (message.text == "ВТОРНИК_6Д"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/англ.яз/320/116\n2️⃣14:25-15:05/рус.яз/303\n3️⃣15:15-15:55/ литер/303\n4️⃣16:05-16:45/матем /305\n5️⃣16:55-17:35/музыка/224\n6️⃣17:45-18:25/география/307\nℹВнеурочка\n12:50/англ/106\n")
    elif (message.text == "СРЕДА_6Д"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/матем/217\n2️⃣13:35:14:15/рус.яз/221\n3️⃣14:25-15:05/англ.яз/106/208\n4️⃣15:15-15:55/биология/219\n5️⃣16:05-16:45/литер/224\n6️⃣16:55-17:35/география/219\n")
    elif (message.text == "ЧЕТВЕРГ_6Д"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/рус.яз/224\n2️⃣13:35:14:15/рус.яз/224\n3️⃣14:25-15:05/матем/227\n4️⃣15:15-15:55/литер/224\n5️⃣16:05-16:45/род/124/108/107\n6️⃣16:55-17:35/физ-ра/210\n7️⃣17:45-18:25/ВД ФП/210\n")
    elif (message.text == "ПЯТНИЦА_6Д"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/матем/217\n2️⃣13:35:14:15/история/219\n3️⃣14:25-15:05/изо/208\n4️⃣15:15-15:55/рус.яз/121\n5️⃣16:05-16:45/общ/205\n6️⃣16:55-17:35/физ-ра/210\nℹВнеурочка\n12:50/англ/310\n")
    elif(message.text == "СУББОТА_6Д"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/3d модел/318-114\n10:00/обж/116\n10:40/обж/116\n10:40/3d модел/318-114\n11:20/3d модел/318-114\n12:00/3d модел/318-114\n13:00/футбол/210\n13:35/ю.армия/210\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "7А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_7А")
        btn7aV = types.KeyboardButton("ВТОРНИК_7А")
        btn7aS = types.KeyboardButton("СРЕДА_7А")
        btn7aCH = types.KeyboardButton("ЧЕТВЕРГ_7А")
        btn7aPT = types.KeyboardButton("ПЯТНИЦА_7А")
        btn7aSYB = types.KeyboardButton("СУББОТА_7А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn7aP, btn7aV, btn7aS, btn7aCH, btn7aPT,btn7aSYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_7А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/разгов/ 315\n2️⃣14:25-15:05/матем/304\n3️⃣15:15-15:55/ геогр/219\n4️⃣16:05-16:45/матем/304\n5️⃣16:55-17:35/родной/303/308/107\n6️⃣17:45-18:25/технолог/114\n7️⃣18:35-19:15/технолог/124/114\nℹВнеурочка\n12:00/ю.армия/121\n12:50/мат/304\n")
    elif (message.text == "ВТОРНИК_7А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/матем/304\n2️⃣14:25-15:05/физ-ра/210\n3️⃣15:15-15:55/ биология/315\n4️⃣16:05-16:45/русс.яз/303\n5️⃣16:55-17:35/геогр/219\n6️⃣17:45-18:25/литер/303\n7️⃣18:35-19:15/физика/307ℹВнеурочка\n14:30/родничок/223\n")
    elif (message.text == "СРЕДА_7А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/матем/304\n2️⃣14:25-15:05/англ.яз/121/106\n3️⃣15:15-15:55/история/205\n4️⃣16:05-16:45/общ/205\n5️⃣16:55-17:35/физика/307\n6️⃣17:45-18:25/русс.яз/303\n7️⃣18:35-19:15/физ-ра/210\nℹВнеурочка\n10:10/англ/116\n11:05/англ/116\n")
    elif (message.text == "ЧЕТВЕРГ_7А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/матем/304\n2️⃣14:25-15:05/англ.яз/107/106\n3️⃣15:15-15:55/инфор/309/318\n4️⃣16:05-16:45/русс.яз/124\n5️⃣16:55-17:35/история/205\n6️⃣17:45-18:25/родной/124/308/107\n7️⃣18:35-19:15/род.лит/124/308/107")
    elif (message.text == "ПЯТНИЦА_7А"):
        bot.send_message(message.chat.id, "1️⃣13:35:14:15/матем/304\n2️⃣14:25-15:05/русс.яз/315\n3️⃣15:15-15:55/литер/315\n4️⃣16:05-16:45/англ.яз/107/106\n5️⃣16:55-17:35/музыка/224\n6️⃣17:45-18:25/ИЗО/208\n7️⃣18:35-19:15/ВД ФП/210\nℹВнеурочка\n10:00/черч/209\nВ10:40/черч/209\n")
    elif (message.text =="СУББОТА_7А"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n15:30/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "7Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_7Б")
        btn7bV = types.KeyboardButton("ВТОРНИК_7Б")
        btn7bS = types.KeyboardButton("СРЕДА_7Б")
        btn7bCH = types.KeyboardButton("ЧЕТВЕРГ_7Б")
        btn7bPT = types.KeyboardButton("ПЯТНИЦА_7Б")
        btn7bSYB = types.KeyboardButton("СУББОТА_7Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn7bP, btn7bV, btn7bS, btn7bCH, btn7bPT,btn7bSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_7Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/физика/307\n2️⃣13:35:14:15/разговор/304\n3️⃣14:25-15:05/история/221\n4️⃣15:15-15:55/англ.яз/124/106\n5️⃣16:05-16:45/матем/318\n6️⃣16:55-17:35/родной/308/302\n7️⃣17:45-18:25/ВД.ФП/210\nℹВнеурочка\n10:10/ю.фин/304\n12:00/ю.армия/121\n")
    elif (message.text == "ВТОРНИК_7Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/общ/221\n2️⃣13:35:14:15/русс.яз/302\n3️⃣14:25-15:05/литер/302\n4️⃣15:15-15:55/история/221\n5️⃣16:05-16:45/матем/318\n6️⃣16:55-17:35/биология/315\n7️⃣17:45-18:25/геогр/219\nℹВнеурочка\n14:30/родничок/223\n")
    elif (message.text == "СРЕДА_7Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/русс.яз/302\n2️⃣13:35:14:15/литер/302\n3️⃣14:25-15:05/матем/318\n4️⃣15:15-15:55/матем/318\n5️⃣16:05-16:45/англ.яз/121/106\n6️⃣16:55-17:35/физра/210\nℹВнеурочка\n10:10/англ/116\n")
    elif (message.text == "ЧЕТВЕРГ_7Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/физика/307\n2️⃣13:35:14:15/матем/318\n3️⃣14:25-15:05/технолог/124/114\n4️⃣15:15-15:55/технолог/124/114\n5️⃣16:05-16:45/инфор/309/318\n6️⃣16:55-17:35/русс.яз/302\n7️⃣17:45-18:25/родной/308/302\n8️⃣18:35-19:15/род.лит/308/302\nℹВнеурочка\n10:10/англ/116\n")
    elif (message.text == "ПЯТНИЦА_7Б"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/геогр/219\n2️⃣13:35:14:15/русс.яз/302\n3️⃣14:25-15:05/англ.яз/124/106\n4️⃣15:15-15:55/матем/318\n5️⃣16:05-16:45/физ-ра/210\n6️⃣️⃣16:55-17:35/ИЗО/208\n7️⃣17:45-18:25/музыка/224\nℹВнеурочка\n10:00/черч/209\n10:40/черч/209\n12:00/мат/318\n12:00/англ/116\n")
    elif (message.text == "СУББОТА_7Б"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n15:30/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "7В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_7В")
        btn7vV = types.KeyboardButton("ВТОРНИК_7В")
        btn7vS = types.KeyboardButton("СРЕДА_7В")
        btn7vCH = types.KeyboardButton("ЧЕТВЕРГ_7В")
        btn7vPT = types.KeyboardButton("ПЯТНИЦА_7В")
        btn7vSYB = types.KeyboardButton("СУББОТА_7В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn7vP, btn7vV, btn7vS, btn7vCH, btn7vPT,btn7vSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)
    elif (message.text == "ПОНЕДЕЛЬНИК_7В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/англ.яз/124/115\n2️⃣13:35:14:15/разговор/317\n3️⃣14:25-15:05/русс.яз/303\n4️⃣15:15-15:55/матем/318\n5️⃣16:05-16:45/литер/303\n6️⃣16:55-17:35/родной/308/107/224\n7️⃣17:45-18:25/ИЗО/208\nℹВнеурочка\n11:05/ю.армия/114\n")
    elif (message.text == "ВТОРНИК_7В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/\n2️⃣13:35:14:15/физика/307\n3️⃣14:25-15:05/матем/318\n4️⃣15:15-15:55/геогр/219\n5️⃣16:05-16:45/история/205\n6️⃣16:55-17:35/русс.яз/121\n7️⃣17:45-18:25/общ/205\n8️⃣18:35-19:15/физ-ра/210ℹВнеурочка\n10:10/мат/205\n12:50/ч.грам/223\n")
    elif (message.text == "СРЕДА_7В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/геогр/219\n2️⃣13:35:14:15/матем/318\n3️⃣14:25-15:05/история/205\n4️⃣15:15-15:55/англ.яз/124/116\n5️⃣16:05-16:45/технолог./124/114\n6️⃣16:55-17:35/технолог./124/114\n7️⃣17:45-18:25/физ-ра/210\n8️⃣18:35-19:15/ВД ФП/210\n")
    elif (message.text == "ЧЕТВЕРГ_7В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/\n2️⃣13:35:14:15/биология/217\n3️⃣14:25-15:05/матем/318\n4️⃣15:15-15:55/русс.яз/121\n5️⃣16:05-16:45/литер/121\n6️⃣16:55-17:35/инфор/309/318\n7️⃣17:45-18:25/родной/308/107/224\n8️⃣18:35-19:15/род.лит/308/107/224\nℹВнеурочка\n11:05/англ/116\n")
    elif (message.text == "ПЯТНИЦА_7В"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/физика/317\n2️⃣13:35:14:15/матем/318\n3️⃣14:25-15:05/матем/318\n4️⃣15:15-15:55/русс.яз/121\n5️⃣16:05-16:45/музыка/224\n6️⃣16:55-17:35/англ.яз/107/116\nℹВнеурочка\n10:00/черч/209\n10:40/черч/209\n12:00/мат/318\n12:00/англ/116\n14:30/родничок/223\n")
    elif (message.text == "СУББОТА_7В"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n16:10/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "7Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_7Г")
        btn7gV = types.KeyboardButton("ВТОРНИК_7Г")
        btn7gS = types.KeyboardButton("СРЕДА_7Г")
        btn7gCH = types.KeyboardButton("ЧЕТВЕРГ_7Г")
        btn7gPT = types.KeyboardButton("ПЯТНИЦА_7Г")
        btn7gSYB  = types.KeyboardButton("СУББОТА_7Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn7gP, btn7gV, btn7gS, btn7gCH, btn7gPT,btn7gSYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_7Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/\n2️⃣13:35:14:15/разговор/106\n3️⃣14:25-15:05/матем/107\n4️⃣15:15-15:55/русс.яз/303\n5️⃣16:05-16:45/геогр/219\n6️⃣16:55-17:35/родной/308/106\n7️⃣17:45-18:25/инфор/309\n8️⃣18:35-19:15/ВД ФП/210\nℹВнеурочка\n10:10/ю.фин/221\n11:05/ю.армия/114\n12:50/ч.грам/205\n")
    elif (message.text == "ВТОРНИК_7Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/\n2️⃣13:35:14:15/Матем/108\n3️⃣14:25-15:05/технолог/124\n4️⃣15:15-15:55/технолог/124\n5️⃣16:05-16:45/русс.яз/221\n6️⃣16:55-17:35/литер/221\n7️⃣17:45-18:25/ИЗО/208\n8️⃣18:35-19:15/биолог/219\nℹВнеурочка\n11:05/мат/205\n")
    elif (message.text == "СРЕДА_7Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/литер/217\n2️⃣13:35:14:15/матем/221\n3️⃣14:25-15:05/матем/221\n4️⃣15:15-15:55/музыка/224\n5️⃣16:05-16:45/физика/307\n6️⃣16:55-17:35/англ.яз/116\n7️⃣17:45-18:25/физ-ра/210\n8️⃣18:35-19:15/\nℹВнеурочка\n10:10/ю.фин/318\n")
    elif (message.text == "ЧЕТВЕРГ_7Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/\n2️⃣13:35:14:15/матем/308\n3️⃣14:25-15:05/русс.яз/121\n4️⃣15:15-15:55/геогр/219\n5️⃣16:05-16:45/история/221\n6️⃣16:55-17:35/англ.яз/116\n7️⃣17:45-18:25/родной/308/106\n8️⃣18:35-19:15/род.лит/308/106\nℹВнеурочка\n12:00/англ/116\n")
    elif (message.text == "ПЯТНИЦА_7Г"):
        bot.send_message(message.chat.id, "1️⃣12:50-13:30/общ/221\n2️⃣13:35:14:15/матем/116\n3️⃣14:25-15:05/русс.яз/121\n4️⃣15:15-15:55/история/213\n5️⃣16:05-16:45/англ.яз/116\n6️⃣16:55-17:35/физика/307\n7️⃣17:45-18:25/физ-ра/210\n8️⃣18:35-19:15/\nℹВнеурочка\n10:00/черч/209\n10:40/черч/209\n14:30/родничок/223\n")
    elif (message.text == "СУББОТА_7Г"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n16:10/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "8А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn8aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_8А")
        btn8aV = types.KeyboardButton("ВТОРНИК_8А")
        btn8aS = types.KeyboardButton("СРЕДА_8А")
        btn8aCH = types.KeyboardButton("ЧЕТВЕРГ_8А")
        btn8aPT = types.KeyboardButton("ПЯТНИЦА_8А")
        btn8aSYB = types.KeyboardButton("СУББОТА_8А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn8aP, btn8aV, btn8aS, btn8aCH, btn8aPT,btn8aSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_8А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/217\n2️⃣9:20-10:00/рус.яз/124\n3️⃣10:10-10:50/матем/217\n4️⃣11:05-11:45/химия/317\n5️⃣12:00-12:40/англ.яз/217\n6️⃣12:50-13:30/обж/121\n7️⃣13:35-14:15/литер/217\nℹ️Внеурочка\n15:00/юнармия/121\n16:00/музей/105\n16:00/ю.турист\n19:00/волейбол/210\n")
    elif (message.text == "ВТОРНИК_8А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/217\n2️⃣9:20-10:00/история/318\n3️⃣10:10-10:50/родной/308/316\n4️⃣11:05-11:45/род.лит/308/316\n5️⃣12:00-12:40/биология/325\n6️⃣12:50-13:30/география/219\n7️⃣13:35-14:15/музыка/224\n")
    elif (message.text == "СРЕДА_8А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/124\n2️⃣9:20-10:00/история/205\n3️⃣10:10-10:50/матем/217\n4️⃣11:05-11:45/химия/317\n5️⃣12:00-12:40/физика/307\n6️⃣12:50-13:30/англ.яз/106\n7️⃣13:35-14:15/физ-ра/210\nℹВнеурочка\n14:15/ч.грам/107\n14:30/химия/317\n15:15/Eng/217\n16:00/чертеж/209\n")
    elif (message.text == "ЧЕТВЕРГ_8А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/биология/315\n2️⃣9:20-10:00/матем/217\n3️⃣10:10-10:50/физика/307\n4️⃣11:05-11:45/матем/217\n5️⃣12:00-12:40/география/219\n6️⃣12:50-13:30/труды/124\n7️⃣13:35-14:15/инфор/309\nℹВнеурочка\n14.25/ю.финнанс/315\n14:25/матем/219\n16.05/геогр/219\n12.50/баш.яз/223\n")
    elif (message.text == "ПЯТНИЦА_8А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/124\n2️⃣9:20-10:00/литер/221\n3️⃣10:10-10:50/матем/227\n4️⃣11:05-11:45/англ.яз/107\n5️⃣12:00-12:40/общ/205\n6️⃣12:50-13:30/физ-ра/210\n7️⃣13:35-14:15/родной/308/309\n8️⃣14:25-15:05/ВД ФП\nℹВнеурочка\n17:00/юнкор/105 \n")
    elif (message.text == "СУББОТА_8А"):
        bot.send_message(message.chat.id, "ℹВнеурочка\n11.20/обж/121 \n13.30/инфо/309 \n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "8Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn8bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_8Б")
        btn8bV = types.KeyboardButton("ВТОРНИК_8Б")
        btn8bS = types.KeyboardButton("СРЕДА_8Б")
        btn8bCH = types.KeyboardButton("ЧЕТВЕРГ_8Б")
        btn8bPT = types.KeyboardButton("ПЯТНИЦА_8Б")
        btn8bSYB = types.KeyboardButton("СУББОТА_8Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn8bP, btn8bV, btn8bS, btn8bCH, btn8bPT,btn8bSYB,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_8Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/224\n2️⃣9:20-10:00/рус.яз/224\n3️⃣10:10-10:50/литер/224\n4️⃣11:05-11:45/матем/305\n5️⃣12:00-12:40/музыка/224\n6️⃣12:50-13:30/история/308\n7️⃣13:35-14:15/англ.яз/116\n")
    elif (message.text == "ВТОРНИК_8Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/биология/315\n2️⃣9:20-10:00/рус.яз/224\n3️⃣10:10-10:50/родной/224/107\n4️⃣11:05-11:45/род.лит/224/107\n5️⃣12:00-12:40/матем/305\n6️⃣12:50-13:30/англ.яз/116\n7️⃣13:35-14:15/физ-ра/210\n")
    elif (message.text == "СРЕДА_8Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физика/307\n2️⃣9:20-10:00/история/224\n3️⃣10:10-10:50/матем/305\n4️⃣11:05-11:45/матем/305\n5️⃣12:00-12:40/химия/317\n6️⃣12:50-13:30/общ/205\n7️⃣13:35-14:15/география/219\nℹВнеурочка\n14:30/химия/317\n16:00/чертеж/209\n")
    elif (message.text == "ЧЕТВЕРГ_8Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ОБЖ/121\n2️⃣9:20-10:00/физ-ра/210\n3️⃣10:10-10:50/труды/124\n4️⃣11:05-11:45/биология/315\n5️⃣12:00-12:40/матем/305\n6️⃣12:50-13:30/англ.яз/116\n7️⃣13:35-14:15/география/219\n8️⃣14:25-15:05/ ВД ФП\nℹВнеурочка\n14:25/ю.финанс /315\n16:05/география/219\n")
    elif (message.text == "ПЯТНИЦА_8Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/инфор/309\n2️⃣9:20-10:00/матем/305\n3️⃣10:10-10:50/физика/307\n4️⃣11:05-11:45/химия/317\n5️⃣12:00-12:40/рус.яз/224\n6️⃣12:50-13:30/литер/225\n7️⃣13:35-14:15/родной/114/107\nℹВнеурочка\n16:40/юнкор/105\n16:05/ю.турист/114\n")
    elif (message.text =="СУББОТА_8Б"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n12:00/обж/121 \n13:30/инф/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "8В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn8vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_8В")
        btn8vV = types.KeyboardButton("ВТОРНИК_8В")
        btn8vS = types.KeyboardButton("СРЕДА_8В")
        btn8vCH = types.KeyboardButton("ЧЕТВЕРГ_8В")
        btn8vPT = types.KeyboardButton("ПЯТНИЦА_8В")
        btn8vSYB = types.KeyboardButton("СУББОТА_8В")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn8vP, btn8vV, btn8vS, btn8vCH, btn8vPT,btn8vSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_8В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/205\n2️⃣9:20-10:00/история/205\n3️⃣10:10-10:50/матем/304\n4️⃣11:05-11:45/англ/320/309\n5️⃣12:00-12:40/география/219\n6️⃣12:50-13:30/рус.яз/303\n7️⃣13:35-14:15/англ/322/инфор/309\n8️⃣14:25-15:05/ВД ФП/210\nℹВнеурочка\n15:35/юнармия/121\n17:40/юнкор/105\n20:00/волейбол/210\n")
    elif (message.text == "ВТОРНИК_8В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физ-ра/210\n2️⃣9:20-10:00/биология/315\n3️⃣10:10-10:50/родной/124/107\n4️⃣11:05-11:45/род.лит/124/107\n5️⃣12:00-12:40/матем/304\n6️⃣12:50-13:30/матем/304\n7️⃣13:35-14:15/труды/114\nℹВнеурочка\n16:55/чертеж/208\n14:25/матем/304\n")
    elif (message.text == "СРЕДА_8В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/химия/317\n2️⃣9:20-10:00/рус.яз/303\3️⃣10:10-10:50/англ.яз/322/320\n4️⃣11:05-11:45/литер/303\n5️⃣12:00-12:40/матем/304\n6️⃣12:50-13:30/история/317\n7️⃣13:35-14:15/музыка/224\n8️⃣14:25-15:05/ВД ФП\nℹВнеурочка\n15:15/English/322\n16:00/музей/105\n17:40/драма/225\n15:20/химия/317\n")
    elif (message.text == "ЧЕТВЕРГ_8В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физ-ра/210\n2️⃣9:20-10:00/биология/315\n3️⃣10:10-10:50/рус.яз/303\n4️⃣11:05-11:45/география/219\n5️⃣12:00-12:40/физика/307\n6️⃣12:50-13:30/матем/304\n7️⃣13:35-14:15/общ/317\nℹВнеурочка\n15:15/ю.финанс/315\n15:15/ю.армия/121\n16:55/география/219\n")
    elif (message.text == "ПЯТНИЦА_8В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/химия/317\n2️⃣9:20-10:00/матем/304\n3️⃣10:10-10:50/ОБЖ/121\n4️⃣11:05-11:45/физика/307\n5️⃣12:00-12:40/англ.яз/322/320\n6️⃣12:50-13:30/литер/315\n7️⃣13:35-14:15/родной/303/107\nℹВнеурочка\n14:25/English/320\n16:05/ю.туристы/114\n")
    elif (message.text == "СУББОТА_8В"):
        bot.send_message(message.chat.id, "ℹВнеурочка\n12:40/обж/121\n14:10/инф/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "8Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn8gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_8Г")
        btn8gV = types.KeyboardButton("ВТОРНИК_8Г")
        btn8gS = types.KeyboardButton("СРЕДА_8Г")
        btn8gCH = types.KeyboardButton("ЧЕТВЕРГ_8Г")
        btn8gPT = types.KeyboardButton("ПЯТНИЦА_8Г")
        btn8gSYB = types.KeyboardButton("СУББОТА_8Г")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn8gP, btn8gV, btn8gS, btn8gCH, btn8gPT,btn8gSYB ,back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_8Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/305\n2️⃣9:20-10:00/матем/305\n3️⃣10:10-10:50/химия/317\n4️⃣11:05-11:45/география/219\n5️⃣12:00-12:40/англ.яз/320/инфор/309\n6️⃣12:50-13:30/англ.яз/322/инфор/309\n7️⃣13:35-14:15/музыка /224\nℹВнеурочка\n14:25/English/320\n16:10/юнарм/121\n20:00/волейбол\n")
    elif (message.text == "ВТОРНИК_8Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/305\n2️⃣9:20-10:00/физ-ра/210\n3️⃣10:10-10:50/родной/308/107/121\n4️⃣11:05-11:45/род.лит/308/107/121\n5️⃣12:00-12:40/рус.яз/303\n6️⃣12:50-13:30/литер/303\n7️⃣13:35-14:15/биология/315\nℹВнеурочка\n16:55/чертеж/208\n14:25/матем/304\n")
    elif (message.text == "СРЕДА_8Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/305\n2️⃣9:20-10:00/физика/307\n3️⃣10:10-10:50/рус.яз/303\n4️⃣11:05-11:45/англ/320/322\n5️⃣12:00-12:40/история /219\n6️⃣12:50-13:30/физ-ра/210\n7️⃣13:35-14:15/биология/315\n8️⃣14:25-15:05/ВД ФП/210\nℹВнеурочка\n15:15/English/322\n15:20/химия/317\n16:00/музей/105\n17:40/юнкор/105\n16:20/драма/225\n")
    elif (message.text == "ЧЕТВЕРГ_8Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/матем/305\n2️⃣9:20-10:00/ОБЖ/121\n3️⃣10:10-10:50/география/219\n4️⃣11:05-11:45/матем/305\n5️⃣12:00-12:40/рус.яз/303\n6️⃣12:50-13:30/общ/208\n7️⃣13:35-14:15/литер/303\nℹВнеурочка\n15:15/ю.финанс/315\n15:15/ю.армия/223\n16:55/геог/219\n")
    elif (message.text == "ПЯТНИЦА_8Г"):
        bot.send_message(message.chat.id,"1️⃣8:30-9:10/физика/307\n2️⃣9:20-10:00/история/318\n3️⃣10:10-10:50/химия/317\n4️⃣11:05-11:45/матем/305\n5️⃣12:00-12:40/труды/124/114\n6️⃣12:50-13:30/англ.яз/320/322\n7️⃣13:35-14:15/родной/308/107/205\nℹВнеурочка\n16:05/ю.туристы/114\n")
    elif (message.text == "СУББОТА_8Г"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n13:20/обж/121\n14:10/инф/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "9А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn9aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_9А")
        btn9aV = types.KeyboardButton("ВТОРНИК_9А")
        btn9aS = types.KeyboardButton("СРЕДА_9А")
        btn9aCH = types.KeyboardButton("ЧЕТВЕРГ_9А")
        btn9aPT = types.KeyboardButton("ПЯТНИЦА_9А")
        btn9aSYB = types.KeyboardButton("СУББОТА_9А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn9aP, btn9aV, btn9aS, btn9aCH, btn9aPT,btn9aSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_9А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/307\n2️⃣9:20-10:00/рус.яз/303\n3️⃣10:10-10:50/англ.яз/322/106\n4️⃣11:05-11:45/математика/121\n5️⃣12:00-12:40/история/318\n6️⃣12:50-13:30/биология/315\n7️⃣13:35-14:15/литература/303\nℹВнеурочка\n15:15/физика/217\n")
    elif (message.text == "ВТОРНИК_9А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/химия/317\n2️⃣9:20-10:00/англ.яз/322/106\n3️⃣10:10-10:50/математика/304\n 4️⃣11:05-11:45/родной язык/303\n5️⃣12:00-12:40/физика/307\n6️⃣12:50-13:30/математика/305\n7️⃣13:35-14:15/информатика/309/318\nℹВнеурочка\n13:35/ю.армия/223\n14:25/биология/316\n15:15/инфа/318\n16:00/химия/317\n")
    elif (message.text == "СРЕДА_9А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/318\n2️⃣9:20-10:00/география/219\n 3️⃣10:10-10:50/обществознание/219\n4️⃣11:05-11:45/история219\n5️⃣12:00-12:40/физра/210\n6️⃣12:50-13:30/математика/305\nℹ13:35/англ/322\n13:35/право/223\n14:25/англ/308\n14:25/башкирский/217\n14:25/геог/114\n15:15/гео/114\n")
    elif (message.text == "ЧЕТВЕРГ_9А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физика/307\n 2️⃣9:20-10:00/математика/205\n3️⃣10:10-10:50/англ.яз/322/107\n4️⃣11:05-11:45/химия/317\n5️⃣12:00-12:40/обж/121\n6️⃣12:50-13:30/география219\n7️⃣13:35-14:15/биология315\nℹВнеурочка\n14:25/англ/302\n")
    elif (message.text == "ПЯТНИЦА_9А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/224\n2️⃣9:20-10:00/литература/224\n3️⃣10:10-10:50/физра/210\n 4️⃣11:05-11:45/математика/205\n 5️⃣12:00-12:40/физика/307\n 6️⃣12:50-13:30/технология/114/124\n7️⃣13:35-14:15/род.лит/315\n")
    elif (message.text == "СУББОТА_9А"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n9:10/мат/308\n10:00/ч.грам/302\n12:00/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "9Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn9bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_9Б")
        btn9bV = types.KeyboardButton("ВТОРНИК_9Б")
        btn9bS = types.KeyboardButton("СРЕДА_9Б")
        btn9bCH = types.KeyboardButton("ЧЕТВЕРГ_9Б")
        btn9bPT = types.KeyboardButton("ПЯТНИЦА_9Б")
        btn9bSYB = types.KeyboardButton("СУББОТА_9Б")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn9bP, btn9bV, btn9bS, btn9bCH, btn9bPT,btn9bSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_9Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/320\n2️⃣9:20-10:00/математика/107\n3️⃣10:10-10:50/технология/124\n4️⃣11:05-11:45/рус.яз/124\n5️⃣12:00-12:40/биология/315\n6️⃣12:50-13:30/география/219\n7️⃣13:35-14:15/англ.яз/124\nℹВнеурочка\n15:15/физика/217\n16:00/чертеж/208\n")
    elif (message.text == "ВТОРНИК_9Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/208\n2️⃣9:20-10:00/литература/208\n3️⃣10:10-10:50/химия/317\n4️⃣11:05-11:45/физика/217\n5️⃣12:00-12:40/математика/107\n6️⃣12:50-13:30/история/317\n7️⃣13:35-14:15/обществознание/317\nℹВнеурочка\n13:35/ю.армия/223\n14:25/биология/316\n14:25/право/317\n16:00/химия/317\n")
    elif (message.text == "СРЕДА_9Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/география/219\n2️⃣9:20-10:00/физика/217\n3️⃣10:10-10:50/англ.яз/315\n4️⃣11:05-11:45/математика/315\n5️⃣12:00-12:40/биология/315\n6️⃣12:50-13:30/родной язык/308/107/309\n7️⃣13:35-14:15/род.лит/308/107/309\nℹВнеурочка\n14:25/башкирский/217\n14:25/геог/114\n15:15/геог/114\n17:40/драма/225\n")
    elif (message.text == "ЧЕТВЕРГ_9Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/303\n2️⃣9:20-10:00/литература/303\n3️⃣10:10-10:50/химия/317\n4️⃣11:05-11:45/обж/121\n5️⃣12:00-12:40/математика/308\n6️⃣12:50-13:30/англ.яз/315\nℹВнеурочка\n13:25/профор/320\n16:00/англ/106\n")
    elif (message.text == "ПЯТНИЦА_9Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/история\n2️⃣9:20-10:00/информатика\n3️⃣10:10-10:50/математика\n4️⃣11:05-11:45/математика\n5️⃣12:00-12:40/физика\n6️⃣12:50-13:30/физика\n7️⃣13:35-14:15/физра\nℹВнеурочка\n14:25/ю.армия/114\n")
    elif (message.text == "СУББОТА_9Б"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/мат/304\n10:00/ч.грам/302\n11:00/ч.грам/302\n12:00/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "9В"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn9vP = types.KeyboardButton("ПОНЕДЕЛЬНИК_9В")
        btn9vV = types.KeyboardButton("ВТОРНИК_9В")
        btn9vS = types.KeyboardButton("СРЕДА_9В")
        btn9vCH = types.KeyboardButton("ЧЕТВЕРГ_9В")
        btn9vPT = types.KeyboardButton("ПЯТНИЦА_9В")
        btn9vSYB = types.KeyboardButton("СУББОТА_9А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn9vP, btn9vV, btn9vS, btn9vCH, btn9vPT,btn9vSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_9В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/107\n2️⃣9:20-10:00/физика/217\n3️⃣10:10-10:50/математика/107\n4️⃣11:05-11:45/биология/315\n5️⃣12:00-12:40/англ.яз/106\n6️⃣12:50-13:30/обществознание/318\n 7️⃣13:35-14:15/география/219\nℹВнеурочка\n14:25/право/219\n15:15/физика/217\n")
    elif (message.text == "ВТОРНИК_9В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/история/318\n2️⃣9:20-10:00/физика/217\n3️⃣10:10-10:50/математика/221\n4️⃣11:05-11:45/химия/317\n5️⃣12:00-12:40/родной/121\n6️⃣12:50-13:30/биология/315\n7️⃣13:35-14:15/география/219\nℹВнеурочка\n14:25/биология/316\n15:15/инфа/318\n16:00/химия/317\n")
    elif (message.text == "СРЕДА_9В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ рус.яз/121\n2️⃣9:20-10:00/англ.яз/106\n3️⃣10:10-10:50/математика/304\n4️⃣11:05-11:45/физика/217\n5️⃣12:00-12:40/литература/121\n6️⃣12:50-13:30/физра/210\nℹВнеурочка\n13:35/профор/223\n14:25/башкирский/217\n14:25/геог/114\n15:15/гео/114\n15:15/ч.грам/121\n15:15/англ/106\n16:00/чертеж/208\n")
    elif (message.text == "ЧЕТВЕРГ_9В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/история/205\n2️⃣9:20-10:00/химия/317\n3️⃣10:10-10:50/математика/308\n4️⃣11:05-11:45/рус.яз/124\n5️⃣12:00-12:40/литература/124\n6️⃣12:50-13:30/математика/308\n7️⃣13:35-14:15/род.лит/205\nℹВнеурочка\n13:35/ю.армия223\n")
    elif (message.text == "ПЯТНИЦА_9В"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/англ.яз/106\n2️⃣9:20-10:00/математика/208\n3️⃣10:10-10:50/рус.яз/221\n4️⃣11:05-11:45/обж/121\n5️⃣12:00-12:40/физра/210\n6️⃣12:50-13:30/информатика/318\n7️⃣13:35-14:15/технология/124\n")
    elif (message.text == "СУББОТА_9В"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/ч.грам/302\n10:50/мат/304\n12:00/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "9Г"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn9gP = types.KeyboardButton("ПОНЕДЕЛЬНИК_9Г")
        btn9gV= types.KeyboardButton("ВТОРНИК_9Г")
        btn9gS = types.KeyboardButton("СРЕДА_9Г")
        btn9gCH = types.KeyboardButton("ЧЕТВЕРГ_9Г")
        btn9gPT = types.KeyboardButton("ПЯТНИЦА_9Г")
        btn9gSYB = types.KeyboardButton("СУББОТА_9А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn9gP, btn9gV, btn9gS, btn9gCH, btn9gPT,btn9gSYB, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_9Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/309\n 2️⃣9:20-10:00/обж/121\n3️⃣10:10-10:50/биология/315\n4️⃣11:05-11:45/физра/210\n5️⃣12:00-12:40/математика/208\n6️⃣12:50-13:30/англ.яз/107/106\nℹВнеурочка\n13:35/профор/223\n14:25/ю.армия/114\n15:15/физика/217\n")
    elif (message.text == "ВТОРНИК_9Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физра/210\n2️⃣9:20-10:00/химия/317\n3️⃣10:10-10:50/история/318\n4️⃣11:05-11:45/география/219\n5️⃣12:00-12:40/физика/217\n6️⃣12:50-13:30/математика/309\n7️⃣13:35-14:15/рус.яз/121\nℹВнеурочка\n14:25/биология/316\n16:00/химия/317\n")
    elif (message.text == "СРЕДА_9Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика/308\n2️⃣9:20-10:00/рус.яз/121\n3️⃣10:10-10:50/литература/121\n4️⃣11:05-11:45/англ.яз/124/106\n5️⃣12:00-12:40/физика/217\n6️⃣12:50-13:30/родной/121/308/107\n7️⃣13:35-14:15/род.лит/121/308/107\nℹВнеурочка\n14:25/англ/302\n14:25/геог/114\n14:25/башкирский/217\n15:15/геог/114\n15:15/англ/106\n16:05/ч.грам/219\n16:05/инфа/318\n")
    elif (message.text == "ЧЕТВЕРГ_9Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/химия/317\n2️⃣9:20-10:00/математика/308\n3️⃣10:10-10:50/биология/315\n4️⃣11:05-11:45/англ.яз/107/106\n5️⃣12:00-12:40/история/317\n6️⃣12:50-13:30/обществознание/317\n 7️⃣13:35-14:15/технология/114/124\nℹВнеурочка\n14:25/англ/302\n16:15/право/315\n")
    elif (message.text == "ПЯТНИЦА_9Г"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/121\n2️⃣9:20-10:00/литература/121\n3️⃣10:10-10:50/информатика/309/318\n4️⃣11:05-11:45/физика/217\n5️⃣12:00-12:40/математика/208\n6️⃣12:50-13:30/математика/217\n7️⃣13:35-14:15/география/219\n")
    elif(message.text == "СУББОТА_9Г"):
        bot.send_message(message.chat.id,"ℹВнеурочка\n10:00/ч.грам/302\n11:40/мат/304\n12:00/инфа/309\n12:40/инфа/309\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "10А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn10aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_10А")
        btn10aV = types.KeyboardButton("ВТОРНИК_10А")
        btn10aS = types.KeyboardButton("СРЕДА_10А")
        btn10aCH = types.KeyboardButton("ЧЕТВЕРГ_10А")
        btn10aPT = types.KeyboardButton("ПЯТНИЦА_10А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn10aP, btn10aV, btn10aS, btn10aCH, btn10aPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_10А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/303\n2️⃣9:20-10:00/англ.яз/320/инф/309\n3️⃣10:10-10:50/география/219\n4️⃣11:05-11:45/физика/307\n5️⃣12:00-12:40/история/221\n6️⃣12:50-13:30/математика/305\n7️⃣13:35-14:15/ЭК общ/221\nℹВнеурочка\n15:15/башкирский/308\n16:00/англ/320/107\n")
    elif (message.text == "ВТОРНИК_10А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/рус.яз/303\n2️⃣9:20-10:00/математика/305\n3️⃣10:10-10:50/математика/305\n4️⃣11:05-11:45/физика/307\n5️⃣12:00-12:40/физра/210\n6️⃣12:50-13:30/биология/307\n7️⃣13:35-14:15/родной/303\n8⃣14:25-15:05/ЭК инф/309\nℹВнеурочка\n14:25/биология/316\n")
    elif (message.text == "СРЕДА_10А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/литература/303\n2️⃣9:20-10:00/обществознание/221\n3️⃣10:10-10:50/химия/317\n4️⃣11:05-11:45/история/221\n5️⃣12:00-12:40/математика/305\n6️⃣12:50-13:30/англ.яз/208/320\n7️⃣13:35-14:15/ЭК химия/317\nℹВнеурочка\n15:40/право/221\n")
    elif (message.text == "ЧЕТВЕРГ_10А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ЭК биология/219\n2️⃣9:20-10:00/математика/305\n3️⃣10:10-10:50/англ.яз/106/инф/309\n4️⃣11:05-11:45/общ/221\n5️⃣12:00-12:40/физра/210\n6️⃣12:50-13:30/обж/121\n7️⃣13:35-14:15/ЭК история/221\nℹВнеурочка\n14:25/этикет/302\n15:00/гов.публ/303\n")
    elif (message.text == "ПЯТНИЦА_10А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/Литер/303\n2️⃣9:20-10:00/химия/317\n3️⃣10:10-10:50/биология/219\n4️⃣11:05-11:45/англ.яз/320/инф/309\n5️⃣12:00-12:40/математика/305\n6️⃣12:50-13:30/англ.яз/106/инф/309\n7️⃣13:35-14:15/ЭК физика/307\nℹВнеурочка\n14:30/хим/317\n16:00/шахматы/208\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "10Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn10bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_10Б")
        btn10bV = types.KeyboardButton("ВТОРНИК_10Б")
        btn10bS = types.KeyboardButton("СРЕДА_10Б")
        btn10bCH = types.KeyboardButton("ЧЕТВЕРГ_10Б")
        btn10bPT = types.KeyboardButton("ПЯТНИЦА_10Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn10bP, btn10bV, btn10bS, btn10bCH, btn10bPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_10Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/302\n2️⃣9:20-10:00/математика/304\n3️⃣10:10-10:50/англ.яз/320/инф/309\n4️⃣11:05-11:45/общ/221\n5️⃣12:00-12:40/химия/317\n6️⃣12:50-13:30/история/221\n7️⃣13:35-14:15/литер/302ℹ️Внеурочка\n15:15/башкирский/308\n")
    elif (message.text == "ВТОРНИК_10Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ЭК инф/309\n2️⃣9:20-10:00/рус.яз/302\n3️⃣10:10-10:50/физика/307\n4️⃣11:05-11:45/математика/304\n5️⃣12:00-12:40/родной/302\n6️⃣12:50-13:30/физра/210\n7️⃣13:35-14:15/биология/124\n8⃣14:25-15:05/география/219\n")
    elif (message.text == "СРЕДА_10Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ЭК общ/221\n2️⃣9:20-10:00/литература/302\n3️⃣10:10-10:50/обществознание/221\n4️⃣11:05-11:45/математика/304\n5️⃣12:00-12:40/англ.яз/320/106\n6️⃣12:50-13:30/история/221\n7️⃣13:35-14:15/ЭК химия/317\nℹВнеурочка\n14:00/биол/221\n15:00/право/221\n")
    elif (message.text == "ЧЕТВЕРГ_10Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/ЭК биология/219\n2️⃣9:20-10:00/англ.яз/106/309\n3️⃣10:10-10:50/рус.яз/302\n4️⃣11:05-11:45/биология/308\n5️⃣12:00-12:40/математика/304\n6️⃣12:50-13:30/физра/210\n7️⃣13:35-14:15/ЭК история/221\nℹВнеурочка\n15:15/англ/106\n15:30/этикет/203\n16:20/гов.пуб/302\n")
    elif (message.text == "ПЯТНИЦА_10Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика/304\n2️⃣9:20-10:00/физика/307\n3️⃣10:10-10:50/англ.яз/320/106\n4️⃣11:05-11:45/математика/304\n5️⃣12:00-12:40/химия/317\n6️⃣12:50-13:30/обж/121\n7️⃣13:35-14:15/ЭК физика/307\nℹВнеурочка\n15:20/хим/317\n16:00/шахматы/208\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "11А"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11aP = types.KeyboardButton("ПОНЕДЕЛЬНИК_11А")
        btn11aV = types.KeyboardButton("ВТОРНИК_11А")
        btn11aS = types.KeyboardButton("СРЕДА_11А")
        btn11aCH = types.KeyboardButton("ЧЕТВЕРГ_11А")
        btn11aPT = types.KeyboardButton("ПЯТНИЦА_11А")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11aP, btn11aV, btn11aS, btn11aCH, btn11aPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_11А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/308\n2️⃣9:20-10:00/химия/317\n3️⃣10:10-10:50/рус.яз/303\n4️⃣11:05-11:45/математика/304\n5️⃣12:00-12:40/литература/303\n6️⃣12:50-13:30/физра/210\n7️⃣13:35-14:15/обж121\nℹВнеурочка\n14:30/хим/317\n")
    elif (message.text == "ВТОРНИК_11А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/физика/307\n2️⃣9:20-10:00/математика/304\n3️⃣10:10-10:50/родной/303\n4️⃣11:05-11:45/инф/309/318\n5️⃣12:00-12:40/общ/205\n6️⃣12:50-13:30/общ/205\n7️⃣13:35-14:15/литер/221\n")
    elif (message.text == "СРЕДА_11А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/англ.яз/106/124\n2️⃣9:20-10:00/математика/304\n3️⃣10:10-10:50/история/205\n4️⃣11:05-11:45/история/205\n5️⃣12:00-12:40/общ/205\n6️⃣12:50-13:30/астрономия/307\n7️⃣13:35-14:15/право/205\nℹВнеурочка\n14:25/матем/304\n14:25-15:45/биол/309\n")
    elif (message.text == "ЧЕТВЕРГ_11А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/англ.яз/106/116\n2️⃣9:20-10:00/физика/307\n3️⃣10:10-10:50/математика/304\n4️⃣11:05-11:45/математика/303\n5️⃣12:00-12:40/история/205\n6️⃣12:50-13:30/литер/303\n7️⃣13:35-14:15/физра/210\nℹВнеурочка\n15:15/англ/106\n15:15/башкирский/308\n")
    elif (message.text == "ПЯТНИЦА_11А"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/биология/315\n2️⃣9:20-10:00/англ.яз/106/107\n3️⃣10:10-10:50/рус.яз/315\n4️⃣11:05-11:45/литер/315\n5️⃣12:00-12:40/литер/315\n6️⃣12:50-13:30/математика/304\n7️⃣13:35-14:15/география/317\nℹВнеурочка\n14:25/право/205\n15:15/истор/205\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "11Б"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11bP = types.KeyboardButton("ПОНЕДЕЛЬНИК_11Б")
        btn11bV = types.KeyboardButton("ВТОРНИК_11Б")
        btn11bS = types.KeyboardButton("СРЕДА_11Б")
        btn11bCH = types.KeyboardButton("ЧЕТВЕРГ_11Б")
        btn11bPT = types.KeyboardButton("ПЯТНИЦА_11Б")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11bP, btn11bV, btn11bS, btn11bCH, btn11bPT, back)
        bot.send_message(message.chat.id, text="Выбрать день нужного расписания", reply_markup=markup)

    elif (message.text == "ПОНЕДЕЛЬНИК_11Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/разгов/304\n2️⃣9:20-10:00/физика/307\n3️⃣10:10-10:50/инф/318\4️⃣11:05-11:45/история/318\n5️⃣12:00-12:40/математика/304\n6️⃣12:50-13:30/химия/317\n7️⃣13:35-14:15/общ/318\nℹВнеурочка\n14:25/инфа/304\n")
    elif (message.text == "ВТОРНИК_11Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика/304\n2️⃣9:20-10:00/физика/307\n3️⃣10:10-10:50/биология/315\n4️⃣11:05-11:45/физра/210\n5️⃣12:00-12:40/рус.яз/308\n6️⃣12:50-13:30/литер/308\n7️⃣13:35-14:15/англ.яз/106\n")
    elif (message.text == "СРЕДА_11Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика/304\n2️⃣9:20-10:00/химия/317\n3️⃣10:10-10:50/физика/307\n4️⃣11:05-11:45/физра/210\n5️⃣12:00-12:40/литер/303\n6️⃣12:50-13:30/инфор/318\n7️⃣13:35-14:15/астрономия/307nℹВнеурочка\n14:25/право/302\n14:25-15:45/биол/309\n")
    elif (message.text == "ЧЕТВЕРГ_11Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/математика/304\n2️⃣9:20-10:00/математика/304\n️⃣3️⃣10:10-10:50/история/205\n4️⃣11:05-11:45/общ/205\n5️⃣12:00-12:40/родной/224\n6️⃣12:50-13:30/инф/318\n7️⃣13:35-14:15/англ.яз/121\nℹВнеурочка\n14:25/мат/106\n15:15/башкирский/308\n")
    elif (message.text == "ПЯТНИЦА_11Б"):
        bot.send_message(message.chat.id, "1️⃣8:30-9:10/география/219\n2️⃣9:20-10:00/биология/315\n3️⃣10:10-10:50/математика/304\n4️⃣11:05-11:45/рус.яз/303\n5️⃣12:00-12:40/англ.яз/106\n6️⃣12:50-13:30/физика/307\n7️⃣13:35-14:15/обж/121\nℹВнеурочка\n14:25/англ/205\n")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("О боте")
        button2 = types.KeyboardButton("Я хочу узнать свое расписание")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def func(message):
    # if message.text == "Меню столовой":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     stol1 = types.KeyboardButton('Первая смена')
    #     stol2 = types.KeyboardButton('Вторая смена')
    #     back = types.KeyboardButton('Вернуться в главное меню')
    #     markup.add(stol1, stol2 ,back)
    #     bot.send_message(message.chat.id, 'приятного аппетита!', reply_markup=markup)
    # elif message.text == "О боте":
    #     bot.send_message(message.chat.id,text="Привет, Я lyceym бот! Смогу помочь тебе быстро узнать свое расписание♡ ")
    # elif message.text == "/help":
    #     bot.send_message(message.chat.id,text="Eсли у вас возникли проблемы  обратитесь к https://t.me/YarmAlsu")
    # elif(message.text =="Первая смена"):
    #     stolP1 = types.KeyboardButton("Понедельник")
    #     stolV2 = types.KeyboardButton("Вторник")
    #     stolS3 = types.KeyboardButton("Среда")
    #     stolCH4 = types.KeyboardButton("Четверг")
    #     stolPT5 = types.KeyboardButton("Пятница")
    #     markup.add(stolP1, stolV2, stolS3, stolCH4, stolPT5)
    #     bot.send_message(message.chat.id, text="Приятного аппетита!", reply_markup=markup)
    # elif (message.text == "Понедельник"):
    #     bot.send_message(message.chat.id, "банан")
    # elif (message.text == "Вернуться в главное меню"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     button1 = types.KeyboardButton("О боте")
    #     button2 = types.KeyboardButton("Я хочу узнать свое расписание")
    #     button3 = types.KeyboardButton("/help")
    #     button4 = types.KeyboardButton("меню столовой ")
    #     markup.add(button1, button2, button3, button4)
    #     bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован..")

# elif message.text == ' '
# elif massage.text == "О боте":
#         bot.send_message(massage.chat.id, "Этот бот создан для уилкщлпщлщелпоощплйьщ")
bot.polling(none_stop=True)