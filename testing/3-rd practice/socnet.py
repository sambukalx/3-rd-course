import multiprocessing
import sys

user_data_list = []
message_queue = multiprocessing.Queue()
print("Добро пожаловать в социальную сеть TALKS!")

# Создание логина
def login():
    print("Введите логин:")
    log = input()
    if len(log) <= 6:
        print("Логин должен состоять минимум из 6 знаков.")
        return login()
    else:
        print(f'Отлично, Ваш логин: {log}')
        return log  # Возвращаем логин


# Создание пароля
def password():
    print("Введите пароль:")
    pas = input()
    n = any(chr.isdigit() for chr in pas)
    if len(pas) >= 6 and n:
        print(f'Отлично, Ваш пароль: {pas}\n')
        return pas  # Возвращаем пароль
    else:
        print("Пароль должен состоять минимум из 6 знаков и содержать как минимум 1 цифру.")
        return password()


# Добавление ячейки для писем
def add_email():
    print("Введите письмо:")
    email = input()
    return email  # Возвращаем письмо


# Ввод пользователей поочередно
for i in range(4):
    print(f"Пользователь {i + 1}:")
    user_data = {}
    user_data['login'] = login()
    user_data['password'] = password()
    user_data['emails'] = []
    user_data['friends'] = []
    user_data_list.append(user_data)

# Вывод информации о пользователях
print("Информация о пользователях:")
for i, data in enumerate(user_data_list, start=1):
    print(f"Пользователь {i}:")
    print(f"Логин: {data['login']}")
    print(f"Пароль: {data['password']}")
    print(f"Письма: {', '.join(data['emails'])}")
    print(f"Друзья: {', '.join(data['friends'])}\n")


# Выбор пользователя
def choice():
    print(
        f"Выберите пользователя, под именем, которого Вы хотите работать:\n1. {user_data_list[0]['login']}\n2. {user_data_list[1]['login']}\n3. {user_data_list[2]['login']}\n4. {user_data_list[3]['login']}")
    q = int(input())
    if q == 1:
        print(f"Вы выбрали ползователя: {user_data_list[0]['login']}")
    elif q == 2:
        print(f"Вы выбрали ползователя: {user_data_list[1]['login']}")
    elif q == 3:
        print(f"Вы выбрали ползователя: {user_data_list[2]['login']}")
    elif q == 4:
        print(f"Вы выбрали ползователя: {user_data_list[3]['login']}")
    else:
        print("Введите число от 1 до 4х.")
        return choice()
    return q


# Выбор действий
def selection(q):
    while True:
        print("\n\n======================\nДоступные функции:")
        print("1. Отправка сообщений\n2. Добавление друзей\n3. Просмотр сообщений\n4. Просмотр друзей\n5. Сменить пользователя\n0. Выйти")
        w = int(input())
        if w == 1:
            send_mail(q - 1, user_data_list)
        elif w == 2:
            add_friend(q - 1, user_data_list)
        elif w == 3:
            view_messages(q - 1, user_data_list)
        elif w == 4:
            view_friends(q - 1, user_data_list)
        elif w == 5:
            q = choice()
        elif w == 0:
            sys.exit("Всего хорошего!")
        else:
            print("Выберите одну из доступных функций.")
            return selection(q)


# Отсылка сообщений
def send_mail(selected_user_index, user_data_list):
    print("Выберите получателя сообщения:")
    for index, user_data in enumerate(user_data_list):
        if index != selected_user_index:
            print(f"{index + 1}. {user_data['login']}")
    recipient_index = int(input()) - 1
    if 0 <= recipient_index < len(user_data_list) and recipient_index != selected_user_index:
        message = add_email()
        user_data_list[recipient_index]['emails'].append(message)
        print(f"Сообщение успешно отправлено пользователю {user_data_list[recipient_index]['login']}")
    else:
        print("Выберите корректного получателя.")
        return send_mail(selected_user_index, user_data_list)


# Добавление друзей
def add_friend(selected_user_index, user_data_list):
    print("Выберите пользователя, которого вы хотите добавить в друзья:")
    for index, user_data in enumerate(user_data_list):
        if index != selected_user_index and user_data['login'] not in user_data_list[selected_user_index]['friends']:
            print(f"{index + 1}. {user_data['login']}")
    friend_index = int(input()) - 1
    if 0 <= friend_index < len(user_data_list) and friend_index != selected_user_index:
        friend_login = user_data_list[friend_index]['login']
        if friend_login not in user_data_list[selected_user_index]['friends']:
            user_data_list[selected_user_index]['friends'].append(friend_login)
            print(
                f"{friend_login} успешно добавлен в друзья пользователя {user_data_list[selected_user_index]['login']}")
        else:
            print(f"{friend_login} уже является другом пользователя {user_data_list[selected_user_index]['login']}")
    else:
        print("Выберите корректного пользователя для добавления в друзья.")
        return add_friend(selected_user_index, user_data_list)


# Просмотр сообщений
def view_messages(selected_user_index, user_data_list):
    print(f"Письма пользователя {user_data_list[selected_user_index]['login']}:\n")
    for index, message in enumerate(user_data_list[selected_user_index]['emails'], start=1):
        print(f"{index}. {message}")
    print("\n")


# Просмотр друзей
def view_friends(selected_user_index, user_data_list):
    print(f"Друзья пользователя {user_data_list[selected_user_index]['login']}:\n")
    for index, friend in enumerate(user_data_list[selected_user_index]['friends'], start=1):
        print(f"{index}. {friend}")
    print("\n")


if __name__ == "__socnet__":
    while True:
        q = choice()
        selection(q)
