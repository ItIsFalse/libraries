from barcode import EAN13
from barcode.writer import ImageWriter, SVGWriter

# Номер для штрих-кода равен 12!
barcode_number = '123456789011'
output_filename = 'output_' + barcode_number

# Проверяем, что ввели ровно 12 цифр
if not barcode_number.isdigit() or len(barcode_number) != 12:
    print("Ошибка: Для EAN-13 нужно ввести ровно 12 цифр.")
else:
    print(f"Генерация штрих-кода для: {barcode_number}...")

    try:
        # Создаем штрих-код (ImageWriter говорит, что сохраняем как картинку PNG)
        my_barcode = EAN13(barcode_number, writer=ImageWriter())

        # Создаем штрих-код (SVGWriter говорит, что сохраняем как картинку SVG)
        my_barcode_svg = EAN13(barcode_number, writer=SVGWriter())

        # Сохраняем (библиотека сама добавит .png/.svg в конец)
        my_barcode_svg.save(output_filename)
        my_barcode.save(output_filename)

        print(f"Готово! PNG сохранен: {output_filename}.png")
        print(f"Готово! SVG сохранен: {output_filename}.svg")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
