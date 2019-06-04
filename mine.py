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

# game_board = Matrix.Matrix()
# game_board.resize(board_row, board_col, board_mines)
# game_board.get_count()
# game_board.print_board()
# game_board.print_mask()

############ Initiate pygame settings ###########
pygame.init()

display_width = TILE_SIZE * board_col + 2*BORDER_WIDTH
display_height = TILE_SIZE * board_row + 2*BORDER_WIDTH + HEADER_HEIGHT

print(display_height)
print(display_width)

bombed = False

tile_unfliped = pygame.image.load('img/tile.png')
tile_pressed = pygame.image.load('img/tile_pressed.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MineSweeper')
clock = pygame.time.Clock()
#################################################

#################### Colors #####################
background_grey = (158, 158, 158)
border_shadow = (100, 100, 100)
border_light = (244, 244, 244)
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
#################################################

gameDisplay.fill(background_grey)

draw_all_boxes()

# Draw tiles
print("Drawing tiles")
for i in range(board_col):
        for j in range(board_row):
            place_tile(i * TILE_SIZE + BORDER_WIDTH, j * TILE_SIZE + BORDER_WIDTH + HEADER_HEIGHT)

while not bombed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bombed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if pygame.mouse.get_pressed() == (1, 0, 0):
                clicked_pos = pygame.mouse.get_pos()
                
                clicked_row = round((clicked_pos[1] - 2*BORDER_WIDTH - HEADER_HEIGHT) / TILE_SIZE)
                clicked_col = round((clicked_pos[0] - 2*BORDER_WIDTH) / TILE_SIZE)

                pressed_pos_x = clicked_col*TILE_SIZE + BORDER_WIDTH
                pressed_pos_y = clicked_row*TILE_SIZE + BORDER_WIDTH + HEADER_HEIGHT
                gameDisplay.blit(tile_pressed,(pressed_pos_x, pressed_pos_y))

                print("Col: " + str(clicked_col)) #col
                print("Row: " + str(clicked_row)) #row
            elif pygame.mouse.get_pressed() == (0, 1, 0):
                print(pygame.mouse.get_pos())
    # print(event)
    
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
