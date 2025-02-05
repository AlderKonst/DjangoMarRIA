from django import template  # Импортируем модуль template из Django
from datetime import datetime  # Импортируем класс datetime из модуля datetime

register = template.Library()  # Создаём экземпляр библиотеки шаблонов


def declension(num, forms):  # Для возврата правильной формы слова в зависимости от числа
    if 10 <= num % 100 <= 20:  # Если число в диапазоне 11-19?
        return forms[2]  # То применяем форму для 11-19
    else:  # Если же нет, в других диапазонах
        last_digit = num % 10  # То получаем последнюю цифру числа
        if last_digit == 1:  # Если последняя цифра равна 1
            return forms[0]  # То применяем форму для 1
        elif last_digit in (2, 3, 4):  # Если последняя цифра равна 2, 3 или 4
            return forms[1]  # То применяем форму для 2, 3, 4
        else:  # В остальных случаях
            return forms[2]  # Применяем форма для 0 и 5-9


def current_datetime(value=None):  # Для возврата текущей даты и времени в заданном формате
    now = value if isinstance(value, datetime) else datetime.now()  # Берём значение даты из html, БД или текущее время

    seconds = now.second  # Получаем секунды
    minutes = now.minute  # минуты
    hours = now.hour  # часы
    day = now.day  # день месяца
    month_index = now.month - 1  # Индекс месяца (0-11)
    year = now.year  # и год

    months_russian = [ # Русский список месяцев для преобразования
        "январь", "февраль", "март", "апрель", "май", "июнь",
        "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
    ]

    month = months_russian[month_index]  # Получаем название месяца на русском

    second_form = declension(seconds, ['секунда', 'секунды', 'секунд']) # Склоняем секунды
    minute_form = declension(minutes, ['минута', 'минуты', 'минут']) # минуты
    hour_form = declension(hours, ['час', 'часа', 'часов']) # часы
    year_form = declension(year, ['год', 'года', 'год']) # и год

    return f"{seconds} {second_form} {minutes} {minute_form} {hours} {hour_form} {day} {month} {year} {year_form}"


register.filter('current_datetime', current_datetime)  # Регистрируем фильтр для использования в шаблонах Django
