import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
FPS = 30
DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/SmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(DIR, 'Other/SmallHeart.png'))

PAUSE_TEXT = pygame.image.load(os.path.join(DIR, 'Other/pause_button_text.png'))
PAUSE_ICON =pygame.image.load(os.path.join(DIR, 'Other/pause_icon.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

COLORS = {
    "black": (0,0,0),
    "white": (255,255,255)
}

FONT = 'freesansbold.ttf'

NORMAL = 'normal'
POWER_UP = 'power up'

JUMP_SOUND = (os.path.join(DIR, 'Sounds/jump.wav'))
BACKGROUND_SOUND = (os.path.join(DIR, 'Sounds/Running-About.wav'))
