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
  
def loadLevelData():
  e = load_json(roomdata)
  

def loadLevel():
