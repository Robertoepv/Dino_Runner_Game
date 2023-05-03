import random
from game.utils.constants import SMALL_CACTUS,LARGE_CACTUS,BIRD,SCREEN_WIDTH

obstacle_dic = {
    "TERRAIN": [SMALL_CACTUS, LARGE_CACTUS],
    "SKY": [BIRD]
    }

class ObstacleBuilder:
    terrain_y = 310
    sky_min_y, sky_max_y = 15, 240
    def __init__(self):
        self.terrain_y = self.terrain_y
        self.sky_min_y, self.sky_max_y = self.sky_min_y, self.sky_max_y
        self.last_obstacle_x = SCREEN_WIDTH
        self.obstacles = []
        self.num_obstacles = 0
        self.num_terrain_collisions = 0
        self.num_bird_collisions = 0

    def generate_obstacle(self):
        if self.num_obstacles < 2:
            self.obstacle_type = random.choice(["TERRAIN", "SKY"])
            if self.obstacle_type == "TERRAIN":
                self.option = random.randint(0,1)
                self.obstacle_image = random.choice(obstacle_dic[self.obstacle_type][self.option])
                obstacle = Obstacle(self.obstacle_image, SCREEN_WIDTH, self.terrain_y, 20)
            elif self.obstacle_type == "SKY":
                self.obstacle_image = random.choice(obstacle_dic[self.obstacle_type][0])
                obstacle_y = random.randint(self.sky_min_y, self.sky_max_y)
                obstacle_x = SCREEN_WIDTH + random.randint(300, 500)
                if obstacle_x - self.last_obstacle_x < 200:
                    obstacle_x += 200
                obstacle = Obstacle(self.obstacle_image, obstacle_x, obstacle_y, random.randint(20, 22))
                self.last_obstacle_x = obstacle_x
                
            self.obstacles.append(obstacle)
            self.num_obstacles += 1

    def update(self,player):
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.rect.x >= - obstacle.rect.width]
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.rect.colliderect(player.dino.dino_rect):
                if self.obstacle_image == SMALL_CACTUS or LARGE_CACTUS:
                    self.num_terrain_collisions += 1
                    print(f'Dino t-dino collide with cactus {self.num_terrain_collisions} times')
                elif self.obstacle_image == BIRD:
                    self.num_bird_collisions += 1
                    print(f'Dino t-dino collide with bird {self.num_bird_collisions} times')
            else:
                None
        self.num_obstacles = len(self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

class Obstacle:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
