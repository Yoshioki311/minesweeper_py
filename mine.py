import Matrix
import pygame

BORDER_WIDTH = 12
HEADER_HEIGHT = 50
TILE_SIZE = 23
BORDER_LINE_WEIGHT = 3

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
# game_board.print_mask()

############ Initiate pygame settings ###########
pygame.init()

display_width = TILE_SIZE * board_col + 2*BORDER_WIDTH
display_height = TILE_SIZE * board_row + 2*BORDER_WIDTH + HEADER_HEIGHT

print(display_height)
print(display_width)

quit_game = False
bombed = False

tile_unfliped = pygame.image.load('img/tile.png')
tile_pressed = pygame.image.load('img/tile_pressed.png')
fliped_one = pygame.image.load('img/fliped_one.png')
fliped_two = pygame.image.load('img/fliped_two.png')
fliped_three = pygame.image.load('img/fliped_three.png')
fliped_four = pygame.image.load('img/fliped_four.png')
fliped_five = pygame.image.load('img/fliped_five.png')
fliped_six = pygame.image.load('img/fliped_six.png')
fliped_seven = pygame.image.load('img/fliped_seven.png')
fliped_eight = pygame.image.load('img/fliped_eight.png')
mine = pygame.image.load('img/mine.png')
flag = pygame.image.load('img/flag.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MineSweeper')
clock = pygame.time.Clock()
#################################################

#################### Colors #####################
background_grey = (158, 158, 158)
border_shadow = (100, 100, 100)
border_light = (244, 244, 244)
#################################################

############### Helper functions ################
def row_to_coord(row):
    return row * TILE_SIZE + BORDER_WIDTH + HEADER_HEIGHT

def col_to_coord(col):
    return col * TILE_SIZE + BORDER_WIDTH

def get_clicked_pos(mouse_pos):
    clicked_row = round((mouse_pos[1] - 2*BORDER_WIDTH - HEADER_HEIGHT) / TILE_SIZE)
    clicked_col = round((mouse_pos[0] - 2*BORDER_WIDTH) / TILE_SIZE)
    return (clicked_row, clicked_col)
#################################################

############# GUI related functions #############
def place_tile(x, y):
    gameDisplay.blit(tile_unfliped,(x, y))

def draw_box(list_upper, list_lower):
    pygame.draw.lines(gameDisplay, border_shadow, False, list_upper, BORDER_LINE_WEIGHT)
    pygame.draw.lines(gameDisplay, border_light, False, list_lower, BORDER_LINE_WEIGHT)

def draw_all_boxes():
    outer_box_upper = [[display_width-BORDER_LINE_WEIGHT, 0],
                       [display_width-BORDER_LINE_WEIGHT, display_height-BORDER_LINE_WEIGHT], 
                       [0, display_height-BORDER_LINE_WEIGHT]]
    outer_box_lower = [[0, display_height-BORDER_LINE_WEIGHT], 
                       [0, 0], 
                       [display_width-BORDER_LINE_WEIGHT, 0]]
    draw_box(outer_box_upper, outer_box_lower)

    upper_inner_upper = [[BORDER_WIDTH-BORDER_LINE_WEIGHT, HEADER_HEIGHT-BORDER_LINE_WEIGHT],
                         [BORDER_WIDTH-BORDER_LINE_WEIGHT, BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [display_width-BORDER_WIDTH+BORDER_LINE_WEIGHT, BORDER_WIDTH-BORDER_LINE_WEIGHT]]
    upper_inner_lower = [[display_width-BORDER_WIDTH+BORDER_LINE_WEIGHT, BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [display_width-BORDER_WIDTH+BORDER_LINE_WEIGHT, HEADER_HEIGHT-BORDER_LINE_WEIGHT],
                         [BORDER_WIDTH-BORDER_LINE_WEIGHT, HEADER_HEIGHT-BORDER_LINE_WEIGHT]]
    draw_box(upper_inner_upper, upper_inner_lower)

    lower_inner_upper = [[BORDER_WIDTH-BORDER_LINE_WEIGHT, display_height-BORDER_WIDTH+BORDER_LINE_WEIGHT],
                         [BORDER_WIDTH-BORDER_LINE_WEIGHT, HEADER_HEIGHT+BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [display_width-BORDER_WIDTH+BORDER_LINE_WEIGHT, HEADER_HEIGHT+BORDER_WIDTH-BORDER_LINE_WEIGHT]]
    lower_inner_lower = [[display_width-BORDER_WIDTH+BORDER_LINE_WEIGHT, HEADER_HEIGHT+BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [display_width-BORDER_WIDTH+BORDER_LINE_WEIGHT, display_height-BORDER_WIDTH+BORDER_LINE_WEIGHT],
                         [BORDER_WIDTH-BORDER_LINE_WEIGHT, display_height-BORDER_WIDTH+BORDER_LINE_WEIGHT]]
    draw_box(lower_inner_upper, lower_inner_lower)

def refresh_game_board():
    for x in range(board_row):
        for y in range(board_col):
            # Calculate pygame coordinates
            coord_y = row_to_coord(x)
            coord_x = col_to_coord(y)
            # Tile in fliped state
            if game_board.flagged[x][y] == True:
                gameDisplay.blit(flag,(coord_x, coord_y))
            elif game_board.status[x][y] == True:
                if game_board.board[x][y] == 1:
                    gameDisplay.blit(fliped_one,(coord_x, coord_y))
                elif game_board.board[x][y] == 2:
                    gameDisplay.blit(fliped_two,(coord_x, coord_y))
                elif game_board.board[x][y] == 3:
                    gameDisplay.blit(fliped_three,(coord_x, coord_y))
                elif game_board.board[x][y] == 4:
                    gameDisplay.blit(fliped_four,(coord_x, coord_y))
                elif game_board.board[x][y] == 5:
                    gameDisplay.blit(fliped_five,(coord_x, coord_y))
                elif game_board.board[x][y] == 6:
                    gameDisplay.blit(fliped_six,(coord_x, coord_y))
                elif game_board.board[x][y] == 7:
                    gameDisplay.blit(fliped_seven,(coord_x, coord_y))
                elif game_board.board[x][y] == 8:
                    gameDisplay.blit(fliped_eight,(coord_x, coord_y))
                elif game_board.board[x][y] == 9:
                    gameDisplay.blit(mine,(coord_x, coord_y))
                else:
                    gameDisplay.blit(tile_pressed,(coord_x, coord_y))
            else:
                gameDisplay.blit(tile_unfliped,(coord_x, coord_y))
#################################################

gameDisplay.fill(background_grey)
draw_all_boxes()

while not quit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = get_clicked_pos(pygame.mouse.get_pos())
                if pos[0] < 0 or pos[0] >= board_row or pos[1] < 0 or pos[1] >= board_col:
                    continue
                if game_board.flagged[pos[0]][pos[1]] == True:
                    break
                game_board.reveal(pos[0], pos[1])
                bombed = (game_board.board[pos[0]][pos[1]] == 9)
                # print(bombed)
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                pos = get_clicked_pos(pygame.mouse.get_pos())
                if pos[0] < 0 or pos[0] >= board_row or pos[1] < 0 or pos[1] >= board_col:
                    continue
                if game_board.status[pos[0]][pos[1]] == True:
                    break
                game_board.flagged[pos[0]][pos[1]] = not game_board.flagged[pos[0]][pos[1]]

            elif pygame.mouse.get_pressed() == (0, 1, 0):
                print(pygame.mouse.get_pos())

    refresh_game_board()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

    # user_row = input("Enter the row you would like to reveal: ")
    # user_col = input("Enter the column you would like to reveal: ")
    # user_row = int(user_row) - 1
    # user_col = int(user_col) - 1

    # game_state = game_board.reveal(user_row, user_col)
    # game_board.print_mask()