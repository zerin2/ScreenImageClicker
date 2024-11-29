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
    return os.system('calc')


def open_img_and_click() -> None:
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
    open_calc()
    time.sleep(2)
    open_img_and_click()


if __name__ == '__main__':
    run()
