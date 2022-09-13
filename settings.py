import math



# game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 100

#player settings
PLAYER_POS = 1.5, 5         # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002    #rotation speed
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.00018
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (16, 16, 16)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2            # number of rays
HALF_NUM_RAYS = NUM_RAYS // 2    # angle between the rays
DELTA_ANGLE = FOV / NUM_RAYS     # delta angle
MAX_DEPTH = 20                   # draw distance

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2