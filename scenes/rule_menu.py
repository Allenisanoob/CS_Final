import pygame
from library.button import *
from library.mouse import *
import scenes.ready_menu as ready_menu

def game_logic():
    pass
class scene:
    def __init__(self, screen, clock, *args):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ready_menu.scene]
        self.background = pygame.image.load("resources\\rules.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        pygame.mouse.set_visible(False)
        
        self.button_0 = button(self.screen, image = "resources\\start_button.png")
        self.button_0.x = screen.get_width() // 2 - self.button_0.width // 2
        self.button_0.y = screen.get_height() // 2 - self.button_0.height // 2 + 175
        
    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.load("resources\\sounds\\laugh.mp3")
                    pygame.mixer.music.play()
            
            if self.button_0.clicked:
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return 0
        elif self.done and self.button_0.clicked:
            return [self.next[0]]
        else:
            return -1

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.button_0.draw()
        self.allsprites.update()
        self.allsprites.draw(self.screen)

