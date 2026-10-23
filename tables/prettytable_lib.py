from prettytable import PrettyTable

# Исходные данные
headers = ['Name', 'Password', 'Gender']
data = [
    ['Test1', 'qwerty', 'Female'],
    ['Test2', '12345', 'Male'],
    ['Test3', '987652', 'Male'],
    ['Test4', 'asd', 'Female'],
    ['Test5', 'admin', 'Male']
]

# Создаем таблицу
table = PrettyTable()
table.field_names = headers

# Добавляем данные построчно
for row in data:
    table.add_row(row)

# Настраиваем стиль (например, убираем рамки)
# table.border = False

print("=== PrettyTable ===")
print(table)