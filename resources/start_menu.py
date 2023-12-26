import pygame
import scenes.ready_menu as ready_menu
import scenes.rule_menu as rule_menu

class scene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ready_menu.scene , rule_menu.scene]
        self.background = pygame.image.load("resources\\開始.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        pygame.mouse.set_visible(False)
        
    def run(self):
        choose = 0
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_pos = pygame.mouse.get_pos()
                    if 540 < mouse_pos[0] < 840 and 600 < mouse_pos[1] < 660:
                        choose = 1
                        self.done = True
                        print(mouse_pos)
                    
                    pygame.mixer.music.load("resources\\sounds\\laugh.mp3")
                    pygame.mixer.music.play()
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return 0
        elif self.done and choose == 1:
            return self.next[1]
        elif self.done and choose == 2:
            return self.next[2]
        else:
            return -1

    def render(self):
        self.screen.blit(self.background, (0, 0))
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
