import os

MAX_X = 1000
MAX_Y = 800
FRAME_RATE = 60

PATH = os.path.dirname(os.path.abspath(__file__))
# MESSAGES = open(PATH + "/messages.txt").read().splitlines()
ARTIFACTS = 30

CHESTS = 3
CHEST_IMG = os.path.join(os.getcwd(), "./chest.png")
CHEST_IMAGE = os.path.join(os.getcwd(), "./game/assets/chest.png")
CHEST_TEXT = open(PATH + "/chest_texts.txt").read().splitlines()

GUARDS = 6
GUARD_SPEED = 1
GUARD_RETRO = os.path.join(os.getcwd(), "./game/assets/guard.png")
GUARD_BAD = os.path.join(os.getcwd(), "./game/assets/guard_bad.png")

SOUND_START = os.path.join(os.getcwd(), "./game/assets/place.wav")

MAP_IMAGE = os.path.join(os.getcwd(), "./game/assets/map_temp.png")
MAP_Y = 1000
MAP_X = 800
MAP_TILES = 400

DEFAULT_BLOCK_SIZE = 15
DEFAULT_FONT_SIZE = 20

ROBOT_SPEED = 3
HERO_IMAGE = os.path.join(os.getcwd(), "./game/assets/hero.png")
HERO_RETRO = os.path.join(os.getcwd(), "./game/assets/hero_retro.png")
HERO_VECTOR = os.path.join(os.getcwd(), "./game/assets/download.png")

SCORE_X = 10
SCORE_Y = 50
SCORE_DEFAULT = 0

WALL_STONE_V = os.path.join(os.getcwd(), "./game/assets/wall_stone_vertical.png")
WALL_STONE_H = os.path.join(os.getcwd(), "./game/assets/wall_stone_horizontal.png")

TREES = 250
TREE_1 = os.path.join(os.getcwd(), "./game/assets/tree_1.png")
TREE_TEXT = open(PATH + "/tree_texts.txt").read().splitlines()

SUPPLY_AID = os.path.join(os.getcwd(), "./game/assets/supply_aid.png")

NORTH_DOOR = os.path.join(os.getcwd(), "./game/assets/door.png")
