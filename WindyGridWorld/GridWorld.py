import numpy as np

class GridWorld:
    def __init__(self, rows=7, cols=15):
        self.rows = rows
        self.cols = cols

    def MakeGrid(self):
        self.grid = np.zeros((self.rows,self.cols),dtype='float16')

    def DefineStartEnd(self, start = [3,3], end = [5,12]):
        self.start = start
        self.end = end


    def Unattractive_Border(self):
        self.grid[0:3, :] = -100
        self.grid[-3:, :] = -100
        self.grid[:, 0:3] = -100
        self.grid[:, -3:] = -100

    def MakeRandomGrid(self,terminus="zero"):
        self.grid = np.random.uniform(low=0.0, high=1.0, size=(self.rows, self.cols))

        if terminus =="zero":
            self.grid[self.end[0],self.end[1]] = 0

    def UpdateGrid(self,position, Q_update):
        self.grid[position[0],position[1]] = Q_update

    def AddWind(self,wind="const"):
        if wind == "const":
            # add weak wind from 1/3 to 1/2 of the grid
            a = int(self.cols/3)
            b = int(self.cols/2)
            self.grid[:,a:b+1] = 1

            # add stronger wind from 1/2 to 60 % of the grid
            a = b + 1
            b = int(0.6 * cols)
            self.grid[:,a:b+1] = 2

            # add weak wind again from 60 % to 80 % of the grid
            a = b + 1
            b = int(0.8 * cols)
            self.grid[:,a:b] = 1


        elif wind == "random":
            print("has to be programmed")
            return 0


    def GetGrid(self):
        return self.grid
