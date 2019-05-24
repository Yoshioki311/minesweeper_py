import random
import pygame

class Matrix(object):
    def __init__(self):
        self.col = 0
        self.row = 0
        self.mines = 0
        self.board = []
    def resize(self, row, col, mines):
        self.row = row
        self.col = col
        self.mines = mines
        self.mine_loc = []
        for i in range(mines):
            rand_loc = [random.randint(0, row - 1), random.randint(0, col - 1)]
            self.mine_loc.append(rand_loc)
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
        self.mask = []
        for x in range(row):
            self.mask.append([])
            for y in range(col):
                self.mask[x].append('-')
    def print_board(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                print(self.board[x][y], end=" ")
            print(" ")
        print("\n")
    def print_mask(self):
        for x in range(len(self.mask)):
            for y in range(len(self.mask[x])):
                print(self.mask[x][y], end=" ")
            print(" ")
        print("\n")
    def reveal(self, row, col):
        if self.board[row][col] == 9:
            return False
        elif self.board[row][col] != 0:
            self.mask[row][col] = self.board[row][col]
            return True
        else:
            self.mask[row][col] = self.board[row][col]
            return True
        # else:
        #     self.mask[row][col] = self.board[row][col]
        #     while row  self.board[row][col] == 0:
        #         if row > 0:
        #             self.mask[row-1][col] = self.board[row-1][col]
        #         if row < self.row - 1:
        #             self.mask[row+1][col] = self.board[row+1][col]
        #         if col > 0:
        #             self.mask[row][col-1] = self.board[row][col-1]
        #         if col < self.col - 1:
        #             self.mask[row][col+1] = self.board[row][col+1]
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
        
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('MineSweeper')

board_col = input("How wide should the board be? ")
board_row = input("How tall should the board be? ")
board_mines = input("how many mines should there be? ")

board_row = int(board_row)
board_col = int(board_col)
board_mines = int(board_mines)

game_board = Matrix()
game_board.resize(board_row, board_col, board_mines)
game_board.get_count()
game_board.print_board()
game_board.print_mask()

# hi = Matrix()
# hi.resize(9, 9, 10)
# hi.print_board()
# hi.get_count()
# hi.print_board()

user_row = input("Enter the row you would like to reveal: ")
user_col = input("Enter the column you would like to reveal: ")
user_row = int(user_row) - 1
user_col = int(user_col) - 1

game_state = game_board.reveal(user_row, user_col)
game_board.print_mask()
