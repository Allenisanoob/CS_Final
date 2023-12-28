import pygame

class button():
    def __init__(self, screen = None, x = None, y = None, width = None, height = None,
                 image = None, image_hover = None, image_click = None, color = None):
        self.screen = screen
        self.x = x
        self.y = y
        
        if (width is None or height is None) and image is None:
            print("Error: button.__init__(): width and height and color or image are not given.")
            return -1
        elif not image is None:
            self.image = pygame.image.load(image).convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height
        else:
            self.width = width
            self.height = height
            self.rect = pygame.Rect(x, y, width, height)
            self.image = pygame.Surface(self.rect.size)
            self.image.fill(color)    #remove this line if you want a transparent button

        self.pressed = None
        self.last_pressed = None
        self.clicked = False
        self.released = False
        
        self.image_hover = pygame.image.load(image_hover).convert() if not image_hover is None else self.image
        self.image_hover.set_colorkey((0, 0, 0))
        self.image_click = pygame.image.load(image_click).convert() if not image_click is None else self.image
        self.image_click.set_colorkey((0, 0, 0))
    

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        
        if self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y:
            if mouse_click[0] == True:
                self.screen.blit(self.image_click, (self.x, self.y))
                self.last_pressed = self.pressed
                self.pressed = True
            else:
                self.screen.blit(self.image_hover, (self.x, self.y))
                self.last_pressed = self.pressed
                self.pressed = False
        else:
            self.screen.blit(self.image, (self.x, self.y))
            self.last_pressed = self.pressed
            self.pressed = False

        if not self.last_pressed is None:
            self.clicked = not self.last_pressed and self.pressed
            self.released = self.last_pressed and not self.pressed

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

    