#Решение
def to_lower_char(c):
    if 'A' <= c <= 'Z':
        return chr(ord(c) + 32)
    return c

def to_lower_string(s):
    result = ""
    for ch in s:
        result += to_lower_char(ch)
    return result

def contains_substring(line, sub):
    n = len(line)
    m = len(sub)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if to_lower_char(line[i + j]) != to_lower_char(sub[j]):
                match = False
                break
        if match:
            return True
    return False

# Чтение строк из файла
lines = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line.strip())

# Ввод подстроки
substring = input("Введите подстроку: ")

# Поиск индексов
result = []
for i in range(len(lines)):
    if contains_substring(lines[i], substring):
        result.append(i)

print("Номера строк с подстрокой:", result)
