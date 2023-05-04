from game.utils.constants import SMALL_CACTUS,LARGE_CACTUS,BIRD,SCREEN_HEIGHT,SCREEN_WIDTH,FONT,COLORS
import random
import pygame

OBSTACLES_DICT = {
    "TERRAIN": [SMALL_CACTUS, LARGE_CACTUS],
    "SKY": [BIRD]
    }

class ObstacleBuilder:
    
    def __init__(self):
        self.obstacles = []
        self.large_cactus_y,self.small_cactus_y = 305,330
        self.min_distance = random.randint(300, 500)
        self.on_cactus, self.on_bird = False, False
        self.count_cactus, self.count_bird = 0, 0
        self.font = pygame.font.Font(FONT, 17)        

    def generate_obstacles(self):
            obstacle_choise = random.choice(["TERRAIN", "SKY"])
            if obstacle_choise == 'TERRAIN':
                image_type, option  = random.randint(0, 1), random.randint(0, 2)
                obstacle_image = OBSTACLES_DICT[obstacle_choise][image_type][option]
                if image_type == 0:
                    obstacle_y = self.small_cactus_y
                elif image_type == 1:
                    obstacle_y = self.large_cactus_y
                obstacle = Obstacle(obstacle_image, SCREEN_WIDTH, obstacle_y, 20)
                obstacle_x = obstacle.image_rect.x
                if not self.obstacles or self.last_obstacle_x - obstacle_x >= self.min_distance:
                    self.obstacles.append(obstacle)
                    self.last_obstacle_x = obstacle_x
            else:
                None
    
    def check_collision(self,player):
        for obstacle in self.obstacles:
            obstacle_type = None
            if obstacle.image_rect.colliderect(player.dino.dino_rect):
                if obstacle in OBSTACLES_DICT["TERRAIN"][0]:
                    obstacle_type = "SMALL_CACTUS"
                    self.total_points -= 5
                elif obstacle in OBSTACLES_DICT["TERRAIN"][1]:
                    obstacle_type = "LARGE_CACTUS"
                    self.total_points -= 5
                elif obstacle in OBSTACLES_DICT["SKY"][0]:
                    obstacle_type = "BIRD"
                    self.total_points -= 2.5
                if not self.on_cactus and obstacle_type == "SMALL_CACTUS" or "LARGE_CACTUS":
                    self.on_cactus = True
                    self.count_cactus += 1
                    print(f'{self.count_cactus}')
                elif obstacle_type and not self.on_bird:
                    self.count_bird += 1 
                    self.on_bird = True
            else:
                self.on_cactus = False
                self.on_bird = False

    def update(self):
        if len(self.obstacles) < 2:
            self.generate_obstacles()
        for obstacle in self.obstacles:
            obstacle.update()
        if self.obstacles and self.obstacles[0].image_rect.right < 0:
            self.obstacles.pop(0)

    def draw(self, screen):
        for obstacle in self.obstacles:
            screen.blit(obstacle.image, obstacle.image_rect)
        
        text_cactus = self.font.render(f'Collided with cactus: {self.count_cactus}', True, COLORS["black"])
        screen.blit(text_cactus,(20,SCREEN_HEIGHT-70))
        text_bird = self.font.render(f'Collided with bird: {self.count_bird}', True, COLORS["black"])
        screen.blit(text_bird,(20,SCREEN_HEIGHT-100))

class Obstacle:
    image_rect = None
    def __init__(self, image, x, y, speed):
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.x, self.image_rect.y = x, y
        self.speed = speed
        Obstacle.image_rect = self.image_rect

    def update(self):
        self.image_rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
