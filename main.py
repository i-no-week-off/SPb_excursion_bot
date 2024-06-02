import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('7459894163:AAEGdLsc8iM0OazTcuMita15abhBqTpIBpc')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}")
    sleep(2)
    bot.send_message(message.chat.id, f"Вы написали боту-экскурсоводу, готовому предложить Вам интересные"
                                      f"экскурсионные маршруты Санкт-Петербурга с аудио сопровождением. Для того, "
                                      f"чтобы начать экскурсию, воспользуйтесь командой /begin.")
    return


@bot.message_handler(commands=['begin'])
def begin(message):
    reply_markup = types.InlineKeyboardMarkup()
    reply_markup.add(types.InlineKeyboardButton("Главные улицы поэтического Петербурга", callback_data='10'))
    reply_markup.add(types.InlineKeyboardButton("Отмена", callback_data='0'))
    bot.send_message(message.chat.id, """<b>Давайте начнём экскурсию!</b>
    
<b>Во время экскурсии вы будете получать:</b>
📍 Адреса точек на нашем маршруте
📍 Файлы с аудио-сопровождением 
📍 Некоторые примечательные фотографии

<b>Для прохождения маршрута Вам могут пригодиться:</b> 
🎧 наушники
🧢 удобная одежда и обувь
🫶 хорошее настроение

<i>Маршруты рассчитаны на 1 - 1,5 часа.</i>""", parse_mode='html')
    sleep(3)
    bot.send_message(message.chat.id,
                     "Выберите один из предложенных ниже маршрутов:\n\n"
                     "<b>• Главные улицы поэтического Петербурга</b>\n"
                     "Маршрут проходит по одним из самых красивых исторических улиц Петербурга. Вы увидите известный "
                     "Таврический сад, прогуляетесь по  Кирочной и Захарьевской улицам,  дойдете до улицы Шпалерная, "
                     "далее маршрут проведёт вас по Литейному проспекту и закончится недалеко от станции метро "
                     "Площадь Восстания - на улице Жуковского.",
                     parse_mode='html', reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id)
    if callback.data == '10':
        with open("Audios/0. Welcome.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте", callback_data="11"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Наш маршрут начинается у Таврического дворца. Дайте знать, когда окажетесь там.",
                         reply_markup=reply_markup)
    if callback.data == '11':
        with open("Audios/1. The Tauride Palace.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/1. The Tauride Palace.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Таврический дворец</b>", "html")
        with open("Images/1. Architector I. E. Starov.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Архитектор И. Е. Старов</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Продолжаем!", callback_data="12"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - собственно, сам Таврический сад. "
                         "Давайте погуляем по нему. Дайте знать, когда будете готовы продолжить.",
                         reply_markup=reply_markup)
    if callback.data == '12':
        with open("Audios/2. The Tauride Garden.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        with open("Audios/2. Legends of the Tauride Garden.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)

        sleep(5)
        with open("Images/2. The Tauride Garden.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Таврический сад</b>", "html")
        with open("Images/2. The Greenhouse.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Оранжерея Таврического сада</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="13"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Чайковского, 62</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '13':
        with open("Audios/3. Marshak's apartment.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/3. Samuil Marshak.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>С. Я. Маршак</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="14"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Фурштатская, 62/9</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '14':
        with open("Audios/4. The salon of Princess Ponomoryova.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/4. Princess Sofia Ponomoryova.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Княгиня Софья Пономорёва</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="15"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Кирочная, 24</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '15':
        with open("Audios/5. Marienhof's apartment.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/5. Bak House.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Дом Бака</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="16"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Захарьевская, 23</code>. "
                         "Дайте знать, когда будете готовы продолжить.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '16':
        with open("Audios/6. The Egyptian House.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/6. The Egyptian House.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Египетский дом</b>", "html")
        with open("Images/6. Architector Michael Songailo.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Архитектор Михаил Сонгайло</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="17"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Шпалерная, 25</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '17':
        with open("Audios/7. The house of pre-trial detention.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/7. The house of pre-trial detention 1879.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Дом предварительного заключения в 1879</b>", "html")
        with open("Images/7. Nikolai Gumilev.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Н. С. Гумилёв</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="18"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Шпалерная, 18</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '18':
        with open("Audios/8. The Writers' house.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/8. The Writers' House.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Дом писателей</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="19"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Фурштатская, 5</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '19':
        with open("Audios/9. The Club 81.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/9. Boluchevsky and Kurehin in the Club 81. 1983.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>В.Болучевский и С.Курехин в Клубе 81, 1983</b>",
                           "html")
        with open("Images/9. Meeting in the Club 81.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image,
                           "<b>Собрание Товарищества экспериментального изобразительного искусства в Клубе 81</b>",
                           "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="110"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Кирочная, 8В</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '110':
        with open("Audios/10. Annenkirche.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/10. Interior.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Анненкирхе внутри</b>", "html")
        with open("Images/10. Architector Yury Felten.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Архитектор Юрий Фельтен</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="111"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Пестеля, 27</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '111':
        with open("Audios/11. Brodsky's apartment.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/11. Pestel's street.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Улица Пестеля</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Продолжаем!", callback_data="112"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута находится здесь же."
                         "Дайте знать, когда будете готовы продолжить.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '112':
        with open("Audios/12. The Poets' Workshop.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        with open("Audios/12. The Poets' Workshop. Clarification.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/12. Muruzi house.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Дом Мурузи</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="113"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Жуковского, 7-9</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '113':
        with open("Audios/13. Briks' apartment.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/13. Lilya Brik.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Лиля Брик</b>", "html")
        with open("Images/13. Briks' apartment.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Дом, в котором жили Лиля и Осип Брики</b>",
                           "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Я на месте!", callback_data="114"))
        reply_markup.add(types.InlineKeyboardButton("Прервать экскурсию", callback_data="00"))
        bot.send_message(callback.message.chat.id,
                         "Следующая точка нашего маршрута - <code>улица Маяковского, 11</code>. "
                         "Дайте знать, когда будете на месте.",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '114':
        with open("Audios/14. Kharms' apartment.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        with open("Images/14. Kharms' apartment.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Дом, в котором жил Хармс</b>", "html")
        with open("Images/14. Kharms' apartment's sheme.png", "rb") as image:
            bot.send_photo(callback.message.chat.id, image, "<b>Схема квартиры Хармса</b>", "html")
        sleep(7)
        reply_markup = types.InlineKeyboardMarkup()
        reply_markup.add(types.InlineKeyboardButton("Завершить экскурсию", callback_data="115"))
        bot.send_message(callback.message.chat.id,
                         "Эта точка последняя в нашем маршруте. Вы дошли до конца!",
                         reply_markup=reply_markup, parse_mode='html')
    if callback.data == '115':
        with open("Audios/-1. Goodbye.ogg", "rb") as audio:
            bot.send_audio(callback.message.chat.id, audio)
        sleep(5)
        bot.send_message(callback.message.chat.id,
                         "Будем рады взаимодействовать с Вами снова!")
    if callback.data == "00":
        bot.send_message(callback.message.chat.id, "Экскурсия прервана. Возвращайтесь к нам снова!")

    return


bot.polling(none_stop=True)