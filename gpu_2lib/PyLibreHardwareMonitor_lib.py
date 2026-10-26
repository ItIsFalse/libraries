from PyLibreHardwareMonitor import Computer


def get_intel_info():
    print("Подключение к датчикам...")
    try:
        computer = Computer()

        # Получаем данные о видеокарте (там будет и встроенная Intel)
        # Это заменит несуществующий computer.hardware
        gpu_info = computer.gpu
        print("Данные GPU:")
        print(gpu_info)

        # Если нужно посмотреть температуру процессора, используй computer.cpu
        cpu_info = computer.cpu
        print("Данные CPU:", cpu_info)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    get_intel_info()
