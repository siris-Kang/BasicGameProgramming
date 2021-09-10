import random
import os
import time
import msvcrt

class Snake:
    def __init__(self, n):
        self.length = n
        self.head = [] #머리위치 [a, b]
        self.tail = [] #꼬리위치 [a, b]

class SnakeGame:
    direction = {"LEFT":-2, "DOWN":-1, "NON_DIR":0, "UP":1, "RIGHT":2}
    sprite = {"EMPTY":0, "BODY":1, "HEAD":2, "FOOD":3}
    element = {"SPRITE":0, "DIRECTION":1} #SPRITE: 몸이냐 머리냐 먹이냐 비어있냐 하는 상태
    
    def __init__(self, w, h, length, delay):
        self.W = w
        self.H = h
        self.initLen = length
        self.snake = Snake(length)
        self.delay = delay
        self.board = [[[0]*2 for x in range(self.W)] for y in range(self.H)]

        self.snake.head = [self.H//2, self.snake.length-1]
        self.snake.tail = [self.H//2, 0]

        for i in range(0, self.snake.length):
            self.board[self.H//2][i][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
            self.board[self.H//2][i][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["RIGHT"] #꼬리 입력

        self.board[self.H//2][self.snake.length-1][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
        self.board[self.H//2][self.snake.length-1][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["RIGHT"] #머리 입력

        
        x = random.randint(0, self.W-1)
        y = random.randint(0, self.H-1)
        while self.board[y][x][SnakeGame.element["SPRITE"]] != SnakeGame.sprite["EMPTY"]:
            x = random.randint(0, self.W-1)
            y = random.randint(0, self.H-1)

        self.board[y][x][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["FOOD"] #비어있는 경우에 먹이 랜덤 배치

    def DrawScene(self):
        os.system('cls||clear')
        for x in range(0, self.W+2):
            print("=", end="")
        print("")
        for y in range(0, self.H):
            print("|", end="")
            for x in range(0, self.W):
                if self.board[y][x][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["BODY"]:
                    print("+", end="")
                elif  self.board[y][x][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["HEAD"]:
                    print("@", end="")
                elif  self.board[y][x][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("|")

        for x in range(0, self.W+2):
            print("=", end="")
        print("")
                

    @staticmethod #객체를 만들지 않고 바로 method사용 가능
    def GetDirection():
        rtn = SnakeGame.direction["NON_DIR"]
        msvcrt.getch()
        ch = msvcrt.getch().decode()
        
        if ch == chr(72):
            print("UP")
            rtn = SnakeGame.direction["UP"]
        elif ch == chr(75):
            print("LEFT")
            rtn = SnakeGame.direction["LEFT"]
        elif ch == chr(77):
            print("RIGHT")
            rtn = SnakeGame.direction["RIGHT"]
        elif ch == chr(80):
            print("DOWN")
            rtn = SnakeGame.direction["DOWN"]
        return rtn

    def RandomFeed(self):
        x = random.randint(0, self.W-1)
        y = random.randint(0, self.H-1)
        while self.board[y][x][SnakeGame.element["SPRITE"]] != SnakeGame.sprite["EMPTY"]:
            x = random.randint(0, self.W-1)
            y = random.randint(0, self.H-1)
        self.board[y][x][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["FOOD"]

    def CalDirection(self, dir, lst): #int, array, shallow copy
        if (dir == SnakeGame.direction["UP"]):
            lst[0] -= 1
        elif (dir == SnakeGame.direction["LEFT"]):
            lst[1] -= 1
        elif (dir == SnakeGame.direction["RIGHT"]):
            lst[1] += 1
        elif (dir == SnakeGame.direction["DOWN"]):
            lst[0] += 1

    #Game Loop
    def GameLoop(self):
        self.DrawScene()
        current = SnakeGame.direction["RIGHT"]
        while True: #Loop 시작
            start = time.time()
            eat = False
            while (time.time() - start) <= self.delay/1000:
                if msvcrt.kbhit():
                    temp = SnakeGame.GetDirection()
                    if (temp != -current):
                        current = temp
            
            self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
            self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = current
            self.CalDirection(current, self.snake.head)

            if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["BODY"]\
                or self.snake.head[0] <0 or self.snake.head[0] >= self.H or self.snake.head[1] <0 or self.snake.head[1] >= self.W):
                return None

            if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]):
                self.snake.length += 1
                eat = True
                self.RandomFeed()

            self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
            if (eat == False):
                tailDir = self.board[self.snake.tail[0]][self.snake.tail[1]][SnakeGame.element["DIRECTION"]]
                self.board[self.snake.tail[0]][self.snake.tail[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["EMPTY"]
                self.board[self.snake.tail[0]][self.snake.tail[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["NON_DIR"]
                self.CalDirection(tailDir, self.snake.tail)
            eat = False
              
            self.DrawScene()
            print("Score: {}".format(self.snake.length - self.initLen))

if __name__ == '__main__' :
    game = SnakeGame(60, 24, 4, 100)
    game.GameLoop()