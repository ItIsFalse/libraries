from ANSI.ansi import Style

# Внимание (Желтый)
print(f"{Style.YELLOW}[ВНИМАНИЕ] Проверка соединения...{Style.RESET}")

# Успех (Зеленый)
print(f"{Style.GREEN}Успешно подключено к серверу!{Style.RESET}")

# Ошибка (Красный)
print(f"{Style.RED}Ошибка: Неверный пароль.{Style.RESET}")

# Комбинация (Синий + Подчеркивание)
print(f"{Style.BLUE}{Style.UNDERLINE}Справка: Подробнее читайте в документации.{Style.RESET}")

# Комбинация (Белый + Жирный)
print(f"{Style.WHITE}{Style.BOLD}Грязный белый жирный текст{Style.RESET}")

# Комбинация (Красный фон + Черный текст)
print(f"{Style.BG_RED}{Style.BLACK}Черный текст на красном фоне{Style.RESET}")
