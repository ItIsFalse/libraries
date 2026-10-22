from getpass import getpass
import os

SECRET_PASSWORD = "12345"

file_path = r"D:\stucrure\libraries\getpass_lib\test_data.txt" # Файл котоый защищаем

print("Доступ к файлу заблокирован.")
password = getpass("Введите пароль: ")

if password == SECRET_PASSWORD:
    print("Пароль верный! Доступ разрешен.")

    if os.path.exists(file_path):
        # Если файл есть, читаем и показываем
        with open(file_path, 'r', encoding='utf-8') as f:
            print("\nСодержимое файла:")
            print(f.read())
    else:
        print(f"Файл '{file_path}' не найден.")
else:
    print("Неверный пароль! Доступ запрещен.")