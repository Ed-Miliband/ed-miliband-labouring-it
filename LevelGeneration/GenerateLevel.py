import Pygame
import random
from LevelGeneration import roomData
from LevelGeneration import LootRarity
from main import utility

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLATFORM_COLOR = (255, 255, 255)
PLAYER_COLOR = (255, 0, 0)


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
      
