from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if seed is not None:
            random.seed(seed)
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self._cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            dict_direction = {}
            need_to_go = []
            key = 0
            if i > 0 and not self._cells[i - 1][j].visited:
                need_to_go.append((i - 1, j))
                dict_direction[key] = "left" 
                key += 1  
            if i < self.__num_cols - 1 and not self._cells[i + 1][j].visited:
                need_to_go.append((i + 1, j))
                dict_direction[key] = "right"
                key += 1
            if j > 0 and not self._cells[i][j - 1].visited:
                need_to_go.append((i, j - 1))
                dict_direction[key] = "up"
                key += 1
            if j < self.__num_rows - 1 and not self._cells[i][j + 1].visited:
                need_to_go.append((i, j + 1))
                dict_direction[key] = "down"
            if key == 0:
                self._draw_cell(i, j)
                return
            rng = random.randrange(0, len(need_to_go))
            chosen = need_to_go[rng]
            direction = dict_direction[rng]
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            if direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            self._break_walls_r(chosen[0], chosen[1])
    
    def _reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        #if i == self.__num_cols - 1 and j == self.__num_rows - 1:
        if self._cells[i][j] == self._cells[self.__num_cols - 1][self.__num_rows - 1]:
            return True
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            check = self._solve_r(i - 1, j)
            if check is True:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        if i < self.__num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            check = self._solve_r(i + 1, j)
            if check is True:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            check = self._solve_r(i, j - 1)
            if check is True:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        if j < self.__num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            check = self._solve_r(i, j + 1)
            if check is True:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False
        
