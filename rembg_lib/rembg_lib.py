import os
from typing import cast

from PIL import Image
from rembg import remove, new_session

input_path = r'D:\stucrure\libraries\rembg_lib\test.png'
output_path = r'D:\stucrure\libraries\rembg_lib\output.png'

if not os.path.exists(input_path):
    print(f"Ошибка: Файл '{input_path}' не найден в папке!")
else:
    # Раскомментируй ОДНУ из двух строк ниже:

    # Вариант 1: Легкая и быстрая (170 МБ) тоже хорошая базовая
    session = new_session("isnet-general-use")

    # Вариант 2: Тяжелая и максимально качественная (900 МБ) мало кто использует
    # session = new_session("birefnet-general")

    print("Обработка...")
    input_image = Image.open(input_path)

    output_image = cast(Image.Image, remove(input_image, session=session))

    output_image.save(output_path, format="PNG")
    print(f"Готово! Сохранено в: {output_path}")
