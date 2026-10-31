"""Модуль для отримання та перевірки імені й віку користувача."""


def get_name(name=None):
    """
    Отримує ім'я користувача.

    Args:
        name (str, optional): Ім'я користувача. Якщо не передано, запитується через консоль.

    Returns:
        str: Очищене ім'я користувача.
    """
    if name is None:
        name = input("Введіть ваше ім'я: ")
    return str(name).strip()


def get_age(age=None):
    """
    Отримує вік користувача.

    Args:
        age (int | str, optional): Вік користувача. Якщо не передано, запитується через консоль.

    Returns:
        int: Вік користувача у вигляді цілого невід'ємного числа.

    Raises:
        ValueError: Якщо вік є від'ємним або не може бути перетворений на число.
    """
    if age is None:
        age = input("Введіть ваш вік: ")
    age_int = int(age)
    if age_int < 0:
        raise ValueError("Вік не може бути від'ємним.")
    return age_int