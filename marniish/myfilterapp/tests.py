from django.test import TestCase # Импортируем тесты из модуля django.test
from datetime import datetime # Импортируем класс datetime из модуля datetime
from myfilterapp.templatetags import current # Импортируем модуль с фильтрами форматирования времени

class DeclensionTest(TestCase): # Для проверки def declension
    def test_declension(self): # Проверяем склонения
        forms = ['секунда', 'секунды', 'секунд'] # Список форм слова "секунда" для склонений
        n_s = { # Словарь с тестовыми данными: число : ожидаемая форма слова
            1: 'секунда',
            2: 'секунды',
            5: 'секунд',
            11: 'секунд',
            21: 'секунда',
            101: 'секунда',
            111: 'секунд',
            0: 'секунд'
        }
        for n, s in n_s.items(): # Перебираем тестовые данные
            self.assertEqual(current.declension(n, forms), s) # Склонения правильно определяются?

class CurrentDatetimeTest(TestCase): # Для проверки def current_datetime
    def test_current_datetime(self): # Проверяем вывод заданных заданных значений времени
        dt = datetime(2024, 5, 15, 10, 30, 45) # Создаем объект datetime с заданными данными
        data_txt = "45 секунд 30 минут 10 часов 15 май 2024 года" # Ожидаемое отображение в html
        self.assertEqual(current.current_datetime(dt), data_txt) # Выводит data_txt, определённое в dt или нет&

