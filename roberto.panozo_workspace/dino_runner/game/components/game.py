import pygame
from game.utils.constants import PAUSE_TEXT,BG,ICON,SCREEN_HEIGHT,SCREEN_WIDTH,TITLE,FPS,COLORS,BACKGROUND_SOUND
from game.components.obstacles.obstacle_builder import ObstacleBuilder
from game.components.player import Dinosaur
from game.components.sky import Sky

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        pygame.mixer.music.load(BACKGROUND_SOUND)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.4)
        self.dino = Dinosaur('T-Rex')
        self.sky = Sky()
        self.obstacles = ObstacleBuilder()

        self.pause = False
        self.pause_text_rect = PAUSE_TEXT.get_rect()
        self.pause_text_rect.center = self.screen.get_rect().center

    def run(self):
        # This is Game Loop: events - update - draw
        self.playing = True
        while self.playing:
            pygame.display.flip()
            self.capture_events()
            self.screen.blit(PAUSE_TEXT, self.pause_text_rect)
            if (not self.pause):
                pygame.mixer.music.unpause()
                self.update()
                self.draw()
        else:
            print(f'game run method is {self.playing}')

    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                self.pause = not self.pause
                pygame.mixer.music.pause()

    def update(self):
        self.dino.update(pygame.key.get_pressed())
        self.sky.update()
        self.obstacles.update(self)
        self.obstacles.generate_obstacle()
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLORS['white'])
        self.draw_background()
        self.sky.draw(self.screen)
        self.dino.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.dino.show_text(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed