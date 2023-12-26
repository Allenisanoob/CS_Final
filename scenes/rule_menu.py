import pygame
import scenes.ready_menu as ready_menu

class scene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.done = False
        self.next = [ready_menu.scene]
        self.background = pygame.image.load("resources\\遊戲規則.png")
        
        self.mouse = Mouse()
        self.allsprites = pygame.sprite.Group(self.mouse)
        pygame.mouse.set_visible(False)
        
    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.load("resources\\sounds\\laugh.mp3")
                    pygame.mixer.music.play()

            condition = False
            if condition:
                self.done = True
            
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
            
        if not self.running:
            return 0
        elif self.done and condition:
            return self.next[0]
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