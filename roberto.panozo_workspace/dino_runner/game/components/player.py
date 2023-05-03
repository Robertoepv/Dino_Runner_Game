import pygame
from game.utils.constants import RUNNING, DUCKING, JUMPING, JUMP_SOUND, DEFAULT_TYPE, SCREEN_HEIGHT, FONT, COLORS

class Dinosaur():
    POS_X, POS_Y = 80, 310
    POS_Y_DUCKING = 345
    JUMP_VEL = 8.5
    def __init__(self, name):
        self.run_img = {DEFAULT_TYPE: RUNNING}
        self.duck_img = {DEFAULT_TYPE: DUCKING}
        self.jump_img = {DEFAULT_TYPE: JUMPING}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x, self.dino_rect.y = self.POS_X, self.POS_Y
        self.jump_vel = self.JUMP_VEL
        self.jump_sound = JUMP_SOUND
        self.step_index = 0
        self.dino_running, self.dino_ducking, self.dino_jumping = True, False, False
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.jump_sound.set_volume(1)
        self.name = name
        self.state = ''
        self.font = pygame.font.Font(FONT, 20)

    def update(self, user_input):
        if self.dino_running:
            self.run()
        elif self.dino_jumping:
            self.jump()
        elif self.dino_ducking:
            self.duck()

        if user_input[pygame.K_DOWN] and not self.dino_jumping:
            self.state = 'Is ducking'
            print(self.state)
            self.dino_running,self.dino_jumping,self.dino_ducking = False, False, True

        elif user_input[pygame.K_UP] and not self.dino_jumping:
            self.state = 'Is jumping'
            print(self.state)
            self.jump_sound.play()
            self.dino_running, self.dino_jumping, self.dino_ducking = False, True, False

        elif not self.dino_jumping:
            self.state = 'Is running'
            self.dino_running, self.dino_jumping, self.dino_ducking = True, False, False

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)
        
    def run(self):
        self.image = self.run_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x, self.dino_rect.y = self.POS_X, self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.POS_Y
            self.dino_jumping = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x, self.dino_rect.y = self.POS_X, self.POS_Y_DUCKING
        self.step_index += 1

    def show_text(self,screen):
        if self.dino_running or self.dino_jumping or self.dino_ducking:
            state_text = self.font.render(f'Dino {self.name}: {self.state}', True, COLORS["black"])
            screen.blit(state_text, (20, SCREEN_HEIGHT-40))
        