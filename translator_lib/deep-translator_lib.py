import logging
import argostranslate.package
import argostranslate.translate

# Отключаем лишние предупреждения от библиотеки stanza
logging.getLogger('stanza').setLevel(logging.ERROR)


def offline_translate(text, from_code, to_code):
    try:
        translated_text = argostranslate.translate.translate(text, from_code, to_code)
        print(f"\nОригинал ({from_code}): {text}")
        print(f"Перевод ({to_code}): {translated_text}")
    except Exception as e:
        print(f"Ошибка перевода: {e}")


if __name__ == "__main__":
    # Если захочешь скачать новые языки, просто раскомментируй нужные строки ниже:

    # argostranslate.package.update_package_index()
    # available_packages = argostranslate.package.get_available_packages()
    # package_to_install = next(filter(lambda x: x.from_code == "ru" and x.to_code == "en", available_packages))
    # argostranslate.package.install_from_path(package_to_install.download())


    offline_translate("Привет, мой друг!", "ru", "en")
    offline_translate("Hello, my friend!", "en", "ru")