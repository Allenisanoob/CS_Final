import pygame
import random
from moviepy.editor import VideoFileClip
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
    
    def __init__(self, screen, clock, *args):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.mouse = Mouse()
        
        #States of the scene.
        self.turn = 1
        self.processing = False
        self.done = False
        self.winner = None
        
        #Put all the "next scenes" in this list.
        self.next = [end_menu.scene]
        
        #Load background image here.
        self.background = pygame.image.load("resources\\map.png")
        self.image_1 = pygame.image.load(f"resources\\{args[0][0]}.png")
        self.image_1_place = self.image_1.get_rect()
        self.image_1_place.topleft = (15, 100)
        self.image_2 = pygame.image.load(f"resources\\{args[0][1]}.png")
        self.image_2_place = self.image_2.get_rect()
        self.image_2_place.topleft = (885, 100)
        
        player1_image = pygame.transform.scale(pygame.image.load("resources\\weichen1.png").convert(), (72, 72))
        player2_image = pygame.transform.scale(pygame.image.load("resources\\weichen2.png").convert(), (72, 72))
        self.player1 = player(self.screen, player1_image, 15, -25)
        self.player2 = player(self.screen, player2_image, 0, -15)
        self.players = [None, self.player1, self.player2]
        self.allsprites = pygame.sprite.Group(self.mouse, self.player1, self.player2)

        self.video = VideoFileClip("resources\\rolling_dice_1020x720.mp4")
        
        #Creating roll button
        self.button_0 = button(self.screen, x = 900, y = 620, width = 50, height = 50, color = (255, 255, 255))    #Need image here.
        #Creating cheat button
        self.button_win1 = button(self.screen, x = 900, y = 460, width = 50, height = 50, color = (173, 216, 230))    #Need image here.
        self.button_win2 = button(self.screen, x = 900, y = 540, width = 50, height = 50, color = (255, 127, 127))    #Need image here.

    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #Put the condition to end the scene here, if there are more than one, use "and" or "or" to combine them.
            if not self.winner is None:
                self.done = True

            #Make K_SPACE activate button_0.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.button_0.pressed = True

            self.game_logic()

            self.render()
            
            pygame.display.flip()

            self.clock.tick(60)
            
        if self.running == False:
            return [0]
        #Use the condition to choose the next scene here, if there are more than one, use multiple elif.
        elif self.done and not self.winner is None:
            return (self.next[0], (self.winner))
        else:
            return [-1]

    #Put all the renderings here.
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.image_1, self.image_1_place)
        self.screen.blit(self.image_2, self.image_2_place)
        self.button_0.draw()
        self.button_win1.draw()
        self.button_win2.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)
    
    def play_animation(self, dices):
        image = pygame.image.load(f"resources\\dice\\dice_{dices[0][0]}{dices[0][1]}{dices[1][0]}{dices[1][1]}.png")
        self.video.preview()
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(1500)

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
            pool1 = ((1, 1), (1, 2), (0, 1), (0, 2), (0, 3), (0, 4))
            pool2 = ((0, 1), (0, 2), (1, 1), (1, 2), (1, 3), (1, 4))
            return random.choice(pool1), random.choice(pool2)
        
        if (self.player1.block == 100 or self.player2.block == 100) and not self.processing:
            self.winner = 1 if self.player1.block == 100 else 2
            return
        
        if self.button_win1.clicked and not self.processing:
            self.turn = 1
            self.processing = True
            self.players[self.turn].block = 100
            self.players[self.turn].dest = get_coord(100)

        if self.button_win2.clicked and not self.processing:
            self.turn = 2
            self.processing = True
            self.players[self.turn].block = 100
            self.players[self.turn].dest = get_coord(100)
        
        if self.button_0.released and not self.processing:
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
                for i in range(8):
                    if self.players[self.turn].block <= self.ladder_start[i]:
                        self.players[self.turn].block = self.ladder_end[i]
                        self.players[self.turn].dest = get_coord(self.ladder_start[i])
                        break
            else:
                next_block = self.players[self.turn].block + dices[0][1] + dices[1][1]
                if next_block > 100:
                    self.players[self.turn].block = 100
                    self.players[self.turn].dest = get_coord(100)
                elif next_block in self.snake_start:
                    index = self.snake_start.index(next_block)
                    self.players[self.turn].block = self.snake_end[index]
                    self.players[self.turn].dest = get_coord(self.snake_start[index])
                elif next_block in self.ladder_start:
                    index = self.ladder_start.index(next_block)
                    self.players[self.turn].block = self.ladder_end[index]
                    self.players[self.turn].dest = get_coord(self.ladder_start[index])
                else:
                    self.players[self.turn].dest = get_coord(next_block)
                    self.players[self.turn].block = next_block
                        
            #Play animation here.
            self.play_animation(dices)
                    
            # print(dices)
            # print(self.turn)
            # print(self.players[1].block, self.players[2].block)
        
        if self.processing:
            if dist(self.players[self.turn].get_pos(), self.players[self.turn].dest) < 3:
                self.players[self.turn].x = self.players[self.turn].dest[0] + self.players[self.turn].xoffset
                self.players[self.turn].y = self.players[self.turn].dest[1] + self.players[self.turn].yoffset
                if self.players[self.turn].dest == get_coord(self.players[self.turn].block):
                    self.processing = False
                    self.turn = 3 - self.turn
                else:
                    self.players[self.turn].dest = get_coord(self.players[self.turn].block)
            else:
                self.players[self.turn].move(speed(self.players[self.turn].get_pos(), self.players[self.turn].dest))
