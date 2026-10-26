import GPUtil
from tabulate import tabulate


def get_nvidia_info():
    try:
        # Пытаемся получить список видеокарт
        gpus = GPUtil.getGPUs()

        if not gpus:
            print("Видеокарты NVIDIA не обнаружены (или не установлен nvidia-smi).")
            return

        gpu_list = []
        for gpu in gpus:
            gpu_list.append([
                gpu.id,
                gpu.name,
                f"{gpu.load * 100:.1f}%",
                f"{gpu.memoryFree}MB",
                f"{gpu.memoryUsed}MB",
                f"{gpu.memoryTotal}MB",
                f"{gpu.temperature}°C"
            ])

        headers = ["ID", "Name", "Load", "Free", "Used", "Total", "Temp"]
        print(tabulate(gpu_list, headers=headers, tablefmt="fancy_grid"))

    except Exception as e:
        print(f"Ошибка при получении данных NVIDIA: {e}")


if __name__ == "__main__":
    get_nvidia_info()
