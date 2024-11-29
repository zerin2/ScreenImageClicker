import time
import os
from enum import Enum

import pyautogui

from settings import MEDIA_PATH


class Buttons(Enum):
    BUTTON_1 = MEDIA_PATH / 'button_1.PNG'
    BUTTON_2 = MEDIA_PATH / 'button_2.PNG'
    BUTTON_PLUS = MEDIA_PATH / 'button_plus.PNG'
    BUTTON_7 = MEDIA_PATH / 'button_7.PNG'
    BUTTON_EQUALS = MEDIA_PATH / 'button_equals.PNG'


def open_calc() -> None:
    """
    Открывает приложение калькулятора.

    Возвращает: None
    """
    return os.system('calc')


def open_img_and_click() -> None:
    """
    Ищет на экране изображения кнопок и кликает по ним.

    Для каждой кнопки из перечисления Buttons:
    - Проверяет существование файла изображения.
    - Ищет изображение на экране с помощью pyautogui.locateOnScreen с заданной точностью.
    - Если изображение найдено, выполняет клик по нему.
    - Обрабатывает исключение ImageNotFoundException, если изображение не найдено на экране.

    Возвращает: None
    """
    for button in Buttons:
        time.sleep(0.5)
        image_path = button.value

        if not image_path.exists():
            print(f'Изображение не найдено, путь: {image_path}')
            continue
        try:
            required_button = pyautogui.locateOnScreen(str(image_path), confidence=0.9)
            if required_button:
                pyautogui.click(required_button)
        except pyautogui.ImageNotFoundException as e:
            print(
                f'Изображение не найдено на экране, путь: {image_path}\n'
                f'Ошибка: {e}'
            )


def run() -> None:
    """
    Основная функция запуска скрипта.

    Выполняет следующие шаги:
    - Открывает приложение калькулятора.
    - Ждет 2 секунды для запуска приложения.
    - Вызывает функцию open_img_and_click для автоматизации кликов по кнопкам.

    Возвращает: None
    """
    open_calc()
    time.sleep(2)
    open_img_and_click()
    print('Успешно!')


if __name__ == '__main__':
    run()
