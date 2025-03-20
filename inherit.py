
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Square:
    def __init__(self, color, border_width, filled, side_size_a):
        self.color = color
        self.border_width = border_width
        self.filled = filled
        self.side_size_a = side_size_a

    def draw(self):
        fig, ax = plt.subplots()
        square = patches.Rectangle((0, 0), self.side_size_a, self.side_size_a, linewidth=self.border_width, edgecolor=self.color,facecolor=self.color if self.filled else 'none')


        ax.add_patch(square)
        ax.set_xlim(-1, self.side_size_a + 1)
        ax.set_ylim(-1, self.side_size_a + 1)
        ax.set_aspect('equal', 'box')
        plt.title("Квадрат")
        plt.show()

    def info(self):
        return (f"Квадрат: цвет = {self.color}, Ширина границы = {self.border_width}, "
                f"Заливка = {self.filled}, Сторона A = {self.side_size_a}")

    def __del__(self):
        print(f"Квадрат удален.")


class Quadrilateral:
    def __init__(self, color, border_width, filled, side_size_a, side_size_b, side_size_c, side_size_d):
        self.color = color
        self.border_width = border_width
        self.filled = filled
        self.side_size_a = side_size_a
        self.side_size_b = side_size_b
        self.side_size_c = side_size_c
        self.side_size_d = side_size_d

    def draw(self):
        fig, ax = plt.subplots()
        
        points = [(0, 0), (self.side_size_a, 0),(self.side_size_a, self.side_size_b), (0, self.side_size_c)]
        quadrilateral = patches.Polygon(points, closed=True, linewidth=self.border_width, edgecolor=self.color, facecolor=self.color if self.filled else 'none')
        
        
        ax.add_patch(quadrilateral)
        ax.set_xlim(-1, max(self.side_size_a, self.side_size_c) + 1)
        ax.set_ylim(-1, max(self.side_size_b, self.side_size_d) + 1)
        ax.set_aspect('equal', 'box')
        plt.title("Четырехугольник")
        plt.show()

    def info(self):
        return (f"Четырехугольник: цвет = {self.color}, Ширина границы = {self.border_width}, "
                f"Заливка = {self.filled}, Стороны: A = {self.side_size_a}, B = {self.side_size_b}, "
                f"C = {self.side_size_c}, D = {self.side_size_d}")

    def __del__(self):
        print(f"Четырехугольник удален.")



