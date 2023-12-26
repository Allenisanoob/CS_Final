import pygame
from library.button import *
from library.mouse import *
import scenes.ready_menu as ready_menu
import scenes.rule_menu as rule_menu

def game_logic():
    pass
class scene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ready_menu.scene, rule_menu.scene]
        self.background = pygame.image.load("resources\\start_menu.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        
        #Creating start button
        self.button_0 = button(self.screen, image = "resources\\start_button.png")
        self.button_0.x = screen.get_width() // 2 - self.button_0.width // 2
        self.button_0.y = screen.get_height() // 2 - self.button_0.height // 2 - 250
        
        #Creating rule button
        self.button_1 = button(self.screen, image = "resources\\start_button.png")
        self.button_1.x = screen.get_width() // 2 - self.button_1.width // 2
        self.button_1.y = screen.get_height() // 2 - self.button_1.height // 2 + 250
        
    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.load("resources\\sounds\\laugh.mp3")
                    pygame.mixer.music.play()
            
            if self.button_0.clicked or self.button_1.clicked:
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return 0
        elif self.done and self.button_0.clicked:
            return self.next[0]
        elif self.done and self.button_1.clicked:
            return self.next[1]
        else:
            return -1

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.button_0.draw()
        self.button_1.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)
