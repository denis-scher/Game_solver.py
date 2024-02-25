from solver import Player
import copy

_grid = [[0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
initialGrid = copy.deepcopy(_grid)


def solve(grid, options):
    initial_grid = copy.deepcopy(grid)
    initial_y = copy.deepcopy(player.getY())
    initial_x = copy.deepcopy(player.getX())
    for i in range(5):
        print(grid[i])
    print(player.getY(), player.getX())
    print('\n')
    if len(options) != 0:
        _move = options[-1]
        player.move(options.pop())
        grid = player.getGrid()
        if solve(grid, player.checkOptions()) == "Solved":
            print(_move)
        else:
            if len(options) == 0:
                return "Not Solved"
            player.setGrid(initial_grid)
            grid = player.getGrid()
            player.setY(initial_y)
            player.setX(initial_x)
            for i in range(5):
                print(grid[i])
            print(player.getY(), player.getX())
            print('\n')
            _move = options[-1]
            player.move(options.pop())
            grid = player.getGrid()
            for i in range(5):
                print(grid[i])
            print(player.getY(), player.getX())
            print('\n')
            solve(grid, player.checkOptions())
    if len(options) == 0:
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 0:
                    return "Not Solved"
        return "Solved"

for i in range(5):
    for j in range(5):
        _grid = initialGrid
        player = Player(i,j,_grid)
        if (bool(player)):
            print(solve(_grid,player.checkOptions()))
        continue

