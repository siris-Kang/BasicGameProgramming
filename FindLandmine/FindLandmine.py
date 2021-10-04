import tkinter as tk
import numpy as np
import random
import tkinter.messagebox

from numpy.core.fromnumeric import size

class GameFrame:
    def __init__(self, _size_width, _size_height):
        self.size_width = _size_width
        self.size_height = _size_height
        # num(boom = -1), opne(TF)
        self.pattern = [[[0]*3 for i in range(self.size_width)] for k in range(self.size_height)]
        self.mark_boom()
        self.fill_num()

    # make landmine in map
    def mark_boom(self):
        i = 0
        if (self.size_width ==9): # boom = 10
            while (i < 10):
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if (self.pattern[y][x][0] != -1):
                    self.pattern[y][x][0] = -1
                    i += 1
        elif (self.size_width == 16):
            while (i < 40):
                x = random.randint(0, 15)
                y = random.randint(0, 15)
                if (self.pattern[y][x][0] != -1):
                    self.pattern[y][x][0] = -1
                    i += 1
        else:
            while (i < 99):
                x = random.randint(0, 29)
                y = random.randint(0, 15)
                if (self.pattern[y][x][0] != -1):
                    self.pattern[y][x][0] = -1
                    i += 1
    # fill array
    def fill_num(self):
        for i in range(self.size_width):
            for j in range(self.size_height):
                if (self.pattern[j][i][0] == -1):
                    self.determin_num(i, j)

    def determin_num(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j ==0):
                    continue
                if x+i < 0:
                    continue
                elif x+i >= self.size_width: 
                    continue
                elif y+j < 0:
                    continue
                elif y+j >= self.size_height:
                    continue
                if self.pattern[y+j][x+i][0] == -1:
                    continue
                self.pattern[y+j][x+i][0] +=1

    def open_tile(self, x, y):
        self.pattern[y][x][1] = 1
        return self.pattern[y][x][0] # boom = -1 or num return

    def is_open(self, x, y):
        return self.pattern[y][x][1] # not open = 0, open = 1

    def open_right_tile(self, x, y):
        self.pattern[y][x][2] = 1
        return self.pattern[y][x][2]

    def close_right_tile(self, x, y):
        self.pattern[y][x][2] = 0
        return self.pattern[y][x][2]

    def is_right_open(self, x, y):
        return self.pattern[y][x][2]

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 9
        self.height = 9
        self.square = 30
        self.landmine = GameFrame(self.width, self.height)
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width*self.square, height=self.height*self.square,)
        self.set_game(self.width, self.height)
        self.menu(master)

        self.canvas.pack()
        self.pack()

    def set_game(self, width: int, height: int):
        self.canvas.destroy()
        self.width = width
        self.height = height
        self.landmine = GameFrame(self.width, self.height)
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width*self.square, height=self.height*self.square)
        for i in range(self.width):
            self.canvas.create_line(i * self.square, 0, i * self.square, self.height*self.square)
        for j in range(self.height):
            self.canvas.create_line(0, j * self.square, self.width*self.square, j * self.square)
        self.canvas.pack()
        self.pack()

        self.canvas.bind('<Button-1>', self.left_button)
        self.canvas.bind('<Button-3>', self.right_button)

    def left_button(self, event):
        self.finish_game()
        x = event.x//self.square
        y = event.y//self.square
        if (self.landmine.is_open(x, y)):
            pass
        else:
            if (self.landmine.pattern[y][x][0] == -1):
                self.landmine.open_tile(x, y)
                self.draw_text(self.width*self.square/2-15, self.height*self.square/2-15, "Game Over", 30)
                # 지뢰의 위치를 list에 넣어놓았다면, 폭탄의 위치를 보여줄 수 있을텐데
            elif (self.landmine.pattern[y][x][0] == 0):
                self.detect_region(x, y)
            else:
                self.draw_text(x*self.square, y*self.square, self.landmine.open_tile(x, y), 20)

    def right_button(self, event):
        self.finish_game()
        x = event.x//self.square
        y = event.y//self.square
        if (self.landmine.is_right_open(x, y) == 0):
            self.landmine.open_right_tile(x, y)
            self.draw_text(x*self.square, y*self.square, "⁂", 20)
        elif (self.landmine.is_right_open(x, y) == 1):
            self.landmine.close_right_tile(x, y)
            self.erase_text(x*self.square, y*self.square)

    def draw_text(self, x, y, text, size='40'):
        font = ('Helvetica', size)
        return self.canvas.create_text(x+15, y+15, text=text, font=font)
    def erase_text(self, x, y):
        return self.canvas.delete(x+15, y+15)

    def detect_region(self, x, y): # press 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x+i < 0:
                    continue
                if x+i >= self.width: 
                    continue
                if y+j < 0:
                    continue
                if y+j >= self.height:
                    continue
                if (self.landmine.is_open(x+i, y+j)):
                    continue
                self.draw_text((x+i)*self.square, (y+j)*self.square, self.landmine.pattern[y+j][x+i][0], 20)
                self.landmine.open_tile(x+i, y+j)
                if (self.landmine.pattern[y+j][x+i][0] == 0):
                    self.detect_region(x+i, y+j)

    def finish_game(self):
        for i in range(self.width):
            for j in range(self.height):
                if (self.landmine.pattern[j][i][0] == -1 and self.landmine.pattern[j][i][2] == 1):
                    pass
                else:
                    return
        tk.messagebox.showinfo('Win', 'You win!')

    def menu(self, master):
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="9*9", command = lambda: self.set_game(width=9, height=9))
        filemenu.add_command(label="16*16", command = lambda: self.set_game(width=16, height=16))
        filemenu.add_command(label="30*16", command = lambda: self.set_game(width=30, height=16))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command = master.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Find Landmine')
    game = Game(root)
    game.mainloop()