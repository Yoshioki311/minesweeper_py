import Matrix
# import pygame

# Initiate pygame settings
# pygame.init()
# gameDisplay = pygame.display.set_mode((800,600))
# pygame.display.set_caption('MineSweeper')
# clock = pygame.time.Clock()

board_col = input("How wide should the board be? ")
board_row = input("How tall should the board be? ")
board_mines = input("how many mines should there be? ")

board_row = int(board_row)
board_col = int(board_col)
board_mines = int(board_mines)

game_board = Matrix.Matrix()
game_board.resize(board_row, board_col, board_mines)
game_board.get_count()
game_board.print_board()
game_board.print_mask()

user_row = input("Enter the row you would like to reveal: ")
user_col = input("Enter the column you would like to reveal: ")
user_row = int(user_row) - 1
user_col = int(user_col) - 1

game_state = game_board.reveal(user_row, user_col)
game_board.print_mask()
