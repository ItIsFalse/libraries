from tabulate import tabulate

# Исходные данные
headers = ['Name', 'Password', 'Gender']
data = [
    ['Test1', 'qwerty', 'Female'],
    ['Test2', '12345', 'Male'],
    ['Test3', '987652', 'Male'],
    ['Test4', 'asd', 'Female'],
    ['Test5', 'admin', 'Male']
]

print("=== Tabulate (Стиль fancy_grid) ===")
# Tabulate просто берет готовый список и рисует
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

print("\n=== Tabulate (Стиль github) ===")
# Легко менять стили одной командой
print(tabulate(data, headers=headers, tablefmt="github"))
