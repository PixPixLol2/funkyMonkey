import pygame

pygame.init()

W_W = 1280
W_H = 720

x = 100
y = 100
velocity = 1

scrn = pygame.display.set_mode((W_W, W_H))
pygame.display.set_caption('Funky Monkey')

monkey = pygame.image.load("C:/Users/brado/Downloads/funkyMonkey/funkyMonkey.png").convert()
monkey = pygame.transform.scale(monkey, (523.25, 392.45))

def movementSystem(keys, x, y):
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
    return x, y

status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    keys = pygame.key.get_pressed()

    x, y = movementSystem(keys, x, y)

    scrn.fill((0, 0, 0))
    scrn.blit(monkey, (x, y))
    pygame.display.update()

pygame.quit()
