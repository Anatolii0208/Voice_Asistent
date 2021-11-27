import telebot
from sqlite3 import *
from telebot import types

#создаем объект бота
mybot = telebot.TeleBot('1264427315:AAHdCp16k-CErpXAcHRnXN6f_9WAlYNeoZk')

#Список названий таблиц товаров
table_list = []

#переменная хранит количество товаров из данной таблицы
count_product = 0

#Admin_now
admin = False
pass_acsept = False
l = 0
password = "abcd1234"

#Переменная для добавление товара в магазин
add_some = False
name_shop = ''
pred_but = ''
del_some = ''

#список предметов добавленых в корзину
list_cart = []

#клавиатура главного меню
keyBoardMain = types.ReplyKeyboardMarkup()
button_1 = types.KeyboardButton("SHOP 🛒")
button_2 = types.KeyboardButton("CART")
button_3 = types.KeyboardButton("BACK")
keyBoardMain.add(button_1, button_2, button_3)

#Inline keyboard for admin
keyBoardAdmin = types.InlineKeyboardMarkup()
keyBoardAdmin.add(types.InlineKeyboardButton("Admin", callback_data="admin"))

#Декаратор оброботки команд
@mybot.message_handler(commands=['start', 'help'])
def get_command(message):
    if message.text == '/start':
        mybot.send_message(message.chat.id, 'Магазин выпечки. Добро пожаловать:', reply_markup=keyBoardMain)
        mybot.send_message(message.chat.id, 'Если вы админ войдите в ваш аккаунт:', reply_markup=keyBoardAdmin)
    elif message.text == '/help':
        mybot.send_message(message.chat.id, """1. /start - приветствие
2. /help - список доступных команд""")
        mybot.send_message(message.chat.id, '[Site](http://127.0.0.1:5000/)', parse_mode='Markdown')

#декоратор для обработи foto сообщений
@mybot.message_handler(content_types=['text','photo'])
def get_text(message):
    global table_list, list_cart, admin, password, pass_acsept, l, count_product, add_some, name_shop
    if admin == True and password == message.text and l < 3 and pass_acsept != True:
        pass_acsept = True
        l=3
        mybot.send_message(message.chat.id, 'Ваш пароль приня. Вы стали админом. У вас появилась возможность упровлять товарами в базе данных(а тоесть добавлять и удалять)! Для того чтобы добавить товар вам нужно зайти в SHOP-> выбрать категорию товаров в которую вы хотите добавить товар и внизу появится кнопка, также у вас есть воз ')
    elif l < 3 and admin == True:
        mybot.send_message(message.chat.id,"Вы ввели неправельный пароль")
        l+=1
    elif add_some == True:
        con = connect("Shop_bot.db")
        cur = con.cursor()
        photo_id = message.photo[0].file_id
        photo_inf = mybot.get_file(photo_id)
        download_photo = mybot.download_file(photo_inf.file_path)
        cur.execute(f"""INSERT INTO {name_shop}_shop VALUES(?,?,?,?)""", (Binary(download_photo), message.caption.split("\n")[0], message.caption.split("\n")[1], message.caption.split("\n")[2]))
        con.commit()
        con.close()
        add_some = False
    elif message.text == "SHOP 🛒":
        #print(2)

        #Обнуление
        count_product = 0
        #инлайн клавиатура
        keyBoardThings = types.InlineKeyboardMarkup()

        #подключение к бд
        con = connect("Shop_bot.db")
        cur = con.cursor()

        cur.execute("""SELECT tbl_name
        FROM sqlite_master
        WHERE type = 'table' """)
        list_1 = cur.fetchall()
        if len(list_1) != len(table_list):
            table_list.clear()
            #отделение таблиц от хлама
            for val in list_1:
                if val[0].split("_")[1] == "shop":
                    table_list.append(val[0].replace("_shop",''))

        #print(table_list)

        #Создание инлайн кнопок динамически
        for el in table_list:
            keyBoardThings.add(
                types.InlineKeyboardButton(el, callback_data=el)
            )

        mybot.send_message(message.chat.id, 'Что желаете покушать?', reply_markup=keyBoardThings)
    elif message.text == "CART":
        keyBoarddelete = types.InlineKeyboardMarkup()
        keyBoarddelete.add(types.InlineKeyboardButton("Удалить товар из корзины", callback_data="delete"))
        if len(list_cart) == 0:
            mybot.send_message(message.chat.id, 'У вас нет товаров в корзине')
        else:
            price_cart = 0
            for i in list_cart:
                mybot.send_photo(message.chat.id, i["photo"], caption=i["caption"], reply_markup=keyBoarddelete)
                for j in i["caption"].split("\n")[1].split(" "):
                    if j != '':
                        price_cart += int(j)
                        break
            mybot.send_message(message.chat.id,   "Это общая стоимость ваших покупок которые выы добавили в корзину" + "\t" + str(price_cart) + "грн")

    elif message.text == "BACK":
        mybot.send_message(message.chat.id, 'Магазин выпечки. Добро пожаловать:', reply_markup=keyBoardMain)

    '''#print(message.photo[-1].file_id)
    con = connect("ImageStore.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS ImageS(
    img BLOB NULL,
    ganr TEXT,
    value TEXT,
    description TEXT
    )""")
    con.commit()

    photo_id = message.photo[-1].file_id

    photo_info = mybot.get_file(photo_id)

    download_photo = mybot.download_file(photo_info.file_path)

    bot_caption = list(message.caption.split('\n'))
    bot_caption.insert(0,Binary(download_photo))
    cur.execute("""INSERT INTO ImageS
        VALUES(?,?,?,?)
    """,bot_caption)
    con.commit()

    con.close()'''

@mybot.callback_query_handler(func=lambda call: True)
def get_query(query):
    global table_list, count_product, list_cart, admin, pass_acsept, name_shop, add_some, pred_but, del_some
    if query.data == "admin":
        admin = True
        mybot.send_message(query.message.chat.id, 'Введите пароль')
    elif query.data in table_list:
        # подключение к бд
        con = connect("Shop_bot.db")
        cur = con.cursor()
        #print(query.data)
        cur.execute(f"""SELECT photo, name, price, description
                FROM {query.data}_shop
                LIMIT 2 OFFSET({count_product})""")
        count_product += 2

        #Получим данные с запроса о товаре
        lister = cur.fetchall()
        con.close()

        # Добавление кнопки для добавление товара в корзину
        keyBoardcart = types.InlineKeyboardMarkup()
        keyBoardcart.add(types.InlineKeyboardButton("Добавить товар в корзину", callback_data="cart"))
        if pass_acsept == True:
            keyBoardcart.add(types.InlineKeyboardButton("Удалить товар из магазина", callback_data="delete_from_shop"))
            del_some = query.data
        #Загружаем данные с запрроса в телегу
        for el in lister:
            print(el[1])
            mybot.send_photo(query.message.chat.id, el[0], caption=f"""
                {el[1]}
                {el[2]}
                {el[3]}
""",reply_markup=keyBoardcart)
            #mybot.answer_callback_query(query.message.chat.id, "Товар добавлен!", show_alert=False)

        if len(lister) > 0:
            keyBoardMore = types.InlineKeyboardMarkup()
            keyBoardMore.add(types.InlineKeyboardButton("Еще товаров", callback_data=query.data))
            mybot.send_message(query.message.chat.id, "Хотите еще посмотреть товары", reply_markup=keyBoardMore)
        else:
            mybot.send_message(query.message.chat.id, "Сдесь товаров уже нет но мы постараемся добавить!")
        #Кнопка для добавление товара (возможность только админа)
        if pass_acsept == True:
            keyBoardAdd = types.InlineKeyboardMarkup()
            keyBoardAdd.add(types.InlineKeyboardButton("Добавить товар", callback_data="add"))
            mybot.send_message(query.message.chat.id, "Хотите добавить товар в эту категорию?", reply_markup=keyBoardAdd)
            pred_but = query.data
    elif query.data == "cart":
        dict_photo = {"photo" : query.message.photo[0].file_id, "caption" : query.message.caption}
        list_cart.append(dict_photo)
    elif query.data == "delete":
        val = query.message.caption
        for i in list_cart:
            for keys,values in i.items():
                if values == val:
                    list_cart.remove(i)
                    break
    elif query.data == "add":
        add_some = True
        name_shop = pred_but
    elif query.data == "delete_from_shop":
        #'''print(query.message.caption.split("""
        #""")[0],del_some)'''

        a = query.message.caption.split('\n')[0]

        con = connect("Shop_bot.db")
        cur = con.cursor()
        #print(a)
        cur.execute(f"""DELETE FROM {del_some + '_shop'} WHERE name = (?)""",(a,))
        con.commit()

        con.close()
mybot.polling()