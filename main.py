from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    #point_1 = Point(10, 20)
    #point_2 = Point(20, 20)
    l = Line(Point(50, 50), Point(400, 400))
    new_line = Line(Point(1, 300), Point(500, 300))
    win.draw_line(new_line, "red")
    win.draw_line(l, "black")
    win.wait_for_close()

main()