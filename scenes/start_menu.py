import pygame
import scenes.ready_menu as ready_menu

class scene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        
        self.done = False
        self.next = [ready_menu.scene]
        self.background = pygame.image.load("resources\\start_menu_temp.png")

    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            condition = False
            if condition:
                self.done = True
            
            self.render()

            pygame.display.flip()

            self.clock.tick(60)
            
        if self.running == False:
            return 0
        elif self.done and condition:
            return self.next[0]
        else:
            return -1

    def render(self):
        pygame.Surface.blit(self.screen, self.background, (0, 0))