import Matrix
import pygame
import time
# from pygame.locals import *

BORDER_WIDTH = 12
HEADER_HEIGHT = 60
TILE_SIZE = 23
BORDER_LINE_WEIGHT = 3
DIFF_WIDTH = 100
DIFF_HEIGHT = 40
RESET_SIZE = 35

game_board = Matrix.Matrix()

############ Initiate pygame settings ###########
pygame.init()

# display_width = TILE_SIZE * board_col + 2*BORDER_WIDTH
# display_height = TILE_SIZE * board_row + 2*BORDER_WIDTH + HEADER_HEIGHT

display_width = TILE_SIZE * 30 + 2*BORDER_WIDTH
display_height = TILE_SIZE * 16 + 2*BORDER_WIDTH + HEADER_HEIGHT

display_width_middle = display_width / 2
display_height_middle = display_height / 2

# print(display_height)
# print(display_width)

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
reset_button = pygame.image.load('img/reset_button.png')
reset_button_pressed = pygame.image.load('img/reset_button_pressed.png')
reset_bombed = pygame.image.load('img/reset_bombed.png')
reset_win = pygame.image.load('img/reset_win.png')

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
pygame.display.set_caption('MineSweeper')
clock = pygame.time.Clock()
#################################################

#################### Colors #####################
background_grey = (158, 158, 158)
border_shadow = (100, 100, 100)
border_light = (244, 244, 244)
font_white = (255, 255, 255)
font_black = (0, 0, 0)
diff_easy_blue = (168, 201, 255)
diff_modest_blue = (124, 174, 255)
diff_hard_blue = (86, 151, 255)
diff_hov_blue = (37, 60, 96)
#################################################

############### Helper functions ################
def row_to_coord(row):
    return row * TILE_SIZE + BORDER_WIDTH + HEADER_HEIGHT

def col_to_coord(col):
    return col * TILE_SIZE + BORDER_WIDTH

def get_board_width(board_col):
    return TILE_SIZE * board_col + 2*BORDER_WIDTH

def get_board_height(board_row):
    return TILE_SIZE * board_row + 2*BORDER_WIDTH + HEADER_HEIGHT

def get_clicked_pos(mouse_pos, x_offset, y_offset):
    clicked_row = round((mouse_pos[1] - y_offset - 2*BORDER_WIDTH - HEADER_HEIGHT) / TILE_SIZE)
    clicked_col = round((mouse_pos[0] - x_offset - 2*BORDER_WIDTH) / TILE_SIZE)
    return (clicked_row, clicked_col)

def create_button(text, x, y, w, h, color, hov_color, text_color, text_hov_color, action = None):
    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf = smallText.render(text, True, text_color)
    
    mouse_pos = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if ((x+w > mouse_pos[0] and mouse_pos[0] > x) and 
        (y+h > mouse_pos[1] and mouse_pos[1] > y)):
        pygame.draw.rect(gameDisplay, hov_color,(x,y,w,h))
        textSurf = smallText.render(text, True, text_hov_color)
        if clicked[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, color,(x,y,w,h))
    
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
#################################################

############# GUI related functions #############
def place_tile(x, y):
    gameDisplay.blit(tile_unfliped,(x, y))

def draw_box(list_upper, list_lower):
    pygame.draw.lines(gameDisplay, border_shadow, False, list_upper, BORDER_LINE_WEIGHT)
    pygame.draw.lines(gameDisplay, border_light, False, list_lower, BORDER_LINE_WEIGHT)

def draw_all_boxes(board_top, board_bottom, board_left, board_right):
    outer_box_upper = [[board_right, board_top],
                       [board_right, board_bottom], 
                       [board_left, board_bottom]]
    outer_box_lower = [[board_left, board_bottom], 
                       [board_left, board_top], 
                       [board_right, board_top]]
    draw_box(outer_box_upper, outer_box_lower)

    upper_inner_upper = [[board_left+BORDER_WIDTH-BORDER_LINE_WEIGHT, board_top+HEADER_HEIGHT-BORDER_LINE_WEIGHT],
                         [board_left+BORDER_WIDTH-BORDER_LINE_WEIGHT, board_top+BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [board_right-BORDER_WIDTH+BORDER_LINE_WEIGHT, board_top+BORDER_WIDTH-BORDER_LINE_WEIGHT]]
    upper_inner_lower = [[board_right-BORDER_WIDTH+BORDER_LINE_WEIGHT, board_top+BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [board_right-BORDER_WIDTH+BORDER_LINE_WEIGHT, board_top+HEADER_HEIGHT-BORDER_LINE_WEIGHT],
                         [board_left+BORDER_WIDTH-BORDER_LINE_WEIGHT, board_top+HEADER_HEIGHT-BORDER_LINE_WEIGHT]]
    draw_box(upper_inner_upper, upper_inner_lower)

    lower_inner_upper = [[board_left+BORDER_WIDTH-BORDER_LINE_WEIGHT, board_bottom-BORDER_WIDTH+BORDER_LINE_WEIGHT],
                         [board_left+BORDER_WIDTH-BORDER_LINE_WEIGHT, board_top+HEADER_HEIGHT+BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [board_right-BORDER_WIDTH+BORDER_LINE_WEIGHT, board_top+HEADER_HEIGHT+BORDER_WIDTH-BORDER_LINE_WEIGHT]]
    lower_inner_lower = [[board_right-BORDER_WIDTH+BORDER_LINE_WEIGHT, board_top+HEADER_HEIGHT+BORDER_WIDTH-BORDER_LINE_WEIGHT],
                         [board_right-BORDER_WIDTH+BORDER_LINE_WEIGHT, board_bottom-BORDER_WIDTH+BORDER_LINE_WEIGHT],
                         [board_left+BORDER_WIDTH-BORDER_LINE_WEIGHT, board_bottom-BORDER_WIDTH+BORDER_LINE_WEIGHT]]
    draw_box(lower_inner_upper, lower_inner_lower)

def refresh_game_board(board_row, board_col, x_offset, y_offset):
    for x in range(board_row):
        for y in range(board_col):
            # Calculate pygame coordinates
            coord_y = row_to_coord(x)
            coord_x = col_to_coord(y)
            # Tile in fliped state
            if game_board.flagged[x][y] == True:
                gameDisplay.blit(flag,(coord_x+x_offset, coord_y+y_offset))
            elif game_board.status[x][y] == True:
                if game_board.board[x][y] == 1:
                    gameDisplay.blit(fliped_one,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 2:
                    gameDisplay.blit(fliped_two,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 3:
                    gameDisplay.blit(fliped_three,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 4:
                    gameDisplay.blit(fliped_four,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 5:
                    gameDisplay.blit(fliped_five,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 6:
                    gameDisplay.blit(fliped_six,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 7:
                    gameDisplay.blit(fliped_seven,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 8:
                    gameDisplay.blit(fliped_eight,(coord_x+x_offset, coord_y+y_offset))
                elif game_board.board[x][y] == 9:
                    gameDisplay.blit(mine,(coord_x+x_offset, coord_y+y_offset))
                else:
                    gameDisplay.blit(tile_pressed,(coord_x+x_offset, coord_y+y_offset))
            else:
                gameDisplay.blit(tile_unfliped,(coord_x+x_offset, coord_y+y_offset))

            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos = get_clicked_pos(pygame.mouse.get_pos(), x_offset, y_offset)
                if ((pos[0] >= 0 and pos[0] < board_row) and 
                    (pos[1] >= 0 and pos[1] < board_col) and
                    game_board.flagged[pos[0]][pos[1]] == False and
                    game_board.status[pos[0]][pos[1]] == False):
                    coord = (col_to_coord(pos[1])+x_offset, row_to_coord(pos[0])+y_offset)
                    gameDisplay.blit(tile_pressed, coord)

def set_reset_button(board_top, bombed, win):
    x_coord = display_width_middle - RESET_SIZE / 2
    y_coord = board_top + BORDER_LINE_WEIGHT + (HEADER_HEIGHT - RESET_SIZE) / 2
    if bombed:
        gameDisplay.blit(reset_bombed, (x_coord, y_coord))
    elif win:
        gameDisplay.blit(reset_win, (x_coord, y_coord))        
    else:
        gameDisplay.blit(reset_button, (x_coord, y_coord))

    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouse_pos = pygame.mouse.get_pos()
        if ((mouse_pos[0] > x_coord and mouse_pos[0] < x_coord + RESET_SIZE) and 
            (mouse_pos[1] > y_coord and mouse_pos[1] < y_coord + RESET_SIZE)):
            gameDisplay.blit(reset_button_pressed, (x_coord, y_coord))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    textSurf = largeText.render(text, True, font_white)
    textRect = textSurf.get_rect()
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

def reveal_mine(board_row, board_col, x_offset, y_offset):
    for x in range(board_row):
        for y in range(board_col):
            # Calculate pygame coordinates
            coord_y = row_to_coord(x)
            coord_x = col_to_coord(y)
            if game_board.board[x][y] == 9:
                gameDisplay.blit(mine,(coord_x+x_offset, coord_y+y_offset))
    pygame.display.update()
#################################################

################ Main game loop #################
def game_intro():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit")
                pygame.quit()
                quit()
                
        gameDisplay.fill(background_grey)
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf = largeText.render('Minesweeper!', True, font_white)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((display_width/2),HEADER_HEIGHT)
        gameDisplay.blit(TextSurf, TextRect)

        easy_pos = ((display_width/2)-50,(display_height/2)-30)
        modest_pos = ((display_width/2)-50,(display_height/2)+20)
        hard_pos = ((display_width/2)-50,(display_height/2)+70)

        # create_button(text, x, y, w, h, color, hov_color, text_color, text_hov_color)
        create_button('Easy', easy_pos[0], easy_pos[1], DIFF_WIDTH, DIFF_HEIGHT, 
                diff_easy_blue, diff_hov_blue, font_black, font_white, easy_game)
        create_button('Modest', modest_pos[0], modest_pos[1], DIFF_WIDTH, DIFF_HEIGHT, 
                diff_modest_blue, diff_hov_blue, font_black, font_white, modest_game)
        create_button('Hard', hard_pos[0], hard_pos[1], DIFF_WIDTH, DIFF_HEIGHT, 
                diff_hard_blue, diff_hov_blue, font_black, font_white, hard_game)     

        pygame.display.update()
        clock.tick(15)

def game_loop(board_row, board_col, board_mines):
    bombed = False

    board_width = get_board_width(board_col)
    board_height = get_board_height(board_row)

    board_width_middle = board_width / 2
    board_height_middle = board_height / 2

    board_top = display_height_middle-board_height_middle
    board_bottom = display_height_middle+board_height_middle
    board_left = display_width_middle-board_width_middle
    board_right = display_width_middle+board_width_middle

    game_board.reset(board_row, board_col, board_mines)
    game_board.get_count()
    game_board.print_board()

    gameDisplay.fill(background_grey)
    draw_all_boxes(board_top, board_bottom, board_left, board_right)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pass
                elif pygame.mouse.get_pressed() == (0, 0, 1):
                    pos = get_clicked_pos(pygame.mouse.get_pos(), board_left, board_top)
                    ######### Probably need to change #########
                    if pos[0] < 0 or pos[0] >= board_row or pos[1] < 0 or pos[1] >= board_col:
                        continue
                    ###########################################
                    if game_board.status[pos[0]][pos[1]] == True:
                        break
                    game_board.flagged[pos[0]][pos[1]] = not game_board.flagged[pos[0]][pos[1]]

                elif pygame.mouse.get_pressed() == (0, 1, 0):
                    print(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if (mouse_pos[0] > display_width_middle - RESET_SIZE / 2 and
                        mouse_pos[0] < display_width_middle + RESET_SIZE / 2 and
                        mouse_pos[1] > board_top + BORDER_LINE_WEIGHT + (HEADER_HEIGHT - RESET_SIZE) / 2 and
                        mouse_pos[1] < board_top + BORDER_LINE_WEIGHT + HEADER_HEIGHT / 2 + RESET_SIZE / 2):
                        print("Reset")
                        return True
                    pos = get_clicked_pos(mouse_pos, board_left, board_top)
                    ######### Probably need to change #########
                    if pos[0] < 0 or pos[0] >= board_row or pos[1] < 0 or pos[1] >= board_col:
                        continue
                    ###########################################
                    if game_board.flagged[pos[0]][pos[1]] == True:
                        break
                    game_board.reveal(pos[0], pos[1])
                    bombed = (game_board.board[pos[0]][pos[1]] == 9)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape")
                    return False
                if event.key == pygame.K_SPACE:
                    print("Restart")
                    return True
            if event.type == pygame.VIDEORESIZE:
                print('resize!')
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                gameDisplay.fill(background_grey)
                draw_all_boxes(board_top, board_bottom, board_left, board_right)

        win = game_board.count_revealed() == board_row * board_col - board_mines;

        refresh_game_board(board_row, board_col, board_left, board_top)
        set_reset_button(board_top, bombed, win)

        if win:
            message_display('Win!')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if (mouse_pos[0] > display_width_middle - RESET_SIZE / 2 and
                        mouse_pos[0] < display_width_middle + RESET_SIZE / 2 and
                        mouse_pos[1] > board_top + BORDER_LINE_WEIGHT + (HEADER_HEIGHT - RESET_SIZE) / 2 and
                        mouse_pos[1] < board_top + BORDER_LINE_WEIGHT + HEADER_HEIGHT / 2 + RESET_SIZE / 2):
                        print("Win")
                        return True

        if bombed:
            reveal_mine(board_row, board_col, board_left, board_top)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if (mouse_pos[0] > display_width_middle - RESET_SIZE / 2 and
                        mouse_pos[0] < display_width_middle + RESET_SIZE / 2 and
                        mouse_pos[1] > board_top + BORDER_LINE_WEIGHT + (HEADER_HEIGHT - RESET_SIZE) / 2 and
                        mouse_pos[1] < board_top + BORDER_LINE_WEIGHT + HEADER_HEIGHT / 2 + RESET_SIZE / 2):
                        print("Reset")
                        return True
        
        pygame.display.update()
        clock.tick(60)

def easy_game():
    cont = True
    while cont:
        cont = game_loop(9, 9, 10)

def modest_game():
    cont = True
    while cont:
        cont = game_loop(16, 16, 40)

def hard_game():
    cont = True
    while cont:
        cont = game_loop(16, 30, 99)
#################################################

game_intro()
    
pygame.quit()
quit()