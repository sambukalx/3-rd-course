def is_valid_password(password):
    return len(password) >= 6 and any(char.isdigit() for char in password)


def get_password_from_user():
    while True:
        password = input("Введите пароль: ")
        if is_valid_password(password):
            return password
        else:
            print("Пароль должен содержать минимум 6 символов и хотя бы 1 цифру.")


if __name__ == "__main__":
    password = get_password_from_user()
    print("Вы ввели допустимый пароль:", password)
