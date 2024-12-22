import pygame
import random
import sys

colorList = ["rad","green", "blue","gray"]

pygame.init()
monitor = pygame.display.set_mode((500,700))
color = random.choice(colorList)
cara = pygame.image.load("C:/Users/piosp/OneDrive/english/donaldo.png")
cara = pygame.transform.scale(cara,(50,50))
tx, ty = 200, 300

while True:
    monitor.fill(color)
    monitor.blit(cara,(tx,ty))
    pygame.display.update()

    for e in pygame.event.get():
        if e.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()

        if e.type in [pygame.KEYDOWN]:
            if e.key == pygame.K_LEFT: tx -= 10
            if e.key == pygame.K_RIGHT: tx += 10
            if e.key == pygame.K_UP: ty -= 10
            if e.key == pygame.K_DOWN: ty += 10

            if e.key == pygame.K_SPACE:
                tx = random.randrange(0,500)
                ty = random.randrange(0,700)
