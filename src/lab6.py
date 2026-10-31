"""Головна програма, яка імпортує та використовує створений пакет user_info, стандартні модулі та requests."""

import datetime
import math
import os
import sys
import requests

# Додаємо шлях до папки src, щоб імпорт працював при будь-якому способі запуску
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from user_info.input import get_name, get_age
from user_info.output import greet_user


def main():
    """Запускає демонстрацію роботи пакета user_info, стандартної бібліотеки та стороннього пакета."""
    print("--- 1. Робота з власним пакетом user_info ---")
    user_input_name = input("Введіть ім'я (або натисніть Enter для 'Артем'): ").strip()
    name = get_name(user_input_name if user_input_name else "Артем")

    user_input_age = input("Введіть вік (або натисніть Enter для '19'): ").strip()
    age = get_age(user_input_age if user_input_age else 19)

    greet_user(name, age)

    print("\n--- 2. Робота зі стандартною бібліотекою Python (datetime, math) ---")
    current_year = datetime.date.today().year
    birth_year = current_year - age
    print(f"Поточний рік: {current_year}. Орієнтовний рік народження: {birth_year}")
    print(f"Квадратний корінь з віку ({age}): {math.sqrt(age):.2f}")

    print("\n--- 3. Робота зі стороннім пакетом (requests) ---")
    try:
        response = requests.get("https://www.google.com", timeout=5)
        print(f"Статус-код запиту до Google: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Помилка при виконанні HTTP-запиту: {e}")


if __name__ == "__main__":
    main()