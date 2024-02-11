

grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]


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

        if direction == "down":
            y_add = 0
            for i in range(self.y + 1, 5):
                if grid[i][self.x] == 0:
                    grid[i][self.x] = 1
                    y_add = y_add + 1
                else:
                    break
            self.y = self.y + y_add

        if direction == "up":
            y_add = 0
            for i in range(self.y-1, -1, -1):
                if grid[i][self.x] == 0:
                    grid[i][self.x] = 1
                    y_add = y_add + 1
                else:
                    break
            self.y = self.y - y_add

    def setLocation(self, y, x):
        if grid[y][x] == 1:
            print("The location is invalid")
        self.x = x
        self.y = y
        grid[y][x] = 1

    def checkOptions(self):
        up = True
        down = True
        left = True
        right = True
        _list = []
        if self.x == 4:
            right = False
        elif grid[self.y][self.x + 1] == 1:
            right = False
        if self.x == 0:
            left = False
        elif grid[self.y][self.x - 1] == 1:
            left = False
        if self.y == 4:
            down = False
        elif grid[self.y + 1][self.x] == 1:
            down = False
        if self.y == 0:
            up = False
        elif grid[self.y - 1][self.x] == 1:
            up = False
        if up is True:
            _list.append("up")
        if down is True:
            _list.append("down")
        if left is True:
            _list.append("left")
        if right is True:
            _list.append("right")
        return _list


player = Player(0,0)
player.move("right")
for i in grid:
    print(i)
print(player.getLocation())
print(player.checkOptions())
