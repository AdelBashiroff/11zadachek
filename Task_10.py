#Решение
may_2017 = [12, 15, 20, 17, 18, 23, 9, 9, 4, 14, 26, 27, 25, 22, 18]
may_2018 = [5, 5, 11, 7, 17, 11, 19, 18, 14, 20, 21, 24, 23, 25, 27]

def count_comfort_days(temps):
    count = 0
    for temp in temps:
        if 22 <= temp <= 26:
            count += 1
    return count

comfort_2017 = count_comfort_days(may_2017)
comfort_2018 = count_comfort_days(may_2018)

print("Комфортных дней в мае 2017:", comfort_2017)
print("Комфортных дней в мае 2018:", comfort_2018)

if comfort_2017 > comfort_2018:
    print("2017 год был более комфортным.")
elif comfort_2018 > comfort_2017:
    print("2018 год был более комфортным.")
else:
    print("Оба года были одинаково комфортными.")
