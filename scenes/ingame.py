import pygame
from library.button import *
from library.mouse import *

class player(pygame.sprite.Sprite):
    
    def __init__(self, screen, image, xoffset, yoffset):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = self.block_one[0] + xoffset
        self.y = self.block_one[1] + yoffset
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        
    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y
        
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
class scene:
    #Class variables
    ladder_start = (2, 4, 9, 21, 28, 51, 72, 80)
    ladder_end = (37, 14, 31, 42, 84, 67, 91, 99)
    snake_start = (17, 54, 62, 64, 87, 93, 95, 98)
    snake_end = (7, 34, 19, 60, 36, 73, 75, 79)
    block_one = (150, 649)
    block_width = 72
    
    def __init__(self, screen, clock, n,*args):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.mouse = Mouse()
        
        #Ture if the scene is ended by regular procedure.
        self.done = False
        
        #Put all the "next scenes" in this list.
        self.next = []
        
        #Load background image here.
        self.background = pygame.image.load("resources\\map.png")
        self.image_1 = pygame.image.load("resources\\0.png")
        self.image_1_place = self.image_1.get_rect()
        self.image_1_place.topleft = (885, 100)
        self.image_2 = pygame.image.load(f"resources\\{n}.png")
        self.image_2_place = self.image_2.get_rect()
        self.image_2_place.topleft = (15, 100)
        self.allsprites = pygame.sprite.Group(self.mouse)

    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #Put the condition to end the scene here, if there are more than one, use "and" or "or" to combine them.
            condition = False
            if condition:
                self.done = True

            self.render()
            
            self.game_logic()
            
            pygame.display.flip()

            self.clock.tick(60)
            
        if self.running == False:
            return 0
        #Use the condition to choose the next scene here, if there are more than one, use multiple elif.
        elif self.done and condition:
            return [self.next[0],0]
        else:
            return -1

    #Put all the renderings here.
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.image_1, self.image_1_place)
        self.screen.blit(self.image_2, self.image_2_place)
        self.allsprites.update()
        self.allsprites.draw(self.screen)
        
    #Calculations and game logic should be put here.
    def game_logic(self):
        
        def get_coord(block):
            if block % 20 >= 11:
                xx = 20 - block
            else:
                xx = block - 1
            yy = (block - 1) // 10
            
            x, y = (self.block_one[0] + xx * self.block_width, self.block_one[1] - yy * self.block_width)
            return (x, y)
        
        def speed(start_block, end_block):
            start_x, start_y = get_coord(start_block)
            end_x, end_y = get_coord(end_block)
            return ((end_x - start_x) / 10, (end_y - start_y) / 10)
        
        pass
