import pygame,sys
import spritesheet
FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
CLR_KEY=(255,255,255)
X_OFFSET=70
Y_OFFSET=95
W=600
H=600
class bullet(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprite = sprite
    pass
class ship(pygame.sprite.Sprite):
    up_count=0
    down_count=0
    left_count=0
    right_count=0
    def __init__(self,name,x_pos,y_pos,sprite,speed):
        #Parent class init
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.sprite= sprite
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.count = 0
        self.speed = speed
        self.right_flag=False
    def move_up(self): 
        if(self.y_pos - self.speed >= 0):
            self.y_pos = self.y_pos - self.speed
     
    def move_down(self): 
        if(self.y_pos + self.speed <= H):
            self.y_pos = self.y_pos + self.speed
     
    def move_right(self): 
        if(self.x_pos + self.speed <= W):
            self.x_pos = self.x_pos + self.speed
            
    def move_left(self): 
        if(self.x_pos - self.speed >= 0):
            self.x_pos = self.x_pos - self.speed
            self.right_flag=False
    def draw(self,screen):
            image = self.sprite
            image_rect = self.sprite.get_rect()
            image_rect.move_ip(self.x_pos,self.y_pos)
            screen.blit(image,image_rect)
    def update(self):
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT)):
            self.move_right()
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT)):
            self.move_left()
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_UP)):
            self.move_up()
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_DOWN)):
            self.move_down()

            
        
pygame.init()
w =W
h =H
pygame.key.set_repeat(10,10)
pygame.display.set_caption("Space Ship")
screen = pygame.display.set_mode((w,h))
ship_sprite= spritesheet.spritesheet("ships.png")
ship_image = ship_sprite.image_at((64,70,130,104))
bullet_image = ship_sprite.image_at((367,2466,35,67))


ship1= ship("Destroyer",0,h/2,ship_image,10)

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            sys.exit()
    ship1.update()         
    screen.fill(BLACK)
    ship1.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
