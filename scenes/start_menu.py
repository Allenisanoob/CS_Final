import pygame
from library.button import *
from library.mouse import *
import scenes.rule_menu as rule_menu
import scenes.ready_menu1 as ready_menu1

def game_logic():
    pass
class scene:
    def __init__(self, screen, clock,*args):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ready_menu1.scene, rule_menu.scene]
        self.background = pygame.image.load("resources\\start_menu.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        
        #Creating start button
        self.button_0 = button(self.screen, image = "resources\\start_button.png",
                               image_hover="resources\\start_button_hover.png")
        self.button_0.set_pos(screen.get_width() // 2 - self.button_0.width // 2,
                              screen.get_height() // 2 - self.button_0.height // 2 - 55)
        
        #Creating rule button
        self.button_1 = button(self.screen, image = "resources\\rule_button.png",
                               image_hover="resources\\rule_button_hover.png")
        self.button_1.set_pos(screen.get_width() // 2 - self.button_0.width // 2,
                              screen.get_height() // 2 - self.button_0.height // 2 + 25)
        
    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_pos = pygame.mouse.get_pos()
                    if 540 < mouse_pos[0] < 840 and 600 < mouse_pos[1] < 660:
                        self.done = True
                    
                    pygame.mixer.music.load("resources\\sounds\\laugh.mp3")
                    pygame.mixer.music.play()
            
            if self.button_0.clicked:
                next_scene = 0
                self.done = True   
            elif self.button_1.clicked:
                next_scene = 1
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return [0]
        elif self.done :
            return [self.next[next_scene]]
        else:
            return [-1]

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.button_0.draw()
        self.button_1.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)
