import pygame
import gameboard
from variables import SCREENWIDTH, SCREENHEIGHT, CAPTION, FPS, BLACK, BACKGROUNDGREY, titleFont



WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption(CAPTION)

def main():
    run = True
    MaxFPS = FPS
    squares = []
    clock = pygame.time.Clock()

    gameboard.createSquares(squares)

    def redraw_window():
        
        WIN.fill(BACKGROUNDGREY)
        for square in squares:
            square.draw(WIN)

        pygame.display.update()

    while run:

        clock.tick(MaxFPS)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # left
            delay +=1

        redraw_window()


            





def main_menu():
    
    run = True

    while run:

        WIN.fill(BLACK)
        titleLabel = titleFont.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(titleLabel, (SCREENWIDTH/2 - titleLabel.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


main_menu()