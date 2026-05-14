import matplotlib.pyplot as plt

class Grid:
    def __init__(self, fill_value, width, height):
        self.fill_value = fill_value
        self._width = width
        self._height = height

        self.border_thickness = 0
        self.border_value = self.fill_value

        self.data = [[self.fill_value for _ in range(self.width)] for _ in range(self.height)]

        self._history = []

    def get_value(self, x, y):
        return self.data[y][x]

    @property
    def history(self):
        return self._history

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
        self.update_grid()

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
        self.update_grid()

    def add_border(self, border_thickness, border_value):
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if c < border_thickness or c > self.width - border_thickness - 1 or r < border_thickness or r > self.height - border_thickness - 1:
                    self.data[r][c] = border_value
                elif col == border_value:
                    self.data[r][c] = self.fill_value
        self.border_thickness = border_thickness
        self.border_value = border_value

    def append_value(self, value, x, y):
        self.data[y][x] = value
        self.history.append((value, x, y))


    def update_grid(self):
        self.add_border(self.border_thickness, self.border_value)

        for value, x, y in self.history:
            self.data[y][x] = value


    def draw_line(self, value, x, y, dx, dy, size):
        if not (-1 <= dx <= 1 and -1 <= dy <= 1):
            return

        end_x = x + dx * (size - 1)
        end_y = y + dy * (size - 1)

        if not (0 <= end_x < self.width and 0 <= end_y < self.height):
            return

        for _ in range(size):
            self.append_value(value, x, y)
            x += dx
            y += dy

    def draw_rect(self, value, x, y, width, height):
        for _ in range(height):
            for _ in range(width):
                self.append_value(value, x, y)
                x += 1
            x = x - width
            y += 1

grid = Grid((255, 255, 255), 30, 30)
grid.add_border(1, (0, 0, 0))

grid.draw_rect((0, 0, 0), 10, 10, 9, 9)
grid.draw_rect((255, 255, 255), 12, 12, 5, 5)

plt.imshow(grid.data)
plt.axis('off')
plt.show()
