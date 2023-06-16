import sys, pygame,random

pygame.init()

size = width, height = 1280, 960
speed = [5, 5]
black = 0, 0, 0
clock = pygame.time.Clock()


screen = pygame.display.set_mode(size)

fon= pygame.image.load("FOON.png").convert()


player_score=0
oponent_score=0
game_font=pygame.font.Font('freesansbold.ttf',100)


pygame.key.set_mods(0)
pygame.key.set_repeat(2,3)


class Ball:
    def __init__(self,speed,oponent,player) -> None:
        self.ball = pygame.image.load("intro_ball.png")
        self.ballrect = self.ball.get_rect()
        self.ballrect=self.ballrect.move([650,480])
        self.speed_new=speed
        self.oponent=oponent
        self.player=player



    def animation(self):
        self.ballrect = self.ballrect.move(self.speed_new)
        if self.ballrect.left < 0 :
            self.speed_new=[5, 5]
            self.ballrect.center=(screen.get_width()/2,screen.get_height()/2)
            self.speed_new[0] *=random.choice((1,-1))
            self.speed_new[1] *=random.choice((1,-1))
            self.oponent+=1

        if self.ballrect.right > width:
            self.speed_new=[5, 5]
            self.ballrect.center=(screen.get_width()/2,screen.get_height()/2)
            self.speed_new[0] *=random.choice((1,-1))
            self.speed_new[1] *=random.choice((1,-1))
            self.player+=1

        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed_new[1] = -1*self.speed_new[1]
        

class Plauer:
    def __init__(self) -> None:
        self.raketka1=pygame.image.load('raketka.png')
        self.raketkaRect1= self.raketka1.get_rect()
        self.raketkaRect1=self.raketkaRect1.move([-30,0])
    
    def move(self):
          if self.raketkaRect1.top<=0:
            self.raketkaRect1.top=0
          if self.raketkaRect1.bottom>=screen.get_height():
            self.raketkaRect1.bottom=screen.get_height()

class oponent:
    def __init__(self) -> None:
        self.raketka2=pygame.image.load('raketka.png')
        self.raketkaRect2= self.raketka2.get_rect()
        self.raketkaRect2=self.raketkaRect2.move([1250,0])
    def move(self,ball):
        if self.raketkaRect2.top<ball.y:
            self.raketkaRect2.top+=7
        if self.raketkaRect2.bottom>ball.y:
            self.raketkaRect2.bottom-=7
        if self.raketkaRect2.top<=0:
            self.raketkaRect2.top=0
        if self.raketkaRect2.bottom>=screen.get_height():
            self.raketkaRect2.bottom=screen.get_height()

ball1=Ball(speed,oponent_score,player_score,)
player1=Plauer()
oponent1=oponent()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    key_pressed = pygame.key.get_pressed()
    pygame.key.get_repeat()
    ball1.animation()
    if key_pressed[pygame.K_UP]:
        player1.raketkaRect1=player1.raketkaRect1.move([0,-7])
    if key_pressed[pygame.K_DOWN]:
        player1.raketkaRect1=player1.raketkaRect1.move([0,7])
    player1.move()
    oponent1.move(ball1.ballrect)
    if ball1.ballrect.colliderect(player1.raketkaRect1) or ball1.ballrect.colliderect(oponent1.raketkaRect2):
          ball1.speed_new[0] = -1*ball1.speed_new[0]
          if ball1.speed_new[0]<0:
              ball1.speed_new[0] -= 1
          else:
              ball1.speed_new[0] += 1
          if ball1.speed_new[1]<0:
              ball1.speed_new[1] -= 1
          else:
              ball1.speed_new[1] += 1
    player_text= game_font.render(f"{ball1.player}", False,black)

    oponent_text= game_font.render(f"{ball1.oponent}", False,black)

    clock.tick(60)
    screen.blit(fon, (0 , 0))
    
    screen.blit(player1.raketka1,player1.raketkaRect1)
    screen.blit(oponent1.raketka2,oponent1.raketkaRect2)
    screen.blit(ball1.ball, ball1.ballrect)
    screen.blit(oponent_text,(640,100))
    screen.blit(player_text,(540,100))

    pygame.display.flip()
