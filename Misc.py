class Grid:
    def __init__(self, fill_value, width, height):
        self.fill_value = fill_value
        self._width = width
        self._height = height

        self.border_thickness = 0
        self.border_value = self.fill_value

        self.data = [[self.fill_value for _ in range(self.width)] for _ in range(self.height)]

    def get_value(self, x, y):
        return self.data[y][x]

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < self.width:
            for _ in range(self.width - value):
                for row in self.data:
                    row.pop()
        elif value > self.width:
            for _ in range(value - self.width):
                for row in self.data:
                    row.append(self.fill_value)
        self._width = value
        self.add_border(self.border_thickness, self.border_value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):

        if value < self.height:
            for _ in range(self.height - value):
                self.data.pop()
        elif value > self.height:
            for _ in range(value - self.height):
                self.data.append([self.fill_value for _ in range(self.width)])
        self._height = value
        self.add_border(self.border_thickness, self.border_value)

    def add_border(self, border_thickness, border_value):
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if c < border_thickness or c > self.width - border_thickness - 1 or r < border_thickness or r > self.height - border_thickness - 1:
                    self.data[r][c] = border_value
                elif col == border_value:
                    self.data[r][c] = self.fill_value
        self.border_thickness = border_thickness
        self.border_value = border_value


grid = Grid(0, 10, 10)
grid.add_border(1, 1)
grid.height = 3
grid.width = 3
for row in grid.data:
    print(row)