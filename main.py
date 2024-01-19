#import libraries & modules
import sys
import pygame
 
def run_game():
    #initializing the pygame
    pygame.init()

    #setting screen size, icons, titles of the game
    screen=pygame.display.set_mode((1200,800))
    icon=pygame.image.load('images/ufo.png')
    player=pygame.image.load('images/ship.png')
    pygame.display.set_caption("Alien Invasion")
    pygame.display.set_icon(icon)


    #creating a loop for the game.
    run=True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        pygame.display.flip()
        screen.fill((0,0,0))
        pygame.display.update()
run_game()
