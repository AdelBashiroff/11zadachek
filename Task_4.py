#Решение
n = int(input("Введите радиус круга: "))
r2 = n * n

y = n
while y >= -n:
    x = -n
    while x <= n:
        d = x * x + y * y
        if d <= r2:
            print("0", end="")
        else:
            print("*", end="")
        x += 1
    print()
    y -= 1
