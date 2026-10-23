import random

from faker import Faker

# Создаем три генератора говорим с какими данными нужно работать
fake_ru = Faker('ru_RU')
fake_uz = Faker('uz_UZ')
fake_en = Faker('en_US')

# Наши кастомные списки для Узбекистана, чтобы было красиво потому что нет внутри fake
UZ_COMPANIES = [
    "MChJ «O'zbekiston Oltinlari»",
    "MChJ «Toshkent Avtomobil Zavodi»",
    "AJ «UzAuto Motors»",
    "MChJ «Uzum Market»",
    "MChJ «Artel Electronics»",
    "XK «O'zbektelekom»"
]

UZ_STREETS = [
    "Amir Temur ko'chasi",
    "Navoiy ko'chasi",
    "Mustaqillik shoh ko'chasi",
    "Buyuk Ipak Yo'li ko'chasi"]


def generate_person(fake, country_code):
    # и так 3 станы и узб с личными правками потому что нет внутри faker
    if country_code == 'RU':
        # Для России используем стандартный Faker + измененный Gmail
        email = fake.email().split('@')[0] + "@gmail.com"
        return {
            "ФИО": fake.name(),
            "Телефон": fake.phone_number(),  # Выдаст +7...
            "Email": email,
            "Компания": fake.company(),  # Выдаст ООО «...»
            "Адрес": fake.address().replace('\n', ', '),
            "Должность": fake.job(),
            "Дата рождения": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d.%m.%Y')
        }

    elif country_code == 'US':
        # Для США используем стандартный Faker (все на английском)
        email = fake.email().split('@')[0] + "@gmail.com"  # тоже измененный Gmail
        return {
            "Name": fake.name(),
            "Phone": fake.phone_number(),
            "Email": email,
            "Company": fake.company(),
            "Address": fake.address().replace('\n', ', '),
            "Job": fake.job(),
            "Birthdate": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%m/%d/%Y')
        }

    elif country_code == 'UZ':
        # Для Узбекистана делаем свои телефоны и компании с помощью random
        phone = f"+998 {random.randint(90, 99)} {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}"
        company = random.choice(UZ_COMPANIES)

        # Меняем домен почты на Gmail как и до этого
        email = fake.email().split('@')[0] + "@gmail.com"

        # Собираем адрес вручную, чтобы было по-узбекски
        address = f"{fake.city()}, {random.choice(UZ_STREETS)}, {fake.building_number()}-uy"

        return {
            "ФИО": fake.name(),
            "Телефон": phone,
            "Email": email,
            "Компания": company,
            "Адрес": address,
            "Должность": fake.job(),
            "Дата рождения": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d.%m.%Y')
        }

    else:
        return None


# range(сколько данных выдать
print("РОССИЯ:")
for _ in range(1):
    p = generate_person(fake_ru, 'RU')
    if p:
        for k, v in p.items():
            print(f"{k}: {v}")
    print("-" * 30)

print("\nСША:")
for _ in range(1):
    p = generate_person(fake_en, 'US')
    if p:
        for k, v in p.items():
            print(f"{k}: {v}")
    print("-" * 30)

print("\nУЗБЕКИСТАН:")
for _ in range(1):
    p = generate_person(fake_uz, 'UZ')
    if p:
        for k, v in p.items():
            print(f"{k}: {v}")
    print("-" * 30)
