#Решение
import re
import random
from datetime import datetime

# Исключение для неверной даты
class InvalidDateFormat(Exception):
    pass

# Исключение для забракованного этапа
class StageRejected(Exception):
    pass

# Статусы этапов
STATUS_PLANNED = "запланирован"
STATUS_IN_PROGRESS = "осуществляется"
STATUS_COMPLETED = "выполнен"
STATUS_REJECTED = "забракован"

# Проверка формата даты
DATE_REGEX = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

def validate_date(date_str):
    if not DATE_REGEX.match(date_str):
        raise InvalidDateFormat(f"Неверный формат даты: {date_str}")

class Stage:
    def __init__(self, cost, start_date, end_date, description):
        validate_date(start_date)
        validate_date(end_date)
        self.cost = cost
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.status = STATUS_PLANNED
        self.prev_stage = None
        self.next_stage = None

    def start(self):
        self.status = STATUS_IN_PROGRESS

    def stop(self):
        self.status = STATUS_COMPLETED

    def reject(self):
        self.status = STATUS_REJECTED
        raise StageRejected(f"Этап забракован: {self.description}")

    def prev(self):
        return self.prev_stage

    def next(self):
        return self.next_stage

class Project(Stage): pass
class Foundation(Stage): pass
class Walls(Stage): pass
class Roof(Stage): pass
class Finishing(Stage): pass

class Construction:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_stage(self, stage):
        if self.tail:
            self.tail.next_stage = stage
            stage.prev_stage = self.tail
            self.tail = stage
        else:
            self.head = self.tail = stage

    def run(self):
        current = self.head
        while current:
            current.start()
            if random.random() < 0.1:
                current.reject()
            current.stop()
            current = current.next()
        return True

    def go(self):
        try:
            return self.run()
        except StageRejected as e:
            if self.head.description == str(e).split(": ")[1]:
                return False  # проект забракован
            return self.retry(e)

    def retry(self, exception):
        failed_desc = str(exception).split(": ")[1]
        current = self.head
        while current and current.description != failed_desc:
            current = current.next()
        if current and current.prev():
            return self.go_from(current.prev())
        return False

    def go_from(self, stage):
        current = stage
        while current:
            current.status = STATUS_PLANNED
            current = current.next()
        return self.go()

# Тестовая симуляция
success_count = 0
for _ in range(1000):
    construction = Construction()
    construction.add_stage(Project(1000, "01.01.2023", "05.01.2023", "проект"))
    construction.add_stage(Foundation(5000, "06.01.2023", "15.01.2023", "фундамент"))
    construction.add_stage(Walls(7000, "16.01.2023", "25.01.2023", "стены"))
    construction.add_stage(Roof(4000, "26.01.2023", "30.01.2023", "крыша"))
    construction.add_stage(Finishing(3000, "31.01.2023", "05.02.2023", "отделка"))

    if construction.go():
        success_count += 1

print(f"Успешных завершений: {success_count} из 1000")

# Тест на исключение
try:
    bad_stage = Stage(1000, "01.13.2023", "05.01.2023", "плохая дата")
except InvalidDateFormat as e:
    print(f"Исключение при неверной дате успешно поймано: {e}")
