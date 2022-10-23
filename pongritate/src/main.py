import sys
import pygame
import random
import os
import time
import json

pygame.init()
pygame.font.init()

windowedWidth, windowedHeight = 1080, 720
fullscreenWidth, fullscreenHeight = (
    pygame.display.get_desktop_sizes()[0][0],
    pygame.display.get_desktop_sizes()[0][1],
)

if json.load(open(f"{os.getcwd()}\\pongritate\\data\\savedata.json"))["settings"][
    "fullscreen"
]:
    screen = pygame.display.set_mode(
        (fullscreenWidth, fullscreenHeight), pygame.FULLSCREEN
    )
    width, height = fullscreenWidth, fullscreenHeight

else:
    screen = pygame.display.set_mode((windowedWidth, windowedHeight), pygame.RESIZABLE)
    width, height = windowedWidth, windowedHeight

playButtonSize = 200

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
PLAYBUTTONCOLOR = (55, 55, 55)
BACKGROUNDCOLOR = (43, 43, 43)

TITLE = pygame.image.load(f"{os.getcwd()}\\pongritate\\assets\\title.png")
titlePositionX, titlePositionY = (screen.get_width() / 2) - (720 / 2), (height / 3)-300
desiredY = titlePositionY

playButtonPressed = False
toggle = True
limit = 100
loop_count = 0
while not(playButtonPressed):
    loop_count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if (
        pygame.mouse.get_pos()[0] >= (screen.get_width() / 2) - (playButtonSize / 2)
        and pygame.mouse.get_pos()[0] <= ((screen.get_width() / 2) - (playButtonSize / 2)) + playButtonSize
        and pygame.mouse.get_pos()[1] >= 440
        and pygame.mouse.get_pos()[1] <= 523
    ):
        playButtonSize = playButtonSize + ((240 - playButtonSize) / 50)
        if pygame.mouse.get_pressed() == (1, 0, 0):
            playButtonPressed = True
    else:
        playButtonSize = playButtonSize + ((200 - playButtonSize) / 50)

    if loop_count > limit:
        toggle = not(toggle)
        limit = loop_count + 200
    elif toggle == True:
        desiredY += 1
    elif toggle == False:
        desiredY -= 1
    titlePositionY = titlePositionY + ((desiredY - titlePositionY) / 150)
    
    screen.fill((BACKGROUNDCOLOR))
    
    titlePositionX = (screen.get_width() / 2) - (720 / 2)

    pygame.draw.rect(
        screen,
        PLAYBUTTONCOLOR,
        (
            (screen.get_width() / 2) - (playButtonSize / 2),
            (450 - round(playButtonSize / 5)) + 30,
            playButtonSize,
            playButtonSize / 2.5,
        ),
        border_radius=500,
    )
    font = pygame.font.Font(
        f"{os.getcwd()}\\pongritate\\fonts\\FredokaOne.ttf", round(playButtonSize / 4.4)
    )
    text = font.render("Play", True, WHITE)
    textpos = text.get_rect(
        centerx=screen.get_width() / 2, y=452 - (playButtonSize / 200)
    )
    screen.blit(text, textpos)
    screen.blit(TITLE, (titlePositionX, titlePositionY))

    pygame.display.update()