from line import Line
from point import Point

class Cell():
    def __init__(self, win=None):
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1 #left
        self.__x2 = x2 #right
        self.__y1 = y1 #up
        self.__y2 = y2 #down
        if self.has_bottom_wall:
            wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "black")
        else:
            wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "white")
        if self.has_right_wall:
            wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "black")
        else:
            wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "white")
        if self.has_top_wall:
            wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(wall, "black")
        else:
            wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(wall, "white")
        if self.has_left_wall:
            wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(wall, "black")
        else:
            wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(wall, "white")
        
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        to_center_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_center_y = (to_cell.__y1 + to_cell.__y2) / 2
        self.__win.draw_line(Line(Point(center_x, center_y), Point(to_center_x, to_center_y)), color)
