import pygame
import random
import os

Width = 800
Height = 600
FPS = 30

#Colors
White = (225, 225, 225)
Black = (0, 0, 0)
Red = (225, 0, 0)
Green = (0, 225, 0)
Blue = (0, 0, 225)

#Asset Folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.center = (Width / 2, Height / 2)
        self.y_speed = 5

    def update(self):

        #Returns A list, keystate, Of All Pressed Keys
        keystate = pygame.key.get_pressed()

        #Checks to See Whch Keys Were In the List (A.K.A Pressed)
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 13
        if keystate[pygame.K_LEFT]:
            self.rect.x += -13
        if keystate[pygame.K_UP]:
            self.rect.y += -13
        if keystate[pygame.K_DOWN]:
            self.rect.y += 13

#Initializer Variables
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Third Game")

clock = pygame.time.Clock()

#Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop:
#   Process Events
#   Update
#   Draw
running = True
while running:

    clock.tick(FPS)

    #Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()

    #Draw
    screen.fill(Blue)
    all_sprites.draw(screen)

    #Flip after Drawing
    pygame.display.flip()
                        

pygame.quit()
