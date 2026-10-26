import os
import re

DB_FILE = "ban_words_2024.txt"


def load_ban_words(filepath: str) -> set:
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл '{filepath}' не найден!")
        return set()
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read().lower()
    clean_content = content.replace(',', ' ')  # Заменяем запятые на пробелы и разбиваем на отдельные слова
    words = clean_content.split()
    return set(words)  # Возвращаем множество (set) для быстрой работы


def check_text(text: str, ban_words: set) -> list:
    if not ban_words:
        return []
    words_in_text = re.findall(r'\w+', text.lower())  # Находим все слова в тексте (игнорируя знаки препинания)
    return [word for word in words_in_text if word in ban_words]  # Возвращаем те слова, которые есть в черном списке


def main():
    print("Загрузка базы...")
    bad_words = load_ban_words(DB_FILE)

    if not bad_words:
        print("База пуста или не найдена. Проверка невозможна.")
        return

    print(f"База загружена. Слов в базе: {len(bad_words)}")

    # Запрашиваем текст у пользователя
    test_text = input("\nВведите текст для проверки: ")
    bad_found = check_text(test_text, bad_words)

    if bad_found:
        print(f"Найдены запрещенные слова: {', '.join(bad_found)}")
    else:
        print("Текст чист.")


if __name__ == "__main__":
    main()
