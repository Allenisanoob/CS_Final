import pygame
from library.button import *
import scenes.ingame as ingame
import scenes.rule_menu as rule_menu
import scenes.ready_menu as ready_menu

def game_logic():
    pass
class scene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ingame.scene]
        self.background = pygame.image.load("resources\\ready_menu.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        pygame.mouse.set_visible(False)
        
        #Creating start button
        self.button_0 = button(self.screen, image = "resources\\start_button.png")
        self.button_0.x = screen.get_width() // 2 - self.button_0.width // 2 
        self.button_0.y = screen.get_height() // 2 - self.button_0.height // 2 + 280
        
        #Creating rule button
        self.button_1 = button(self.screen, image = "resources\\me.png")
        self.button_1.x = 29
        self.button_1.y = screen.get_height() // 2 - self.button_1.height // 2 
        
    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 0 < mouse_pos[0] < 255 and 200 < mouse_pos[1] < 520 :
                        self.button_1.x = 29
                        n = 1
                    if 255 < mouse_pos[0] < 510 and 200 < mouse_pos[1] < 520 :
                        self.button_1.x = 283
                        n = 2               
                    if 510 < mouse_pos[0] < 765 and 200 < mouse_pos[1] < 520 :
                        self.button_1.x = 542
                        n = 3 
                    if 765 < mouse_pos[0] < 1020 and 200 < mouse_pos[1] < 520 :
                        self.button_1.x = 798
                        n = 4
       
            if self.button_0.clicked:
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return 0
        elif self.done and self.button_0.clicked:
            return self.next[0]
        else:
            return -1

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.button_0.draw()
        self.button_1.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image('resources\\cursor_temp.png')
        self.rect.topleft = (0, 0)  
    
    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()

    def load_image(self, name):
        image = pygame.image.load(name)
        image = image.convert()
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect()
