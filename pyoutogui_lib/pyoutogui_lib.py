import pyautogui as pg


def take_full_screenshot(output_path: str = 'full_screen.png'):
    try:
        print("Делаю скриншот всего экрана...")
        screenshot = pg.screenshot()
        screenshot.save(output_path)
        print(f"Готово! Сохранено: {output_path}")
    except Exception as e:
        print(f"Ошибка при создании скриншота: {e}")


def take_region_screenshot(x: int, y: int, width: int, height: int, output_path: str = 'region_screen.png'):
    try:
        print(f"Делаю скриншот области (x={x}, y={y}, w={width}, h={height})...")
        screenshot = pg.screenshot(region=(x, y, width, height))
        screenshot.save(output_path)
        print(f"Готово! Сохранено: {output_path}")
    except Exception as e:
        print(f"Ошибка при создании скриншота: {e}")


if __name__ == "__main__":
    # 1. Вызов для полного скриншота путь сохранения тут же
    take_full_screenshot('my_desktop.png')
    # 2. Вызов для скриншота области путь сохранения тут же
    take_region_screenshot(x=0,  # отступ слева
                           y=0,  # отступ справа
                           width=300,  # ширина
                           height=400,  # высота
                           output_path='my_region.png')
