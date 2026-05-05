import Pygame
import random
import sys
from LevelGeneration import roomData
from LevelGeneration import LootRarity
from main import utility
import Images

pygame.init()

#Screen settings
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 16
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedurally Generated Dungeon with Sprites")

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WALL_COLOR = (100, 100, 100) #light grey
FLOOR_COLOR = (50, 50, 50) #dark grey

#Map settings
MAP_WIDTH = WIDTH // TILE_SIZE
MAP_HEIGHT = HEIGHT // TILE_SIZE

#Define tile types
WALL = 1
FLOOR = 0

#Dungeon map (2D array)
dungeon_map = [[WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

#Room settings
MAX_ROOMS = 10
ROOM_MIN_SIZE = 5
ROOM_MAX_SIZE = 10
CORRIDOR_WIDTH = 2
rooms = []

#all inventory items in all rooms
global all_items
all_items = []

#game over flag
global game_over
game_over = False

#total treasure collected
global total_treasure
total_treasure = 0

#total number of all items in the dungeon
global num_total_items
num_total_items = 0

#Load images
player_image = pygame.image.load('player.png').convert_alpha()
weapon_image = pygame.image.load('weapon.png').convert_alpha()
treasure_image = pygame.image.load('treasure.png').convert_alpha()
monster_image = pygame.image.load('monster.png').convert_alpha()
potion_image = pygame.image.load('potion.png').convert_alpha()


def LootChance():
  lootNumber = random.randrange(1,17)
  return lootNumber

def giveLoot():
  chance = lootChance()
  load_json(LootRarity)
  looty = json.load(chance)
  return looty
  
def loadLevelData(map):
  e = load_json("roomdata")
  f = json.load(map)
  return f

def loadLevel(realmap):
  room = realmap
  roomcount = 0
  while roomcount =< 6:
    if room[roomcount] == 1: #empty room
      roomcount += 1
      
    if room[roomcount] == 2: #loot room
      roomcount += 1
      
    if room[roomcount] == 3: #combat room
      roomcount += 1
      
    if room[roomcount] == 4: #placeholder
      roomcount += 1

    if room[roomcount] == 5: #placeholder
      roomcount += 1

    if room[roomcount] == 6: #boss room
      roomcount += 1
      
