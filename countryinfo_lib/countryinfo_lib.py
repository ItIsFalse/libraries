from countryinfo import CountryInfo


def show_country(name):
    try:
        c = CountryInfo(name)
        print(f"\n=== {c.name().upper()} ===")
        print(f"Официальное название: {c.name()}")
        print(f"Альтернативные названия: {', '.join(c.alt_spellings())}")
        print(f"ISO коды: {c.iso()}")
        print(f"Столица: {c.capital()}")
        print(f"Координаты столицы: {c.capital_latlng()}")
        print(f"Население: {c.population():,} чел.")
        print(f"Площадь: {c.area():,} км²")
        print(f"Регион: {c.region()} ({c.subregion()})")
        print(f"Координаты центра: {c.latlng()}")

        neighbors = [n.name() for n in c.neighbors()]
        print(f"Соседи: {', '.join(neighbors) if neighbors else 'Нет'}")
        print(f"Языки (коды): {', '.join(c.languages())}")
        print(f"Валюты: {', '.join(c.currencies())}")
        print(f"Название жителей: {c.demonym()}")
        print(f"Коренное название: {c.native_name()}")
        print(f"Часовые пояса: {', '.join(c.timezones())}")
        print(f"Названия часовых поясов: {', '.join(c.timezone_names())}")
        print(f"Телефонные коды: {', '.join(c.calling_codes())}")
        print(f"Домены: {', '.join(c.tld())}")
        print(f"Википедия: {c.wiki()}")
        print(f"Провинции/Штаты: {', '.join(c.provinces()) if c.provinces() else 'Нет данных'}")
        print("-" * 40)

    except Exception as e:
        if e == KeyError:
            print("Ошибка: Страна не найдена. Введите на английском (Russia, US).")
        else:
            print(f"error: {e}")


user_input = input("Введите страну: ")
show_country(user_input)
