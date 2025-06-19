#Решение
def find_substring_indexes(filename, substring):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    substring_lower = substring.lower()

    for i, line in enumerate(lines):
        if substring_lower in line.lower():
            result.append(i)

    return result

filename = input("Введите имя файла: ")
substring = input("Введите подстроку для поиска: ")

indexes = find_substring_indexes(filename, substring)

print("Индексы строк, содержащих подстроку:", indexes)
