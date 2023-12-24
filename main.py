import pygame
from process import *

def main():
    # pygame setup
    pygame.init()
    pygame.display.set_caption("Eels and Escalators")

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    game = process(screen, clock)
    game.run()
    
if __name__ == "__main__":
    main()