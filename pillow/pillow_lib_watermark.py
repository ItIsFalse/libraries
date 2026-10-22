import os
from PIL import Image, ImageDraw, ImageFont

input_path = 'test.png'
output_path = 'output_test_watermark.png'
watermark_text = "MY WATERMARK"

if not os.path.exists(input_path):
    print(f"Ошибка: Файл '{input_path}' не найден!")
else:
    print("Наложение водяного знака...")

    base = Image.open(input_path).convert("RGBA")
    txt_layer = Image.new('RGBA', base.size, (255, 255, 255, 0)) # Для прозрачности перевели в RGBA
    draw = ImageDraw.Draw(txt_layer)

    try:
        font = ImageFont.truetype("arial.ttf", 20) # Шрифт
    except IOError:
        font = ImageFont.load_default()

    # Принудительно делаем размеры целыми числами
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = int(bbox[2] - bbox[0])
    text_height = int(bbox[3] - bbox[1])

    step_x = text_width + 120
    step_y = (base.height - 90) // 3

    # Тут range точно получит целые числа
    for y in range(40, base.height, step_y):
        offset = int(((y - 50) // step_y) * (text_width // 2))

        for x in range(-150, base.width + 150, step_x):
            draw.text((int(x + offset), int(y)), watermark_text, font=font, fill=(255, 255, 255, 80), stroke_width=1,
                      stroke_fill=(0, 0, 0, 80))

    rotated_txt = txt_layer.rotate(45, expand=True)

    paste_x = (base.width - rotated_txt.width) // 2
    paste_y = (base.height - rotated_txt.height) // 2

    base.paste(rotated_txt, (paste_x, paste_y), rotated_txt)
    base.convert("RGB").save(output_path)
    print(f"Готово! Сохранено: {output_path}")