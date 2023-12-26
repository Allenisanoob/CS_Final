import pygame
#Calculations and game logic should be put here.
def game_logic():
    pass

class scene:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        
        #Ture if the scene is ended by regular procedure.
        self.done = False
        
        #Put all the "next scenes" in this list.
        self.next = []

    def run(self):
        while self.running and not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #Put the condition to end the scene here, if there are more than one, use "and" or "or" to combine them.
            condition = False
            if condition:
                self.done = True
            
            game_logic()
            
            self.render()

            pygame.display.flip()

            self.clock.tick(60)
            
        if self.running == False:
            return 0
        #Use the condition to choose the next scene here, if there are more than one, use multiple elif.
        elif self.done and condition:
            return self.next[0]
        else:
            return -1

    #Put all the renderings here.
    def render(self):
        self.screen.fill((255, 255, 255))