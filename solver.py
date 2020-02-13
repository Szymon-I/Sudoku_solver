class Solver:
    def __init__(self, board):
        self.board = board
        self.solved = 0

    def possible(self, y, x, n):
        # check column
        for i in range(9):
            if self.board[y][i] == n:
                return False
        # check column
        for i in range(9):
            if self.board[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        # check square
        for i in range(3):
            for j in range(3):
                if self.board[y0 + i][x0 + j] == n:
                    return False
        return True

    # util func for printing formatted puzzle
    def display(self):
        line_break = '- - - + - - - + - - -'
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print(line_break)
            for j, x in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print('|', end=' ')
                print(x, end=' ')
            print()

    # solve using backtracking
    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.board[y][x] = n
                            self.solve()
                            self.board[y][x] = 0
                    return
        self.solved += 1
        print(f'solution {self.solved}:')
        self.display()
