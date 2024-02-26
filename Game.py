from solver import Player
import copy

_grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]


def solve(grid, options):
    initial_grid = copy.deepcopy(grid)
    initial_y = copy.deepcopy(player.getY())
    initial_x = copy.deepcopy(player.getX())
    while len(options) != 0:
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
        answer = []
        answer = solve(grid, player.checkOptions())
        if answer != []:
            answer.append(_move)
            return answer
    for i in range(5):
        print(initial_grid[i])
    print(initial_y, initial_x)
    print('\n')
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 0:
                return []
    return ["Done!"]

for i in range(5):
    for j in range(5):
        print("new loop")
        grid_for_this_loop = copy.deepcopy(_grid)
        player = Player(i,j,grid_for_this_loop)
        if (bool(player)):
            answer = []
            answer = solve(grid_for_this_loop,player.checkOptions())
            if answer != []:
                print(f"The starting coordinates are {i},{j}")
                for i in reversed(answer):
                    print(i)
                exit()
            print(f"Unsolvable from {i},{j}")

