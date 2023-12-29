import os
import pygame
from library.button import *
from library.mouse import *
import scenes.ingame as ingame

def game_logic():
    pass
class scene:
    def __init__(self, screen, clock, *args):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.n = args[0]
        self.done = False
        self.next = [ingame.scene]
        self.background = pygame.image.load(os.path.join("resources", "ready_menu.png"))
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        pygame.mouse.set_visible(False)
        
        #Creating next button
        self.button_0 = button(self.screen, image = os.path.join("resources", "next_button.png"),
                               image_hover = os.path.join("resources", "next_button_hover.png"))
        self.button_0.set_pos(screen.get_width() // 2 - self.button_0.width // 2,
                              screen.get_height() // 2 - self.button_0.height // 2 + 280)
        
        #Creating selecting figure
        self.button_1 = button(self.screen, image = os.path.join("resources", "me2.png"), remove_bg = False)
        self.button_1.set_pos(x = 29,
                              y = screen.get_height() // 2 - self.button_1.height // 2)
        
    def run(self):
        n = 1
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 0 < mouse_pos[0] < 255 and 200 < mouse_pos[1] < 520 :
                        self.button_1.set_pos(29, self.button_1.y)
                        n = 1
                    if 255 < mouse_pos[0] < 510 and 200 < mouse_pos[1] < 520 :
                        self.button_1.set_pos(283, self.button_1.y)
                        n = 2               
                    if 510 < mouse_pos[0] < 765 and 200 < mouse_pos[1] < 520 :
                        self.button_1.set_pos(542, self.button_1.y)
                        n = 3 
                    if 765 < mouse_pos[0] < 1020 and 200 < mouse_pos[1] < 520 :
                        self.button_1.set_pos(798, self.button_1.y)
                        n = 4
       
            if self.button_0.clicked:
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return [0]
        elif self.done:
            return [self.next[0], (self.n ,n)]
        else:
            return [-1]

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.button_0.draw()
        self.button_1.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)