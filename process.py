import pygame
import scenes.start_menu as start_menu
import scenes.rule_menu as rule_menu

class process:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.current_scene = start_menu.scene(self.screen, self.clock)
    
    def run(self):
        while self.running:
                    
            next_scene = self.current_scene.run()
            
            if next_scene == 0 or next_scene == -1:
                self.running = False
            else:
                self.current_scene = next_scene(self.screen, self.clock)
        
        pygame.quit()