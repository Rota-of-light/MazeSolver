from tkinter import Tk, BOTH, Canvas
from point import Point

class Line():
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas, color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2
        )
