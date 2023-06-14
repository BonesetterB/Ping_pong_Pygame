import sys, pygame

pygame.init()

size = width, height = 1280, 960
speed = [2, 2]
black = 0, 0, 0
clock = pygame.time.Clock()


screen = pygame.display.set_mode(size)

fon= pygame.image.load("FOON.png").convert()



ball = pygame.image.load("intro_ball.png")
ballrect = ball.get_rect()
ballrect=ballrect.move([640,480])

raketka1=pygame.image.load('raketka.png')
raketkaRect1= raketka1.get_rect()
raketkaRect1=raketkaRect1.move([-30,0])

raketka2=pygame.image.load('raketka.png')
raketkaRect2= raketka2.get_rect()
raketkaRect2=raketkaRect2.move([1250,0])

pygame.key.set_mods(0)
pygame.key.set_repeat(2,3)
while True:
    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        pygame.key.get_repeat()
        if key_pressed[pygame.K_UP]:
                raketkaRect1=raketkaRect1.move([0,-5])
        if key_pressed[pygame.K_DOWN]:
                raketkaRect1=raketkaRect1.move([0,5])
        if event.type == pygame.QUIT: 
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -1*speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -1*speed[1]
    if ballrect.colliderect(raketkaRect1) or ballrect.colliderect(raketkaRect2):
          speed[0] = -1*speed[0]
    clock.tick(60)
    screen.blit(fon, (0 , 0))
    screen.blit(raketka1,raketkaRect1)
    screen.blit(raketka2,raketkaRect2)
    screen.blit(ball, ballrect)

    pygame.display.flip()
