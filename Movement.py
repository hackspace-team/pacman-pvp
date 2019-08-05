import pygame
import spritesheet

pygame.init()

display_width = 800
display_height = 600
 
gameDisplay = pygame.display.set_mode((display_width,display_height)) 

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

ss = spritesheet.spritesheet('pacman.png')

pacmanImg = ss.image_at((0, 0, 16, 16))
pacmanImg1 = ss.image_at((0, 0, 16, 16))
player_rect = pacmanImg.get_rect()
 
def pacman(x,y):
   gameDisplay.blit(pacmanImg, (x,y))

def pacman1(x, y):
   gameDisplay.blit(pacmanImg1, (x1,y1))
 
x =  (display_width * 0.45)
y = (display_height * 0.8)
x1 =  (display_width * 0.45)
y1 = (display_height * 0.4)
x_change = 0
y_change = 0
x1_change = 0
y1_change = 0
pacman_speed = 0
pacman1_speed = 0

while not crashed:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           crashed = True
 
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               pacmanImg = ss.image_at((0, 16, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               x_change = -5
               y_change = 0
           elif event.key == pygame.K_RIGHT:
               pacmanImg = ss.image_at((0, 0, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               x_change = 5
               y_change = 0
           elif event.key == pygame.K_UP:
               pacmanImg = ss.image_at((0, 32, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               y_change = -5
               x_change = 0
           elif event.key == pygame.K_DOWN:
               pacmanImg = ss.image_at((0, 48, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               y_change = 5
               x_change = 0
           elif event.key == pygame.K_a:
               pacmanImg1 = ss.image_at((0, 16, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               x1_change = -5
               y1_change = 0
           elif event.key == pygame.K_d:
               pacmanImg1 = ss.image_at((0, 0, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               x1_change = 5
               y1_change = 0
           elif event.key == pygame.K_w:
               pacmanImg1 = ss.image_at((0, 32, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               y1_change = -5
               x1_change = 0
           elif event.key == pygame.K_s:
               pacmanImg1 = ss.image_at((0, 48, 16, 16))
               player_rect = pacmanImg.get_rect()
               gameDisplay.blit(pacmanImg, player_rect)
               y1_change = 5
               x1_change = 0
     
   x += x_change
   y += y_change    
   x1 += x1_change
   y1 += y1_change
   player_rect.x += x_change
   player_rect.y += y_change    
   gameDisplay.fill(black)
   pacman(x,y)
   pacman1(x1,y1)
      
   pygame.display.update()
   clock.tick(60)
 
pygame.quit()
quit()
