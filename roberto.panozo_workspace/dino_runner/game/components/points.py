import pygame
from game.utils.constants import FONT
from game.components.obstacles.obstacle_builder import Obstacle

class Points:
    
    def __init__(self):
        self.total_points = 100
        self.cactus_dodge = 100
        self.bird_dodge = 75
        self.font = pygame.font.Font(FONT, 20)
        self.valor = Obstacle.image_rect

    def points_manager(self,player):
        if Obstacle.image_rect.colliderect(player.dino.dino_rect):
            total_points -= 5
        if Obstacle.image_rect.colliderect(player.dino.dino_rect):
            total_points -= 2.5

    def draw(self, screen):
        points_text = self.font.render(f"Total Points: {self.total_points}", True,(0,0,0))
        screen.blit(points_text, (1080,20))