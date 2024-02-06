

grid = [[0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]


class Player:
    def __init__(self, y, x):
        self.x = 0
        self.y = 0
        self.setLocation(y,x)

    def getLocation(self):
        return [self.y, self.x]

    def move(self, direction):
        if direction == "right":
            x_add = 0
            for i in range(self.x + 1, 5):
                if grid[self.y][i] == 0:
                    grid[self.y][i] = 1
                    x_add = x_add + 1
                else:
                    break
            self.x = self.x + x_add

        if direction == "left":
            x_add = 0
            for i in range(self.x-1, -1, -1):
                if grid[self.y][i] == 0:
                    grid[self.y][i] = 1
                    x_add = x_add + 1
                else:
                    break
            self.x = self.x - x_add

    def setLocation(self, y, x):
        if grid[y][x] == 1:
            print("The location is invalid")
        self.x = x
        self.y = y
        grid[y][x] = 1

#    def checkAvailability:



player = Player(4,4)
player.move("left")
for i in grid:
    print(i)
print(player.getLocation())