# Рисуем игровое поле
board = list(range(1, 10))
#Создаем функицию
def draw_board(board):
    print("-", 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i*3], "|", board[2 + i * 3],"|")
        print("-" * 13)

# Создаем функцию для приема ввода от пользователя.
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставишь "  + player_token + " ?")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Уверенны, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка занята!!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9!")
# Теперь создадим функцию проверки победил ли игрок, при которой если игрок победил выводится сообщение, если же нет то возвращается False и игра продолжается.
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
#Переходим к созданию главной функции
def main(board):
    counter = 0
    win = False
    while not  win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board)
        if tmp:
            print(tmp, "Победа!")
            win = True
            break
        if counter == 9:
            print("Победила дружба!")
            break
    draw_board(board)

main(board)

input("Нажмите Enter для выхода!")