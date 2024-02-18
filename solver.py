

class Player:
    def __init__(self, y, x, grid):
        self.x = 0
        self.y = 0
        self.grid = grid
        self.setLocation(y,x)

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def move(self, direction):
        if direction == "right":
            x_add = 0
            for i in range(self.x + 1, 5):
                if self.grid[self.y][i] == 0:
                    self.grid[self.y][i] = 1
                    x_add = x_add + 1
                else:
                    break
            self.x = self.x + x_add

        if direction == "left":
            x_add = 0
            for i in range(self.x-1, -1, -1):
                if self.grid[self.y][i] == 0:
                    self.grid[self.y][i] = 1
                    x_add = x_add + 1
                else:
                    break
            self.x = self.x - x_add

        if direction == "down":
            y_add = 0
            for i in range(self.y + 1, 5):
                if self.grid[i][self.x] == 0:
                    self.grid[i][self.x] = 1
                    y_add = y_add + 1
                else:
                    break
            self.y = self.y + y_add

        if direction == "up":
            y_add = 0
            for i in range(self.y-1, -1, -1):
                if self.grid[i][self.x] == 0:
                    self.grid[i][self.x] = 1
                    y_add = y_add + 1
                else:
                    break
            self.y = self.y - y_add

    def setLocation(self, y, x):
        if self.grid[y][x] == 1:
            print("The location is invalid")
        self.x = x
        self.y = y
        self.grid[y][x] = 1
        return self.checkOptions()

    def getGrid(self):
        return self.grid


    def checkOptions(self):
        up = True
        down = True
        left = True
        right = True
        _list = []
        if self.x == 4:
            right = False
        elif self.grid[self.y][self.x + 1] == 1:
            right = False
        if self.x == 0:
            left = False
        elif self.grid[self.y][self.x - 1] == 1:
            left = False
        if self.y == 4:
            down = False
        elif self.grid[self.y + 1][self.x] == 1:
            down = False
        if self.y == 0:
            up = False
        elif self.grid[self.y - 1][self.x] == 1:
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




