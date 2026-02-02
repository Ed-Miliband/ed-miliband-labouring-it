import pygame
import random

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLATFORM_COLOR = (255, 255, 255)
PLAYER_COLOR = (255, 0, 0)


def giveLoot():
  lootNumber = random.ranrange(1,17)
  return lootNumber
