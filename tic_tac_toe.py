# Цветной вывод 31 - красный, 32 - зелёный, 33 - жёлтый, 34 - синий
# https://habr.com/ru/sandbox/158854/
def out_color(text, color):
    print(f"\033[{color}m{text}\033[0;0m")


# Приветствие, правила
def greet():
    out_color("*" * 20, 33)
    out_color(" " * 8 + "Game", 32)
    out_color(" " * 3 + "'Tic-tac-toe'", 32)
    print("")
    out_color(" " * 2 + "формат ввода: XY", 34)
    out_color(" " * 2 + "X - номер строки", 34)
    out_color(" " * 2 + "Y - номер столбца", 34)
    out_color("*" * 20, 33)


# Игровое поле
def show():
    print()
    print("     | 0 | 1 | 2 | ")
    print("  ----------------  ")
    for i, row in enumerate(field):
        row_str = f"   {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ----------------  ")
    print()


# Проверка данных
def ask():
    while True:
        cords = input("Ваш ход: ")
        if len(cords) != 2 or not cords.isnumeric():
            out_color("Введите 2 координаты!", 31)
            continue

        x, y = int(cords[0]), int(cords[1])

        if x < 0 or x > 2 or y < 0 or y > 2:
            out_color("Координаты вне диапазона", 31)
            continue

        if field[x][y] != " ":
            out_color("Клетка занята!", 31)
            continue

        return x, y


# Результат выигрыша
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            out_color("Выиграл X !!!", 33)
            return True
        if symbols == ["0", "0", "0"]:
            out_color("Выиграл 0 !!!", 33)
            return True
    return False


# Запуск, ход игры
greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()

    if count % 2 == 1:
        out_color("Ходит крестик", 32)
        hod = "X"
    else:
        out_color("Ходит нолик", 32)
        hod = "0"

    X, Y = ask()
    field[X][Y] = hod

    # Показать последний ход при выигрыше
    if check_win():
        field[X][Y] = hod
        show()
        break

    if count == 9:
        out_color("Ничья", 33)
        break
