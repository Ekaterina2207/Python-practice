#Задача 4. Крестики нолики

win_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

class Cell:
    def __init__(self, number: int):
        self.x = ' '
        self.cell_num = number

    def __str__(self):
        if self.x != ' ':
            return str(self.x)
        return str(self.cell_num)

    def is_occupied(self):
        return self.x != ' '

class Board:
    def __init__(self):
        self.winner = ''
        self.cells = []
        start = 1
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Cell(start))
                start += 1
            self.cells.append(row)

    def __str__(self):
        result = []
        for row in self.cells:
            result.append(' | '.join(str(cell) for cell in row))
        return '\n'.join(result)

    def make_move(self, number: int, symbol: str):
        cell = self.get_cell(number)
        if cell.is_occupied():
            raise Exception('Клетка занята')
        cell.x = symbol

    def get_cell(self, number: int):
        if number < 1 or number > 9:
            raise IndexError('Введено неверное число')
        row = (number-1) // 3
        column = (number-1) % 3
        return self.cells[row][column]

    def check_game(self):
        flat_cells = []
        for row in self.cells:
            for cell in row:
                flat_cells.append(cell)

        for combo in win_comb:
            a, b, c = combo
            if (flat_cells[a].x != ' ' and
                    flat_cells[a].x == flat_cells[b].x == flat_cells[c].x):
                self.winner = flat_cells[a].x
                return True

        for row in self.cells:
            for cell in row:
                if not cell.is_occupied():
                    return False
        return True


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


if __name__ == "__main__":
    b = Board()
    player_1 = Player('Игрок_1', 'X')
    player_2 = Player('Игрок_2', 'O')

    print('Введите номер клетки (1-9):')
    print(b)

    current_player = player_1

    while True:
        try:
            move = int(input(f'{current_player.name}, введите номер клетки ({current_player.symbol}): '))
            b.make_move(move, current_player.symbol)
            print(b)

            if b.check_game():
                if b.winner:
                    print(f'Победил {b.winner}!')
                else:
                    print('Ничья!')
                break

            current_player = player_2 if current_player == player_1 else player_1

        except Exception as error:
            print(error)

