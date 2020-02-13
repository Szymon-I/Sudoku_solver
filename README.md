# Sudoku solver
Sudoku solver is a script that gives all possible solution for given board.
## Content
- boards -> puzzles to solve in matrix format
- main -> run script
- solver -> class with solving functions
## example output
Puzzle 1:

solution 1:
```
9 5 7 | 6 1 3 | 2 8 4 
4 8 3 | 2 5 7 | 1 9 6 
6 1 2 | 8 4 9 | 5 3 7 
- - - + - - - + - - -
1 7 8 | 3 6 4 | 9 5 2 
5 2 4 | 9 7 1 | 3 6 8 
3 6 9 | 5 2 8 | 7 4 1 
- - - + - - - + - - -
8 4 5 | 7 9 2 | 6 1 3 
2 9 1 | 4 3 6 | 8 7 5 
7 3 6 | 1 8 5 | 4 2 9 
```

Puzzle 2:

solution 1:
```
7 5 2 | 4 9 6 | 1 3 8 
3 9 1 | 2 5 8 | 4 6 7 
4 8 6 | 7 3 1 | 9 5 2 
- - - + - - - + - - -
8 3 9 | 6 7 5 | 2 1 4 
1 2 4 | 9 8 3 | 5 7 6 
6 7 5 | 1 4 2 | 8 9 3 
- - - + - - - + - - -
5 4 7 | 3 2 9 | 6 8 1 
2 6 8 | 5 1 7 | 3 4 9 
9 1 3 | 8 6 4 | 7 2 5 
```

Puzzle 3:

solution 1:
```
8 3 1 | 7 9 5 | 4 6 2 
7 9 2 | 4 6 8 | 1 3 5 
5 4 6 | 3 2 1 | 8 7 9 
- - - + - - - + - - -
3 2 9 | 6 1 4 | 7 5 8 
4 1 5 | 8 3 7 | 2 9 6 
6 8 7 | 2 5 9 | 3 4 1 
- - - + - - - + - - -
9 6 4 | 1 8 3 | 5 2 7 
1 5 3 | 9 7 2 | 6 8 4 
2 7 8 | 5 4 6 | 9 1 3 
```