import random

class Matrix(object):
    def __init__(self):
        # Game info
        self.col = 0
        self.row = 0
        self.mines = 0
        self.mine_loc = []

        # Board related
        self.board = []
        self.status = []
        self.flagged = []

    def reset(self, row, col, mines):
        self.row = row # Number of rows of the board
        self.col = col # Number of cols of the board
        self.mines = mines # Number of mines on the board

        # Array containing mine location
        self.mine_loc = []
        for i in range(mines):
            rand_loc = [random.randint(0, row - 1), random.randint(0, col - 1)]
            for loc in self.mine_loc:
                while rand_loc == loc:
                    rand_loc = [random.randint(0, row - 1), random.randint(0, col - 1)]
            self.mine_loc.append(rand_loc)
        
        # Initiate game board
        self.board = []
        for x in range(row):
            self.board.append([])
            for y in range(col):
                loc = [x, y]
                is_mine = False
                for i in range(len(self.mine_loc)):
                    if loc == self.mine_loc[i]:
                        is_mine = True
                if is_mine:
                    self.board[x].append(9)
                else:
                    self.board[x].append(0)

        # Initiate game cell status
        self.status = []
        for x in range(row):
            self.status.append([])
            for y in range(col):
                self.status[x].append(False)

        self.flagged = []
        for x in range(row):
            self.flagged.append([])
            for y in range(col):
                self.flagged[x].append(False)
    def reveal(self, row, col):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return
        if self.status[row][col] == True:
            return
        
        if self.board[row][col] != 0:
            self.status[row][col] = True
            return
        else:
            self.status[row][col] = True
            self.reveal(row+1, col)
            self.reveal(row-1, col)
            self.reveal(row, col+1)
            self.reveal(row, col-1)
            self.reveal(row+1, col+1)
            self.reveal(row-1, col+1)
            self.reveal(row+1, col-1)
            self.reveal(row-1, col-1)
    def get_count(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 9:
                    # print("case 1")
                    continue
                if x > 0:
                    if y > 0 and self.board[x-1][y-1] == 9:
                        # print("case 2")
                        self.board[x][y] = self.board[x][y] + 1
                    
                    if self.board[x-1][y] == 9:
                        # print("case 3")
                        self.board[x][y] = self.board[x][y] + 1
                    if y < len(self.board[x]) - 1 and self.board[x-1][y+1] == 9:
                        # print("case 4")
                        self.board[x][y] = self.board[x][y] + 1

                if y> 0 and self.board[x][y-1] == 9:
                    # print("case 5")
                    self.board[x][y] = self.board[x][y] + 1
                if y < len(self.board[x]) - 1 and self.board[x][y+1] == 9:
                    # print("case 6")
                    self.board[x][y] = self.board[x][y] + 1
                
                if x < len(self.board) - 1:
                    if y > 0 and self.board[x+1][y-1] == 9:
                        # print("case 7")
                        self.board[x][y] = self.board[x][y] + 1
                    if self.board[x+1][y] == 9:
                        # print("case 8")
                        self.board[x][y] = self.board[x][y] + 1
                    if y < len(self.board[x]) - 1 and self.board[x+1][y+1] == 9:
                        # print("case 9")
                        self.board[x][y] = self.board[x][y] + 1
        
    ################### Utility Functions ####################
    def print_board(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                print(self.board[x][y], end=" ")
            print(" ")
        print("\n")
    ##########################################################
