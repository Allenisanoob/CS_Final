import pygame
from library.button import *
from library.mouse import *
import scenes.ready_menu1 as ready_menu

def game_logic():
    pass
class scene:
    def __init__(self, screen, clock, *args):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ready_menu.scene]
        self.background = pygame.image.load("resources\\end_menu.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        pygame.mouse.set_visible(False)
        
        self.button_0 = button(self.screen, image = "resources\\restart_button.png")
        self.button_0.x = screen.get_width() // 2 - self.button_0.width // 2 - 250
        self.button_0.y = screen.get_height() // 2 - self.button_0.height // 2 -220

        self.button_1 = button(self.screen, image = "resources\\quit_button.png")
        self.button_1.x = screen.get_width() // 2 - self.button_1.width // 2 + 250
        self.button_1.y = screen.get_height() // 2 - self.button_1.height // 2 - 220
        
    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if self.button_0.clicked or self.button_1.clicked:
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return 0
        elif self.done and self.button_0.clicked:
            return [self.next[0]]
        elif self.done and self.button_1.clicked:
            return -1
        else:
            return -1

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.button_0.draw()
        self.button_1.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)
