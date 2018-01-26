# inferior solution because if the grids scales further, the solution does not
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['.', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

i = 0
j = 0
for i in range(6):
    print()
    for j in range(8):
        print(grid[j][i], end='')
        j += 1
    i += 1
