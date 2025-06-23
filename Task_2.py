#Решение
n = int(input("Введите высоту трифорса: "))

def print_spaces(k):
    for _ in range(k):
        print(' ', end='')

def print_stars(k):
    for _ in range(k):
        print('* ', end='')

# Верхний треугольник (на вершине)
for i in range(1, n+1):
    print_spaces(n - i + n)  # центрируем вверх между двумя нижними
    print_stars(i)
    print()

# Нижние два треугольника (рядом)
for i in range(1, n+1):
    print_spaces(n - i)      # отступ перед левым нижним треугольником
    print_stars(i)
    print_spaces((n - i) * 2)  # отступ между двумя нижними
    print_stars(i)
    print()



