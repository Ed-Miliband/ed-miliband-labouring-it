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

def create_dungeon():
    global dungeon_map, rooms, player, num_total_items

    for _ in range(MAX_ROOMS):
        # Random width and height
        w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        # Random position without going out of the boundaries
        x = random.randint(1, MAP_WIDTH - w - 1)
        y = random.randint(1, MAP_HEIGHT - h - 1)

        new_room = Room(x, y, w, h)

        failed = False

        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            # Carve out the new room in the dungeon map
            for i in range(new_room.x1, new_room.x2):
                for j in range(new_room.y1, new_room.y2):
                    dungeon_map[j][i] = FLOOR

            center = new_room.center

            if rooms:
                # Connect the new room to the previous room with a corridor
                prev_center = rooms[-1].center
                # Randomly choose to go horizontal then vertical or vice versa
                if random.choice([True, False]):
                    create_h_corridor(
                        prev_center[0], center[0], prev_center[1])
                    create_v_corridor(prev_center[1], center[1], center[0])
                else:
                    create_v_corridor(
                        prev_center[1], center[1], prev_center[0])
                    create_h_corridor(prev_center[0], center[0], center[1])

            rooms.append(new_room)

    # Place the player in the center of the first room
    player_pos = [rooms[0].center[0] * TILE_SIZE,
                  rooms[0].center[1] * TILE_SIZE]
    global player
    player = Player(player_pos)
    global treasure_display
    treasure_display = TreasureValueDisplay()
    global monster_health_display
    monster_health_display = HealthDisplay()

    # Sprite groups
    global all_sprites
    all_sprites = pygame.sprite.Group(treasure_display, monster_health_display)

    # Generate room contents
    for room in rooms:
        room.generate_contents()

    num_total_items = len(all_items)

def create_h_corridor(x1, x2, y):
    """Creates a horizontal corridor at least CORRIDOR_WIDTH wide."""
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for i in range(CORRIDOR_WIDTH):  # Make the corridor at least 2 tiles wide
            dungeon_map[y + i][x] = FLOOR


def create_v_corridor(y1, y2, x):
    """Creates a vertical corridor at least CORRIDOR_WIDTH wide."""
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for i in range(CORRIDOR_WIDTH):  # Make the corridor at least 2 tiles wide
            dungeon_map[y][x + i] = FLOOR

# Function to check collision with walls


def is_walkable(x, y):
    tile_x = x // TILE_SIZE
    tile_y = y // TILE_SIZE
    if 0 <= tile_y < MAP_HEIGHT and 0 <= tile_x < MAP_WIDTH:
        tile = dungeon_map[tile_y][tile_x]
        if tile == WALL:
            return False
        else:
            return True
    return False
      
