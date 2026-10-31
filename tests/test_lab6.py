"""Модульні тести для пакета user_info (Варіант 8)."""

import os
import sys
import unittest
from unittest.mock import patch

# Додаємо шлях до директорії src для імпорту пакета user_info
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from user_info.input import get_name, get_age
from user_info.output import greet_user


class TestUserInfoPackage(unittest.TestCase):
    """Клас для тестування функцій модулів input та output пакета user_info."""

    def test_get_name_with_argument(self):
        """Тест отримання імені при передачі аргументу напряму."""
        self.assertEqual(get_name("Артем"), "Артем")
        self.assertEqual(get_name("  Олександр  "), "Олександр")

    @patch('builtins.input', return_value="Андрій")
    def test_get_name_from_input(self, mock_input):
        """Тест отримання імені через функцію input()."""
        self.assertEqual(get_name(), "Андрій")

    def test_get_age_with_argument(self):
        """Тест отримання віку при передачі числа або рядка."""
        self.assertEqual(get_age(19), 19)
        self.assertEqual(get_age("20"), 20)

    @patch('builtins.input', return_value="21")
    def test_get_age_from_input(self, mock_input):
        """Тест отримання віку через функцію input()."""
        self.assertEqual(get_age(), 21)

    def test_get_age_negative_raises_error(self):
        """Тест перевірки виклику помилки ValueError для від'ємного віку."""
        with self.assertRaises(ValueError):
            get_age(-5)

    def test_greet_user(self):
        """Тест форматування привітання користувача."""
        result = greet_user("Артем", 19)
        self.assertEqual(result, "Привіт, Артем! Тобі 19 років.")


if __name__ == "__main__":
    unittest.main()
