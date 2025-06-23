#Решение
def exp_maclaurin(x, tolerance=1e-9):
    result = 1.0  # Начинаем с 1 (первый член ряда)
    term = 1.0  # Начальный член ряда (x^0 / 0!)
    n = 1  # Счётчик степени и факториала

    while abs(term) >= tolerance:
        term *= x / n  # Следующий член ряда (x^n / n!)
        result += term  # Добавляем текущий член ряда к результату
        n += 1  # Переходим к следующему члену ряда

    return result

x = float(input("Введите значение x: "))
result = exp_maclaurin(x)
print(f"exp({x}) по ряду Макларена с точностью 1e-9 = {result}")
