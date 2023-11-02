import numpy as np


# Функція для виведення гри на екран
def display_field(field):
    for line in field:
        print(" | ".join(line))
        print("-" * 9)

# Функція для перевірки, чи є переможець
def winner(field, gamer):
    # Перевірка по горизонталі і вертикалі
    for i in range(3):
        if all(field[i][j] == gamer for j in range(3)) or all(field[j][i] == gamer for j in range(3)):
            return True

    # Перевірка по діагоналях
    if all(field[i][i] == gamer for i in range(3)) or all(field[i][2 - i] == gamer for i in range(3)):
        return True

    return False

# Функція для перевірки, чи гра завершилася внічию
def draw(field):
    return all(field[i][j] != " " for i in range(3) for j in range(3))



def game():
    field = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_field(field)
        print(f"gamer {current_player}, ваш хід.")

        line = int(input("Введіть номер рядка (0, 1, або 2): "))
        column = int(input("Введіть номер стовпця (0, 1, або 2): "))


        if field[line][column] == " ":
            field[line][column] = current_player
        else:
            print("Ця клітинка вже зайнята. Спробуйте ще раз.")
            continue

        if winner(field, current_player):
            display_field(field)
            print(f"Гравець {current_player} переміг!")
            break
        elif draw(field):
            display_field(field)
            print("Гра закінчилася внічию.")
            break

        current_player = "O" if current_player == "X" else "X"

game()
