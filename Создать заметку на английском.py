def create_note():
    note = input("Введите вашу заметку: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Заметка сохранена!")


def read_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("У вас пока нет заметок")


def main():
    print("Привет! Что вы хотите сделать?")
    print("1. Создать новую заметку")
    print("2. Посмотреть все заметки")

    choice = input("Введите число: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    else:
        print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
