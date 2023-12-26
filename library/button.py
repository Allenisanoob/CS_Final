import pygame

class button():
    def __init__(self, screen = None, x = None, y = None, width = None, height = None,
                 image = None, image_hover = None, image_click = None):
        self.screen = screen
        self.x = x
        self.y = y
        
        self.image = image
        if (width is None or height is None) and image is None:
            print("Error: button.__init__(): width and height or image are not given.")
        elif image is None:
            self.image = pygame.Surface(width, height)
            self.image.fill((255, 255, 255))    #remove this line if you want a transparent button
        else:
            rect = image.get_rect()
            self.width = rect.width
            self.height = rect.height
        
        self.image_hover = image_hover if not image_hover is None else image
        self.image_click = image_click if not image_click is None else image
    
        self.clicked = False
    
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        
        if self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y:
            if mouse_click[0] == 1:
                self.screen.blit(self.image_click, (self.x, self.y))
                self.clicked = True
            else:
                self.screen.blit(self.image_hover, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y))
            self.clicked = False
            
    