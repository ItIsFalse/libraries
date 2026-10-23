import os

import qrcode
from PIL import Image
from qrcode.image.pil import PilImage


def create_qr(data, filename="output_qrcode.png", add_photo=False):  # add_photo перезаписывать или новое

    # Настраиваем и генерируем QR-код

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        image_factory=PilImage  # <--- Добавь эту строчку
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Создаем картинку
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Если нужно фото, вставляем его
    if add_photo:
        photo_path = "../qrcode_lib/test_photo.png"
        if os.path.exists(photo_path):
            try:
                logo = Image.open(photo_path)

                # Вычисляем размер логотипа (примерно 15% от размера QR-кода)
                qr_width, qr_height = img.size
                logo_size = int(qr_width * 0.15)  # 15% от ширины можно менять размеры
                logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

                # Вычисляем координаты для центра
                pos_x = (qr_width - logo_size) // 2
                pos_y = (qr_height - logo_size) // 2

                # Вставляем логотип
                img.paste(logo, (pos_x, pos_y))
                print("📸 Логотип успешно добавлен в центр.")
            except Exception as e:
                print(f"⚠Не удалось добавить фото: {e}")
        else:
            print(f"⚠Файл {photo_path} не найден. QR-код создан без фото.")

    # Сохраняем
    img.save(filename)
    print(f"\nГотово! QR-код сохранен в файл: {os.path.abspath(filename)}")


def main():
    print("ГЕНЕРАТОР QR-КОДОВ:")

    photo_choice = input("Добавить фото в центр? (да/нет): ").strip().lower()
    add_photo = photo_choice in ['да', 'yes', 'y', 'д']

    if add_photo:
        print("ℹБудет использован файл 'test_photo.png' из папки со скриптом.")

    print("1. Обычный текст или ссылка")
    print("2. Позвонить (Телефон)")
    print("3. Отправить Email")
    print("4. Подключиться к Wi-Fi")
    print("5. Геолокация")
    print("6. Выход")

    choice = input("Выберите вариант (1-6): ").strip()

    if choice == '1':
        text = input("Введите текст или ссылку: ")
        create_qr(text, "qr_text.png", add_photo)

    elif choice == '2':
        phone = input("Введите номер телефона (например, +998901234567): ")
        create_qr(f"tel:{phone}", "qr_phone.png", add_photo)

    elif choice == '3':
        email = input("Введите email: ")
        create_qr(f"mailto:{email}", "qr_email.png", add_photo)

    elif choice == '4':
        ssid = input("Введите название Wi-Fi сети (SSID): ")
        password = input("Введите пароль: ")
        wifi_string = f"WIFI:T:WPA;S:{ssid};P:{password};;"
        create_qr(wifi_string, "qr_wifi.png", add_photo)

    elif choice == '5':
        lat = input("Введите широту (например, 41.311): ")
        lon = input("Введите долготу (например, 69.279): ")
        create_qr(f"geo:{lat},{lon}", "qr_geo.png", add_photo)

    elif choice == '6':
        print("Выход...")

    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")


if __name__ == "__main__":
    main()
