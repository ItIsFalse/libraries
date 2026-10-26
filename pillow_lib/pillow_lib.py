import os

from PIL import Image

input_path = 'test.png'
output_path_bw = 'output_test_bw.png'
output_path_resized = 'output_test_resized.png'
output_path_rotated = 'output_test_rotated.png'

if not os.path.exists(input_path):
    print(f"Ошибка: Файл '{input_path}' не найден!")
else:
    print("Обработка изображения...")
    img = Image.open(input_path)

    # Черно-белый режим (Градации серого)
    bw_img = img.convert('L')
    bw_img.save(output_path_bw)
    print(f"1. Ч/Б сохранено: {output_path_bw}")

    # Изменение размера
    resized_img = img.resize((300, 150))
    resized_img.save(output_path_resized)
    print(f"2. Ресайз сохранен: {output_path_resized}")

    # Поворот ---
    rotated_img = img.rotate(90)
    rotated_img.save(output_path_rotated)
    print(f"3. Поворот сохранен: {output_path_rotated}")

    print("Вся обработка завершена!")
