from game_force_move import start_game
import pygame

pygame.init()
menu = True


height = 800
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Checker")
screen.fill((255, 255, 255))
string = ""
played = False
color = (0, 0, 0)
while menu:
    
    font = pygame.font.Font(None, 36)
    if not played:
        text = font.render("Press any key to start", True, (0, 0, 0))
    else:
        text = font.render("Press any key to exit", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width//2, height//2))
    screen.blit(text, text_rect)
    text_win = font.render(string, True, color)
    text_win_rect = text_win.get_rect(center=(width//2, height//2 + 50))
    screen.blit(text_win, text_win_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.KEYDOWN:    
            if not played:
                string = ""
                color = (0, 0, 0)
                string, color = start_game()
                screen.fill((255, 255, 255))
                played = True
            else:
                menu = False
    pygame.display.flip()

