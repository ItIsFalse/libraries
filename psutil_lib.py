import os
import platform
import time

import psutil


def print_cpu_info():
    """Выводит информацию о процессоре."""
    print("\n=== [1] ПРОЦЕССОР (CPU) ===")
    print("Ядро-", psutil.cpu_count(logical=False))
    print("Логических-", psutil.cpu_count(logical=True))
    print("Загрузка-", psutil.cpu_percent(interval=1), "%")
    print("Загрузка по ядрам-", psutil.cpu_percent(interval=1, percpu=True))

    freq = psutil.cpu_freq()
    print("Частота-", freq._asdict() if freq else "Нет данных")

    print("Время (user/system/idle)-", psutil.cpu_times()._asdict())
    print("Переключения/Прерывания-", psutil.cpu_stats()._asdict())

    try:
        load = psutil.getloadavg()
        print("Средняя нагрузка-", load)
    except (AttributeError, OSError):
        print("Средняя нагрузка- Нет данных (не поддерживается ОС)")


def print_memory_info():
    """Выводит информацию о памяти (RAM и swap)."""
    print("\n=== [2] ПАМЯТЬ (RAM и SWAP) ===")
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()

    print("--- RAM ---")
    print("Всего-", vm.total, "байт")
    print("Доступно-", vm.available, "байт")
    print("Использовано-", vm.used, "байт")
    print("Свободно-", vm.free, "байт")
    print("Процент-", vm.percent, "%")

    print("--- Swap ---")
    print("Всего-", sm.total, "байт")
    print("Использовано-", sm.used, "байт")
    print("Свободно-", sm.free, "байт")
    print("Процент-", sm.percent, "%")
    print("Подкачано с диска-", sm.sin, "байт")
    print("Сброшено на диск-", sm.sout, "байт")


def print_disk_info():
    """Выводит информацию о дисках."""
    print("\n=== [3] ДИСКИ ===")
    print("--- Разделы ---")
    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"Устройство- {part.device}")
            print(f"Точка монтирования- {part.mountpoint}")
            print(f"Файловая система- {part.fstype}")
            print(f"Всего- {usage.total} байт")
            print(f"Использовано- {usage.used} байт")
            print(f"Свободно- {usage.free} байт")
            print(f"Процент- {usage.percent} %")
            print()
        except PermissionError:
            continue

    print("--- I/O ---")
    io = psutil.disk_io_counters()
    print("Чтение/Запись-", io._asdict() if io else "Нет данных")


def print_network_info():
    """Выводит информацию о сети."""
    print("\n=== [4] СЕТЬ ===")
    print("--- I/O (всего) ---")
    print("Байты/Пакеты-", psutil.net_io_counters()._asdict())

    print("--- По интерфейсам ---")
    for nic, data in psutil.net_io_counters(pernic=True).items():
        print(f"{nic}- {data._asdict()}")

    print("--- Адреса (IP/MAC) ---")
    for nic, adders in psutil.net_if_addrs().items():
        print(f"{nic}- {[addr._asdict() for addr in adders]}")

    print("--- Статистика (up/down, скорость, MTU) ---")
    for nic, stats in psutil.net_if_stats().items():
        print(f"{nic}- {stats}")


def print_battery_info():
    """Выводит информацию о батарее (ПК/ноутбук)."""
    print("\n=== [5] БАТАРЕЯ ===")
    battery = psutil.sensors_battery()
    if battery is None:
        print("Статус- Батарея не обнаружена")
        return

    print("Заряд-", battery.percent, "%")
    print("Подключено к сети-", battery.power_plugged)

    if battery.secsleft == psutil.POWER_TIME_UNKNOWN:
        select_human = "Неизвестно"
    elif battery.secsleft == psutil.POWER_TIME_UNLIMITED:
        select_human = "Без ограничений"
    else:
        select_human = f"{battery.secsleft // 60} мин"

    print("Время до разряда-", select_human)


def print_sensors_info():
    """Выводит датчики: температура, вентиляторы."""
    print("\n=== [6] ДАТЧИКИ (ТЕМПЕРАТУРА/КУЛЕРЫ) ===")
    try:
        temps = psutil.sensors_temperatures()
    except AttributeError:
        temps = {}
    try:
        fans = psutil.sensors_fans()
    except AttributeError:
        fans = {}

    print("--- Температуры ---")
    if not temps:
        print("Нет данных (или не поддерживается ОС)")
    for name, entries in temps.items():
        print(f"{name}- {[t._asdict() for t in entries]}")

    print("--- Вентиляторы ---")
    if not fans:
        print("Нет данных (или не поддерживается ОС)")
    for name, entries in fans.items():
        print(f"{name}- {[f._asdict() for f in entries]}")


def print_all_processes(brief=True):
    """Выводит список всех процессов."""
    print("\n=== [7] СПИСОК ПРОЦЕССОВ ===")
    if brief:
        print("--- Краткий список (PID / Имя / Пользователь) ---")
        for p in psutil.process_iter(["pid", "name", "username"]):
            print(f"PID- {p.info['pid']} | Имя- {p.info['name']} | Пользователь- {p.info['username']}")
    else:
        print("--- Полный список (все атрибуты) ---")
        for p in psutil.process_iter():
            print(p.as_dict())


def print_process_details(pid):
    """Выводит детальную информацию о процессе по PID."""
    print("\n=== [8] ДЕТАЛИ ПРОЦЕССА ===")
    try:
        p = psutil.Process(pid)
        with p.oneshot():
            print("PID-", p.pid)
            print("PID родителя-", p.ppid())
            print("Имя-", p.name())
            print("Путь-", p.exe())
            print("Командная строка-", p.cmdline())
            print("Рабочая директория-", p.cwd())
            print("Владелец-", p.username())
            print("Статус-", p.status())
            print("Время запуска-", p.create_time())
            print("Загрузка CPU-", p.cpu_percent(interval=0.1), "%")
            print("Время CPU-", p.cpu_times()._asdict())
            print("Память (rss/vms)-", p.memory_info()._asdict())
            print("Процент памяти-", p.memory_percent(), "%")
            print("Потоков-", p.num_threads())
            print("Файловых дескрипторов-", p.num_fds() if hasattr(p, "num_fds") else "N/A (Windows)")
            print("Соединения-", [c._asdict() for c in p.net_connections()])
            print("Открытые файлы-", [f._asdict() for f in p.open_files()])
            print("Дочерние PID-", [c.pid for c in p.children()])
    except psutil.NoSuchProcess:
        print("Ошибка- Процесс не существует")
    except psutil.AccessDenied:
        print("Ошибка- Нет прав доступа")


# def print_kill_process(pid, force=False):
#     """Завершает процесс."""
#     print("\n=== [9] УБИЙСТВО ПРОЦЕССА ===")
#     try:
#         p = psutil.Process(pid)
#         if force:
#             p.kill()
#         else:
#             p.terminate()
#         print(f"Успешно- Процесс {pid} завершён (force={force})")
#     except psutil.NoSuchProcess:
#         print("Ошибка- Процесс не существует")
#     except psutil.AccessDenied:
#         print("Ошибка- Нет прав")


def print_users_info():
    """Выводит информацию о пользователях системы."""
    print("\n=== [10] ПОЛЬЗОВАТЕЛИ И СИСТЕМА ===")
    for u in psutil.users():
        print("Пользователь-", u._asdict())
    print("Время загрузки ОС-", psutil.boot_time())


def print_system_meta():
    """Выводит мета-информацию о системе."""
    print("\n=== [11] МЕТА-ИНФОРМАЦИЯ ===")
    print("Платформа-", platform.system())
    print("Релиз-", platform.release())
    print("Версия-", platform.version())
    print("Архитектура-", platform.machine())
    print("Имя хоста-", platform.node())
    print("Версия Python-", platform.python_version())
    print("Версия psutil-", ".".join(map(str, psutil.version_info)))
    print("PID скрипта-", os.getpid())
    print("Это Linux-", psutil.LINUX)
    print("Это Windows-", psutil.WINDOWS)
    print("Это macOS-", psutil.MACOS)


def print_uptime():
    """Выводит время работы системы с момента загрузки."""
    print("\n=== [12] ВРЕМЯ РАБОТЫ (UPTIME) ===")
    uptime_sec = time.time() - psutil.boot_time()
    human = f"{int(uptime_sec // 86400)}д {int(uptime_sec % 86400 // 3600)}ч {int(uptime_sec % 3600 // 60)}м"
    print("Секунд-", uptime_sec)
    print("Человеко-читаемо-", human)


def print_windows_services() -> None:
    """Выводит список служб Windows."""
    print("\n=== [13] СЛУЖБЫ WINDOWS ===")
    if not psutil.WINDOWS:
        print("Статус- Доступно только на Windows")
        return

    for s in psutil.win_service_iter():
        try:
            # Пытаемся получить полную инфу
            print(s.as_dict())
        except FileNotFoundError:
            # Если Windows не знает описание службы, выводим хотя бы имя и статус
            print(f"Служба: {s.name()} | Статус: {s.status()} (Нет данных описания)")
        except Exception as e:
            print(f"Ошибка при чтении службы: {e}")


if __name__ == "__main__":
    print_cpu_info()
    print_memory_info()
    print_disk_info()
    print_network_info()
    print_battery_info()
    print_sensors_info()
    print_all_processes(brief=True)  # Поставил True, чтобы не заспамить консоль
    print_process_details(os.getpid())  # Показываем детали самого себя
    # print_kill_process(os.getpid(), force=True)  # УБИРАЕМ ЭТО, ЕСЛИ НЕ ХОТИТЕ УБИТЬ СКРИПТ
    print_users_info()
    print_system_meta()
    print_uptime()
    print_windows_services()
