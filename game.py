import pygame


class Que:
    def __init__(self):
        self.queue = []

    def append(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
# Initialize Pygame
pygame.init()
selected_checker = None
# Set up the game window
window_width = 900  
window_height = 900
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Checkers Game")
def all_posible_moves(selected_checker, checkers):
    moves = []
    if selected_checker:
        color, row, col = selected_checker
        if color[1] == "UP":
                # Check if the move is diagonal and forward
            if (row - 1, col - 1) not in checkers:
                moves.append(((row - 1, col - 1),None))
            if (row - 1, col + 1) not in checkers:
                moves.append(((row - 1, col + 1),None))
            # Check for possible captures
            que= Que()
            que.append(((row, col),[]))
            while(not que.is_empty()):
                cord, eaten = que.dequeue()
                start_row, start_col = cord      
                if (start_row - 2, start_col - 2) not in checkers and (start_row - 1, start_col - 1) in checkers and checkers[(start_row - 1, start_col - 1)][0] != color[0]:
                    moves.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                    que.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                if (start_row - 2, start_col + 2) not in checkers and (start_row - 1, start_col + 1) in checkers and checkers[(start_row - 1, start_col + 1)][0] != color[0]:
                    moves.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                    que.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
        elif color[1] == "Dawn":
                # Check if the move is diagonal and forward
            if (row + 1, col - 1) not in checkers:
                moves.append(((row + 1, col - 1),None))
            if (row + 1, col + 1) not in checkers:
                moves.append(((row + 1, col + 1),None))
            # Check for possible captures
            que= Que()
            que.append(((row, col),[]))
            while(not que.is_empty()):
                cord, eaten = que.dequeue()
                start_row, start_col = cord
                if (start_row + 2, start_col - 2) not in checkers and (start_row + 1, start_col - 1) in checkers and checkers[(start_row + 1, start_col - 1)][0] != color[0]:
                    moves.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                    que.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                if (start_row + 2, start_col + 2) not in checkers and (start_row + 1, start_col + 1) in checkers and checkers[(start_row + 1, start_col + 1)][0] != color[0]:
                    moves.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
                    que.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
        elif color[1] == "KING":
            if (row - 1, col - 1) not in checkers:
                moves.append(((row - 1, col - 1),None))
            if (row - 1, col + 1) not in checkers:
                moves.append(((row - 1, col + 1),None))
            if (row + 1, col - 1) not in checkers:
                moves.append(((row + 1, col - 1),None))
            if (row + 1, col + 1) not in checkers:
                moves.append(((row + 1, col + 1),None))
            
            # Check for possible captures
            been_to = {}
            que= Que()
            que.append(((row, col),[]))
            while(not que.is_empty()):
                cord, eaten = que.dequeue()
                start_row, start_col = cord                     
                been_to[(start_row, start_col)] = True
                if (start_row - 2, start_col - 2) not in checkers and (start_row - 1, start_col - 1) in checkers and checkers[(start_row - 1, start_col - 1)][0] != color[0]:
                    if not been_to.get((start_row - 2, start_col - 2)):
                        moves.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                        que.append(((start_row - 2, start_col - 2),eaten + [(start_row - 1, start_col - 1)]))
                if (start_row - 2, start_col + 2) not in checkers and (start_row - 1, start_col + 1) in checkers and checkers[(start_row - 1, start_col + 1)][0] != color[0]:
                    if not been_to.get((start_row - 2, start_col + 2)):
                        moves.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                        que.append(((start_row - 2, start_col + 2), eaten + [(start_row - 1, start_col + 1)]))
                if (start_row + 2, start_col - 2) not in checkers and (start_row + 1, start_col - 1) in checkers and checkers[(start_row + 1, start_col - 1)][0] != color[0]:
                    if not been_to.get((start_row + 2, start_col - 2)):
                        moves.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                        que.append(((start_row + 2, start_col - 2), eaten + [(start_row + 1, start_col - 1)]))
                if (start_row + 2, start_col + 2) not in checkers and (start_row + 1, start_col + 1) in checkers and checkers[(start_row + 1, start_col + 1)][0] != color[0]:
                    if not been_to.get((start_row + 2, start_col + 2)):    
                        moves.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
                        que.append(((start_row + 2, start_col + 2), eaten + [(start_row + 1, start_col + 1)]))
    return moves


# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
move = RED
# Define the board size
board_size = 8
# Define the size of each square on the board
square_size = window_width // board_size
checkers = {}
# Game loop
for row in range(board_size):
    for col in range(board_size):
        if (row + col) % 2 == 1:
            if row < 3:
                checkers[(row, col)] = (RED, "Dawn")
            elif row > 4:
                checkers[(row, col)] = (BLUE , "UP")
running = True
posible_moves = []
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill(WHITE)
    # Draw the board
    
    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 == 0:
                pygame.draw.rect(window, WHITE, (col * square_size, row * square_size, square_size, square_size))

            else:
                pygame.draw.rect(window, BLACK, (col * square_size, row * square_size, square_size, square_size))
    for key in checkers:
        row, col = key
        color = checkers[key][0]
        type = checkers[key][1]
        if type != "KING":
            pygame.draw.circle(window, color, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 10)  
        else:
            pygame.draw.circle(window, color, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 10)  
            pygame.draw.circle(window, GREY, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 40)
    ##Check for mouse click eventx


    for moves in posible_moves:
        row, col = moves[0]
        pygame.draw.circle(window, GREY, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 40)
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        row = y // square_size
        col = x // square_size
        if (row, col) in checkers:
            # Get the selected checker
            if checkers[(row, col)][0] == move:
                selected_checker = (checkers[(row, col)],row, col)
                posible_moves = all_posible_moves(selected_checker, checkers)
        if selected_checker:
            for moves in posible_moves:
                if (row, col) == moves[0]:
                    if moves[1]:
                        for eaten in moves[1]:
                            if eaten in checkers:
                                del checkers[eaten]
                    if row == 0 and selected_checker[0][1] == "UP" or row == 7 and selected_checker[0][1] == "Dawn":
                        checkers[(row, col)] = (selected_checker[0][0], "KING")
                    else:
                        checkers[(row, col)] = selected_checker[0]
                    
                    del checkers[(selected_checker[1], selected_checker[2])]
                    selected_checker = None
                    posible_moves = []
                    if move == RED:
                        move = BLUE
                    else:
                        move = RED 
    pygame.display.update()
    # Quit the game
pygame.quit()