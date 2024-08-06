from random import choice
import sqlite3
import pip
from background import keep_alive
pip.main(['install', 'pytelegrambotapi'])
from cnfg import config
import telebot
from telebot import types
from starshaki import stud
from rassylka import text_dlya_rassylki
import json


con = sqlite3.connect('users.db', check_same_thread=False)
cursor = con.cursor()

print(1)
bot = telebot.TeleBot(config['token'])
print(2)
message_for_change = ""

with open("studi.json") as json_file:
    my_json = json.load(json_file)


@bot.message_handler(commands=["start"])
def start(message):
    print(message.chat.id, message.from_user.first_name)
    if my_json["id"].get(str(message.chat.id)) == None:
        my_json["id"].update({str(message.chat.id) : False})
        with open("studi.json", 'w') as json_file:
            json.dump(my_json, json_file, indent=4)
    print(my_json)
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    get_info = types.KeyboardButton("Получить инфу")

    key_board.add(get_info)

    name = message.from_user.first_name

    bot.send_photo(message.chat.id, photo = "https://scontent.fala8-1.fna.fbcdn.net/v/t1.18169-9/19905208_1574170009269342_1621587858715569363_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=2ZfyWV8rkDMAX9KjE6Z&_nc_ht=scontent.fala8-1.fna&oh=00_AT_U6j7l6crXDQWgmfHBi2gz2Pytu_YB1AXyI3v1pg2hlQ&oe=63255A20", caption=f"Привет {name}, мы рады что ты пользуешься нашим ботом", reply_markup=key_board)

@bot.message_handler()
def get_message(message):

    print(json.dumps(my_json, indent=4))
    global message_for_change
    if my_json['id'][str(message.chat.id)] == True:
        try:
            msg = int(message.text)
            query=f"""SELECT * from Rooms WHERE Room like {msg}"""
            query=f"""SELECT * from Rooms"""
        except:
            bot.send_message(message.chat.id, "Отправьте номер кабинета")
            return
        
        print(msg)
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return
        try:
            arr = [str(i) for i in cursor.execute(query).fetchone()]
            arr.pop()
            arr[0] = "Улица: " + arr[0]
            arr[1] = "Этаж: " + arr[1]
            s = "Ваш кабинет\n"
            s += "\n".join(arr)
        except:
            s = "Такого кабинета нет🥺"
        bot.send_message(message.chat.id, s)
        send_info_1(message=message)

        my_json['id'][str(message.chat.id)] = False


    # if message.chat.id == 478214472 and message.text == "/Рассылка":
    if message.chat.id == 784892442 and message.text == "/Рассылка":
        text = text_dlya_rassylki
        with open('studi.json') as jsn_file:
            my_jsn = json.load(jsn_file)
            for i, j in my_jsn["id"].items():
                try:
                    bot.send_message(int(i), text_dlya_rassylki)
                except:
                    # bot.send_message(-636032836, "Чет не получается")
                    bot.send_message(784892442, "Чет не получается")

    if message.text == "Привет это я Сабир. Помоги":
        print(type(message.chat.id))



    if message.text == 'Туалеты':
        text = """Чтобы тихоря посрать иди в туалет на казыбек би возле коворки

Покакать и посмотреть на красавиц это 4 этаж панфилова и абылай хана

Самый инновационный туалет на панфилова 2

Самый хреновый туалет на тб1

В туалет в который не стоит заходить - ЦЭ - переход с тб на абылайхана

На каждом этаже есть туалеты, они все нормальные:)\n\ninst\n@404alumni"""

        bot.send_message(message.chat.id, text)






#осталось сделать только input
    if message.text == 'Поиск кабинета':
        my_json['id'][str(message.chat.id)] = True
        print(my_json)
        bot.send_message(message.chat.id, 'Введите номер кабинета\n\ninst\n@404alumni')







    if message.text == 'Полезные кабинеты':
        text = """Деканат Abylai khan 2

ОР Panfilov 2
Бухгалтерия Tole bi 5

Пресс центр Kazybek bi 2

Independence hall / круглый зал Tole bi 2

Коворкинг Kazybek bi 1

Охрана Kazybek bi, аб, конец кб, проходишь дальше арки в сторону кб 0\n\ninst\n@404alumni"""

        bot.send_message(message.chat.id, text)









    if(message.text == "Получить инфу" or message.text == "Вернуться назад"):
        send_info_1(message = message)







    if message.text == 'Материал по предметам':
        keyboard_material = types.InlineKeyboardMarkup()
        item_1 = types.InlineKeyboardButton("Видео Лекции", callback_data="video_lectures")
        item_2 = types.InlineKeyboardButton("Папка с документами", callback_data="file_with_documents")

        keyboard_material.add(item_1, item_2)

        bot.send_message(message.chat.id, "Выберите что вам нужно", reply_markup=keyboard_material)






    #
    # В процесее
    #

    if message.text == "Инфа по преподам":
        bot.send_message(message.chat.id, "В процессе\n\ninst\n@404alumni")


    ne_trogat = message.from_user.first_name
    ne_trogat += '\n'
    ne_trogat += message.text

    bot.send_message(-636032836, ne_trogat)

def send_info_1(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_gaid = types.InlineKeyboardButton('Гайд перваша' , callback_data= 'guide')
    item_material = types.InlineKeyboardButton('Учебный материал' , callback_data= 'material')
    item_rooms = types.InlineKeyboardButton('Найти кабинет' , callback_data= 'rooms')
    item_was_first = types.InlineKeyboardButton('Задать вопрос старшаку' , callback_data= 'first')
    item_was_first2 = types.InlineKeyboardButton('Контакты' , callback_data= 'connn')
    item_kbtu = types.InlineKeyboardButton('Мемы кбту' , callback_data= 'kbtu__keyboard__item')

    markup_inline.add(item_gaid)
    markup_inline.add(item_material)
    markup_inline.add(item_rooms)
    markup_inline.add(item_was_first)
    markup_inline.add(item_was_first2)
    markup_inline.add(item_kbtu)

    bot.send_message(message.chat.id, "Выберите что вам нужно:", reply_markup=markup_inline)

lisss1 = json.load(open("./cont.json" , 'r')) 
def make_btnss(lisss1):
        markup_inline = types.InlineKeyboardMarkup(row_width=3)
        i = 0
        k = 0
        mini_lis = []
        for key , value in lisss1.items():
            btn = types.InlineKeyboardButton(value[0] , callback_data=key)
            # markup_inline.add(btn)
            i+=1
            k+=1
            mini_lis.append(btn)
            if i == 3 or len(lisss1) == k-2:
                markup_inline.row(*mini_lis)
                i = 0
                mini_lis = []
        return markup_inline
ll = make_btnss(lisss1)  


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    markup_reply_back = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
    item_back_main = types.KeyboardButton('Вернуться назад')

    markup_reply_back.add(item_back_main)
    if call.data == "guide":


        file = open("assets/guide_pervasha.pdf", 'rb')
        bot.send_document(call.message.chat.id, file, reply_markup=markup_reply_back, caption="\n\ninst\n@404alumni")


    



    if call.data == "material":
        markup_reply_2 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_material_lesson = types.KeyboardButton('Материал по предметам')
        # item_prepod = types.KeyboardButton('Инфа по преподам')
        item_back = types.KeyboardButton('Вернуться назад')

        markup_reply_2.add(item_material_lesson, item_back)
        bot.send_message(call.message.chat.id, 'Выбор материала\n\ninst\n@404alumni',
            reply_markup= markup_reply_2
        )





    if call.data == 'file_with_documents':
        link = '"https://drive.google.com/drive/folders/1XEEqk3LeWfsXTmp7UGB0CNwR081ONxQ5"'
        bot.send_message(call.message.chat.id, f"<a href={link}>Папка с документами предметов</a>\n\ninst\n@404alumni", parse_mode='html')
        send_info_1(call.message)





    if call.data == 'rooms':
        markup_reply_3 = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard=True)
        item_toiled = types.KeyboardButton('Туалеты')
        item_find_room = types.KeyboardButton('Поиск кабинета')
        item_useful_rooms = types.KeyboardButton('Полезные кабинеты')
        item_back = types.KeyboardButton('Вернуться назад')

        markup_reply_3.add(item_toiled,  item_find_room, item_useful_rooms, item_back)
        bot.send_message(call.message.chat.id, 'Тут ты можешь найти рассположения комнат\n\ninst\n@404alumni',
            reply_markup=markup_reply_3
        )

    #
    # В процессе
    #

    if call.data == 'video_lectures':
        bot.send_message(call.message.chat.id, "В процессе")
        send_info_1(call.message)

    if call.data == "kbtu__keyboard__item":
        link1 = '<a href = "https://instagram.com/kbtu.hub?igshid=YmMyMTA2M2Y=">kbtu.hub</a>'
        link2 = '<a href = "https://instagram.com/office_of_the_registrar?igshid=YmMyMTA2M2Y=">ОР | Офис Регистратора</a>'
        link2 = '<a href = "https://instagram.com/office_of_the_registrar?igshid=YmMyMTA2M2Y=">ОР | Офис Регистратора</a>'
        bot.send_message(call.message.chat.id, f"<b>•</b> {link1}\n<b>•</b> {link2}\n\ninst\n@404alumni", parse_mode="html")
        # bot.send_message(call.message.chat.id, f"<b>•</b> {link1}\n<b>•</b> {link2}\n\ninst\n@404alumni")
        send_info_1(call.message)

    

    if call.data == "connn":
        bot.send_message(call.message.chat.id, "Выберите что вам нужно:", reply_markup=ll)
    # {'FIT_c': "Текст почта бла бла бал", 'BS_c':  "Текст почта бла бла бал qwq w", 'MCM_c' :  "Текст почта бла бла бал" , 'NGD_c': "Текст почта бла бла бал" , 'GEO_c' :  "Текст почта бла бла бал"}
    if call.data in lisss1:
        txt = lisss1[call.data][1]
        print(txt)
        bot.send_message(call.message.chat.id, txt)
    if call.data == "first":
        markup_inline = types.InlineKeyboardMarkup()
        item_1 = types.InlineKeyboardButton('FIT' , callback_data= 'FIT')
        item_2 = types.InlineKeyboardButton('BS' , callback_data= 'BS')
        item_3 = types.InlineKeyboardButton('MCM' , callback_data= 'MCM')
        item_4 = types.InlineKeyboardButton('NGD' , callback_data= 'NGD')
        item_5 = types.InlineKeyboardButton('GEO' , callback_data= 'GEO')
        # item_6 = types.InlineKeyboardButton('FIT' , callback_data= 'first')

        markup_inline.add(item_1 , item_2 , item_3, item_4, item_5)

        bot.send_message(call.message.chat.id, "Выберите что вам нужно:", reply_markup=markup_inline)

        # stud1 = choice(stud)

        # bot.send_message(call.message.chat.id, f"Функция задать вопрос старашаку, отправляет случайного старшекурсника. Ему ты можешь задать вопрос который тебя интересует))\n\n<a href = {stud1[1]}>{stud1[0]}</a>\n\ninst\n@404alumni", parse_mode="html")
        # send_info_1(call.message)
    lisss = ['FIT', 'BS', 'MCM', 'NGD', 'GEO']
    if call.data in lisss:
        print("Hi")
        stud1 = choice(stud[call.data])
        print(stud1[0])
        print(stud1[1])
        bot.send_message(call.message.chat.id, f"Функция задать вопрос старашаку, отправляет случайного старшекурсника. Ему ты можешь задать вопрос который тебя интересует))\n\n <a href={stud1[1]}> {stud1[0]} </a>\n\ninst\n@404alumni",parse_mode="html")




def main():
    keep_alive()
    bot.infinity_polling()

if __name__ == "__main__":
    main()