from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    '''l = Line(Point(50, 50), Point(400, 400))
    new_line = Line(Point(1, 300), Point(500, 300))
    win.draw_line(new_line, "red")
    win.draw_line(l, "black")'''
    mehtul_bawkses = Cell(win)
    mehtul_bawkses.has_bottom_wall = True
    mehtul_bawkses.has_top_wall = True
    mehtul_bawkses.has_left_wall = True
    #mehtul_bawkses.has_right_wall = True
    mehtul_bawkses.draw(50, 100, 300, 350)
    mehtul_bawkses2 = Cell(win)
    mehtul_bawkses2.has_bottom_wall = True
    mehtul_bawkses2.has_top_wall = True
    #mehtul_bawkses2.has_left_wall = True
    mehtul_bawkses2.has_right_wall = True
    mehtul_bawkses2.draw(310, 100, 560, 350)
    mehtul_bawkses.draw_move(mehtul_bawkses2)
    win.wait_for_close()

main()