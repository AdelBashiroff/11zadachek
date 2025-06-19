#Решение
import json
import os

FILENAME = "tracks.json"

# Загрузка треков из файла при запуске
def load_tracks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Сохранение треков в файл
def save_tracks(tracks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tracks, f, ensure_ascii=False, indent=4)

# Ввод нового трека
def add_track(tracks):
    artist = input("Исполнитель: ")
    title = input("Название: ")
    author = input("Автор: ")
    year = input("Год: ")
    filename = input("Имя файла: ")

    track = {
        "Исполнитель": artist,
        "Название": title,
        "Автор": author,
        "Год": year,
        "Файл": filename
    }
    tracks.append(track)
    print("Трек добавлен.")

# Вывод всех треков
def show_tracks(tracks):
    if not tracks:
        print("Список треков пуст.")
        return
    for i, track in enumerate(tracks, start=1):
        print(f"\nТрек {i}:")
        for key, value in track.items():
            print(f"{key}: {value}")

# Поиск трека по названию
def search_track(tracks):
    name = input("Введите название трека для поиска: ").lower()
    found = False
    for track in tracks:
        if name in track["Название"].lower():
            print("\nНайден трек:")
            for key, value in track.items():
                print(f"{key}: {value}")
            found = True
    if not found:
        print("Трек не найден.")

# Главное меню
def main():
    tracks = load_tracks()
    while True:
        print("\nМеню:")
        print("1. Добавить трек")
        print("2. Показать все треки")
        print("3. Поиск трека по названию")
        print("4. Сохранить и выйти")

        choice = input("Выберите пункт: ")
        if choice == "1":
            add_track(tracks)
        elif choice == "2":
            show_tracks(tracks)
        elif choice == "3":
            search_track(tracks)
        elif choice == "4":
            save_tracks(tracks)
            print("Сохранено. Выход.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
