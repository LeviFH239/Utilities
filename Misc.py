class Grid:
    def __init__(self, fill_value, width, height):
        self.fill_value = fill_value
        self.width = width
        self.height = height

        self.data = [[fill_value for _ in range(self.width)] for _ in range(self.height)]


grid = Grid(0, 10, 5)
print(grid.data)