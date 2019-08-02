import pygame
import spritesheet
 
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second

screen = pygame.display.set_mode(SIZE)


ss = spritesheet.spritesheet('pacman.png')
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = []
        self.images.append(ss.image_at((0, 0, 16, 16)))
        self.images.append(ss.image_at((16, 0, 16, 16)))
        self.images.append(ss.image_at((32, 0, 16, 16)))
 
        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(5, 5, 150, 198)
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)
 
main()