import pygame
import scenes.start_menu as start_menu
import scenes.rule_menu as rule_menu

class process:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.current_scene = start_menu.scene(self.screen, self.clock)
        pygame.mouse.set_visible(False)
    
    def run(self):
        while self.running:
            
            next_scene = self.current_scene.run()
            
            if next_scene[0] == 0 or next_scene[0] == -1:
                self.running = False
            else:
                self.current_scene = next_scene[0](self.screen, self.clock, next_scene[1] if len(next_scene) > 1 else None)
        
        pygame.quit()