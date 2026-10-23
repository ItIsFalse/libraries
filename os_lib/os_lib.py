import os


def main():
    print("УПРАВЛЕНИЕ ПИТАНИЕМ WINDOWS")
    print("1. Выключить компьютер (через 10 сек)")
    print("2. Перезагрузить компьютер (через 10 сек)")
    print("3. Спящий режим (Sleep)")
    print("4. Отмена запланированного выключения")
    print("5. Выход из программы")

    choice = input("Выберите действие (1-5): ").strip()

    if choice == '1':
        print("⚠️ Компьютер выключится через 10 секунд. Нажмите Ctrl+C для отмены.")
        os.system('shutdown /s /t 10')

    elif choice == '2':
        print("⚠️ Компьютер перезагрузится через 10 секунд. Нажмите Ctrl+C для отмены.")
        os.system('shutdown /r /t 10')

    elif choice == '3':
        print("Переход в спящий режим...")
        # Команда для перевода ПК в сон
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

    elif choice == '4':
        print("Отмена запланированного выключения...")
        # Команда /a отменяет таймер выключения
        os.system('shutdown /a')

    elif choice == '5':
        print("Выход.")

    else:
        print("❌ Неверный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
