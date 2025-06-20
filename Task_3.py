#Решение
x = float(input("Введите число: "))

# Начальное приближение
r = x
eps = 1e-7  # Точность (чуть меньше, чтобы 6 знаков гарантировано)

# Метод Ньютона
while abs(r * r - x) > eps:
    r = 0.5 * (r + x / r)

# Вывод с точностью до 6 знаков
print(f"Квадратный корень: {r:.6f}")
