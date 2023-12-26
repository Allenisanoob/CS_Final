import pygame
import random
from library.button import *
from library.mouse import *
import scenes.end_menu as end_menu

class player(pygame.sprite.Sprite):
    
    #Clasee variables
    block_one = (150, 649)
    
    def __init__(self, screen, image, xoffset, yoffset):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.block = 1
        self.dest = None
        self.check = False
        self.x = self.block_one[0] + xoffset
        self.y = self.block_one[1] + yoffset
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.image = image
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def move(self, speed):
        self.x += speed[0]
        self.y += speed[1]
    
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
    
    def get_pos(self):
        return (self.x - self.xoffset, self.y - self.yoffset)
    
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
        
        #States of the scene.
        self.turn = 0
        self.processing = False
        self.done = False
        self.winner = None
        
        #Put all the "next scenes" in this list.
        self.next = [end_menu.scene]
        
        #Load background image here.
        self.background = pygame.image.load("resources\\map.png")
        self.image_1 = pygame.image.load("resources\\0.png")
        self.image_1_place = self.image_1.get_rect()
        self.image_1_place.topleft = (885, 100)
        self.image_2 = pygame.image.load(f"resources\\{n}.png")
        self.image_2_place = self.image_2.get_rect()
        self.image_2_place.topleft = (15, 100)
        player0_image = pygame.transform.scale(pygame.image.load("resources\\weichen0.png").convert(), (72, 72))
        player1_image = pygame.transform.scale(pygame.image.load("resources\\weichen1.png").convert(), (72, 72))
        self.player0 = player(self.screen, player0_image, 15, -25)
        self.player1 = player(self.screen, player1_image, 0, -15)
        self.players = [self.player0, self.player1]
        self.allsprites = pygame.sprite.Group(self.mouse, self.player0, self.player1)
        
        #Creating roll button
        self.button_0 = button(self.screen, x = 900, y = 620, width = 50, height = 50)    #Need image here.

    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #Put the condition to end the scene here, if there are more than one, use "and" or "or" to combine them.
            if not self.winner is None:
                self.done = True

            self.game_logic()

            self.render()
            
            pygame.display.flip()

            self.clock.tick(60)
            
        if self.running == False:
            return 0
        #Use the condition to choose the next scene here, if there are more than one, use multiple elif.
        elif self.done and not self.winner is None:
            return (self.next[0], (self.winner))
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
        def dist(a, b):
            return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
        
        def get_coord(block):
            if (block - 1) % 20 >= 10:
                xx = 19 - (block - 1) % 20
            else:
                xx = block % 20 - 1
            yy = (block - 1) // 10
            
            x, y = (self.block_one[0] + xx * self.block_width, self.block_one[1] - yy * self.block_width)
            return (x, y)
        
        def speed(pos, end):
            remain_distance = dist(pos, end)
            if remain_distance < 15:
                return ((end[0] - pos[0]) / remain_distance, (end[1] - pos[1]) / remain_distance)
            else:
                return ((end[0] - pos[0]) / 15, (end[1] - pos[1]) / 15)
        
        def roll():
            pool1 = ((0, 1), (0, 2), (1, 1), (1, 2), (1, 3), (1, 4))
            pool2 = ((1, 1), (1, 2), (0, 1), (0, 2), (0, 3), (0, 4))
            return random.choice(pool1), random.choice(pool2)
        
        if (self.player0.block == 100 or self.player1.block == 100) and not self.processing:
            self.winner = 0 if self.player0.block == 100 else 1
            return
        
        if self.button_0.clicked and not self.processing:
            self.processing = True
            no_object = False
            dices = roll()
            
            if ((self.players[self.turn].block <= 16 and dices[0][0] == 0 and dices[1][0] == 0) or
                (self.players[self.turn].block >= 81 and dices[0][0] == 1 and dices[1][0] == 1)):
                no_object = True
                
            if dices[0][0] == 0 and dices[1][0] == 0 and not no_object:
                for i in range(7, -1, -1):
                    if self.players[self.turn].block >= self.snake_start[i]:
                        self.players[self.turn].block = self.snake_end[i]
                        self.players[self.turn].dest = get_coord(self.snake_start[i])
                        break
            elif dices[0][0] == 1 and dices[1][0] == 1 and not no_object:
                for i in range(7):
                    if self.players[self.turn].block <= self.ladder_start[i]:
                        self.players[self.turn].block = self.ladder_end[i]
                        self.players[self.turn].dest = get_coord(self.ladder_start[i])
                        break
            else:
                next_block = self.players[self.turn].block + dices[0][1] + dices[1][1]
                if self.players[self.turn].block > 100:
                    self.players[self.turn].block = 100
                elif next_block in self.snake_start:
                    index = self.snake_start.index(next_block)
                    self.players[self.turn].block = self.snake_end[index]
                    self.players[self.turn].dest = get_coord(self.snake_start[index])
                elif next_block in self.ladder_start:
                    index = self.ladder_start.index(next_block)
                    self.players[self.turn].block = self.ladder_end[index]
                    self.players[self.turn].dest = get_coord(self.ladder_start[index])
                else:
                    self.players[self.turn].dest = get_coord(self.players[self.turn].block)
                        
            #Play animation here.
            print(dices)
            print(self.turn)
            print(self.players[0].block, self.players[1].block)
        
        if self.processing:
            if dist(self.players[self.turn].get_pos(), self.players[self.turn].dest) < 3:
                self.players[self.turn].x = self.players[self.turn].dest[0] + self.players[self.turn].xoffset
                self.players[self.turn].y = self.players[self.turn].dest[1] + self.players[self.turn].yoffset
                if self.players[self.turn].dest == get_coord(self.players[self.turn].block):
                    self.processing = False
                    self.turn = 1 - self.turn
                else:
                    self.players[self.turn].dest = get_coord(self.players[self.turn].block)
            else:
                self.players[self.turn].move(speed(self.players[self.turn].get_pos(), self.players[self.turn].dest))
        
        self.button_0.draw()