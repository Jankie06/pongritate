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
    screen = pygame.display.set_mode((windowedWidth, windowedHeight))
    width, height = windowedWidth, windowedHeight

playButtonSize = 200
BACKGROUNDCOLOR = (43, 43, 43)
TITLE = pygame.image.load(f"{os.getcwd()}\\pongritate\\assets\\title.png")

playButtonColor = (55, 55, 55)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if pygame.mouse.get_pos()[0] >= 440 and pygame.mouse.get_pos()[0] <= 640 and pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[1] <= 523:
        playButtonSize = playButtonSize + ((240 - playButtonSize) / 50)
    else:
        playButtonSize = playButtonSize + ((200 - playButtonSize) / 50)

    screen.fill((BACKGROUNDCOLOR))

    pygame.draw.rect(
        screen,
        playButtonColor,
        (
            (width / 2) - (playButtonSize / 2), 
            (450 - round(playButtonSize / 5)) + 30, 
            playButtonSize,
            playButtonSize / 2.5,
        ),
        border_radius=500,
    )
    font = pygame.font.Font(
        f"{os.getcwd()}\\pongritate\\fonts\\FredokaOne.ttf", round(playButtonSize / 4.4)
    )
    text = font.render("Play", True, (200, 200, 200))
    textpos = text.get_rect(
        centerx=screen.get_width() / 2, y=452 - (playButtonSize / 200)
    )
    screen.blit(text, textpos)

    pygame.display.update()
