from boards import *
from solver import *


def solve_all():
    for i, board in enumerate(boards, 1):
        solver = Solver(board)
        print(f'Puzzle {i}:')
        solver.solve()


def solve_one(n):
    solver = Solver(boards[n])
    solver.solve()


if __name__ == '__main__':
    solve_all()
