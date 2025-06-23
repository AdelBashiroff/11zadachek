#Решение
def sin_maclaurin(x, eps=1e-9):
    term = x  # первый член ряда (n=0)
    result = 0
    n = 0 #переменная, отслеживающая номер текущего члена ряда. 

    while abs(term) >= eps:
        result += term
        n += 1
        term *= -x * x / ((2 * n) * (2 * n + 1))

    return result

x = float(input("Введите x (в радианах): "))
print(f"sin({x}) ≈ {sin_maclaurin(x)}")
