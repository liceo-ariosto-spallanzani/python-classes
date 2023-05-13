# Example file showing a basic pygame "game loop"
import pygame
from random import randint

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

class Entity:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.w = 10
        self.x = randint(0, screen.get_width() - 1 - self.w)
        self.h = 10
        self.y = randint(0, screen.get_height() - 1 - self.h)
        self.s_x = randint(-5, 5)
        self.s_y = randint(-5, 5)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def move(self):
        if self.x >= self.screen.get_width() - 1 - self.w or self.x <= 0:
            self.s_x *= -1
  
        self.x += self.s_x

        if self.y >= self.screen.get_height() - 1 - self.h or self.y <= 0:
            self.s_y *= -1
        
        self.y += self.s_y

entities = []
for i in range(300):
    entities.append(Entity(screen))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
   
    screen.fill("black")
    for e in entities:
        e.move()
        e.draw()
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()