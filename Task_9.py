#Решение
def to_lower_char(c):
    if 'A' <= c <= 'Z':
        return chr(ord(c) + 32) #преобразовываю символ к нижнему регистру, если он заглавный
    return c

def to_lower_string(s):
    result = ""
    for ch in s:
        result += to_lower_char(ch) #преобразовываю всю строку к нижнему регистру
    return result
    
# Чтение строк из файла
lines = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = to_lower_string(line)
        lines.append(line.strip())

# Ввод подстроки
substring = input("Введите подстроку: ")
substring = to_lower_string(substring)

# Поиск индексов
result = []
for i in range(len(lines)):
    if substring in lines[i]:
        result.append(i)

print("Номера строк с подстрокой:", result)
