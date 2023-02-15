import csv
import telebot
import requests
import aiogram

# API_link = "token"
# updates = requests.get(API_link + "/getUpdates?offset=-1").json()
# print(updates)

# message = updates["result"][0]["message"]
# chat_id = message["from"]["id"]
# text = message["text"]
#
# sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")

bot = telebot.TeleBot("token")

samsung_list = ['самсунг', 'Самсунг', 'Samsung', 'samsung', 'cfveyu', 'ыфьыгтп']
iphone_list = ['iphone', 'IPHONE', 'афон', 'айфон', 'Iphon', 'Iphone']
xiaomi_list = ['xiaom', 'xiaomi', 'Xiaomi', 'ксяоми', 'Ксяоми' 'ксаоми', 'Ксаоми']

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Приветствуем Вас, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Добрый день":
        bot.send_message(message.chat.id, "Здравствуйте!", parse_mode="html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")
    elif message.text == "фото":
        фото = open("ава.jpg", "rb")
        bot.send_photo(message.chat.id, фото)
    else:
        bot.send_message(message.chat.id, "Я не понимаю о чем Вы, сформулируйте свой вопрос более корректно",
                         parse_mode="html")


def get_res_by(cell_name, model_name, service_name):
    with open("CellServicePrice.csv", "r") as f:
        reader = csv.DictReader(f)

        for line in reader:
            if cell_name in line.values():
                if model_name in line.values():
                    if service_name in line.values():
                        return print(
                            f'\nСтоимость работ по услуге: "{line["Услуга"]}", составит {line["Стоимость"]} рублей')
        return print('\nНе смог найти стоимость, просьба обратиться по телефону 555 55 55')


def check_price(cell_mark):
    cell_model = input(f'\n Введите модель телефона! Например: Note 8, Redmi, X, 13\n')
    cell_trouble = input( f'\n Введите поломку или что необходимо починить!Например: не работает экран, заменить стекло, заменить батарейку\n')
    print(f'\nВаш запрос. Марка телефона: {cell_mark}, Модель телефона: {cell_model}, Проблема: {cell_trouble}')
    get_res_by(cell_mark, cell_model, cell_trouble)


while True:
    print(f'\nВас приветствует бот, я могу назвать стоимость работы по ремонту вашего '
          f'телефона или планшета!\nДля этого необходимо ввести марку и модель телефона, а также причину обращения')

    input_com = input(f'\nВведите марку телефона! Например: Самсунг, Айфон и т.д.\n')

    if input_com in samsung_list:
        check_price('Samsung')

    elif input_com in iphone_list:
        check_price('iPhone')

    elif input_com in xiaomi_list:
        check_price('Xiaomi')

    else:
        print("Проверьте вводимую команду!\n")

bot.polling(none_stop=True)

nadim = "КУ-КУ"
print(nadim)