from stegano import lsb

# Пути к файлам и текст
input_image = "test.png"
output_image = "output_test.png"  # Сохраняем только в PNG!
secret_text = "Беги, за тобой выехали!"

# Прячем сообщение
# Функция hide возвращает объект картинки
secret_image = lsb.hide(input_image, secret_text)

# Сохраняем результат
secret_image.save(output_image)
print(f"Сообщение успешно спрятано в: {output_image}")

# Извлекаем сообщение
# Функция reveal возвращает строку
extracted_text = lsb.reveal(output_image)

print(f"Извлеченный секрет: {extracted_text}")
