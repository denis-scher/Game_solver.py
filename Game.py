from solver import Player

_grid = [[0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

player = Player(0,0,_grid)
def solve(grid, options):
    for i in range(5):
        print(grid[i])
    print(player.getY(), player.getX())
    print('\n')
    if len(options) != 0:
        _move = options[-1]
        player.move(options.pop())
        if solve(player.getGrid(), player.checkOptions()) == "Solved":
            print(_move)
        else:
            if len(options) == 0:
                return "Not Solved"
            move2 = options[-1]
            player.move(options.pop())
            for i in range(5):
                print(grid[i])
            print(player.getY(), player.getX())
            print('\n')
            solve(player.getGrid(), player.checkOptions())
    if len(options) == 0:
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 0:
                    return "Not Solved"
        return "Solved"

print(solve(_grid,player.checkOptions()))

