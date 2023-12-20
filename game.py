from tkinter import *
from random import randint


class Game:
    # Инициализация
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[9, 9]]
        self.apple_coords = [randint(0, 19) for _ in range(2)]
        self.vector = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.game()

    # Метод для нового положения яблока
    def set_apple(self):
        self.apple_coords = [randint(0, 19) for _ in range(2)]
        # Условие, для того чтобы яблоко не лежало на змейке
        if self.apple_coords in self.snake_coords:
            self.set_apple()

    # Установка нового направления змейки
    def set_direction(self, event):
        # Условие, которое проверяет нажатие кнопки
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]

    # Отрисовка игры
    def draw(self):
        self.canvas.delete(ALL)
        x_apple, y_apple = self.apple_coords
        self.canvas.create_oval(x_apple * 20, y_apple * 20, (x_apple + 1) * 20, (y_apple + 1) * 20, fill="brown3",
                                outline="brown4", width=2)
        for x, y in self.snake_coords:
            self.canvas.create_oval(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="chartreuse3",
                                    outline="green", width=2)

    # Метод, который возращает координаты на интервале [0, 19]
    @staticmethod
    def coord_check(coord):
        return 0 if coord > 19 else 19 if coord < 0 else coord

    # Логика игры
    def game(self):
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0]
        y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.apple_coords[0] and y == self.apple_coords[1]:
            self.set_apple()
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x, y])
        self.canvas.after(100, self.game)


# Каркас игры
root = Tk()
canvas = Canvas(root, width=400, height=400, bg="pink")
canvas.pack()
game = Game(canvas)
img = PhotoImage(file='C:\\Users\\Ivan\\Desktop\\змейка.png')
root.iconphoto(False, img)
root.title("Змейка")
root.mainloop()
