"""Модуль для виведення привітання користувача."""


def greet_user(name, age):
    """
    Формує та виводить привітання з іменем та віком користувача.

    Args:
        name (str): Ім'я користувача.
        age (int): Вік користувача.

    Returns:
        str: Рядок привітання.
    """
    message = f"Привіт, {name}! Тобі {age} років."
    print(message)
    return message