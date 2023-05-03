import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLOUD

class Sky():

    def __init__(self):
        self.cloud_images = [CLOUD]
        self.clouds = []
        self.min_y, self.max_y = 10, SCREEN_HEIGHT // 3
        self.add_cloud()

    def add_cloud(self):
        image = random.choice(self.cloud_images)
        cloud = {
            'image': image,
            'rect': image.get_rect(),
            'speed': random.randint(7, 10)
        }
        # establecer posición aleatoria verticalmente en y
        cloud['rect'].y = random.randint(self.min_y, self.max_y)
        # establecer posición en x respetando distancia mínima
        last_cloud = self.clouds[-1] if self.clouds else None
        while last_cloud and last_cloud['rect'].right > SCREEN_WIDTH - 20:
            cloud['rect'].x = last_cloud['rect'].left - 20
            last_cloud = self.clouds[-1]
        else:
            cloud['rect'].x = SCREEN_WIDTH - 20
        self.clouds.append(cloud)

    def update(self):
        for cloud in self.clouds:
            cloud['rect'].x -= cloud['speed']
            if cloud['rect'].right < 0:
                self.clouds.remove(cloud)
        if len(self.clouds) < len(self.cloud_images):
            self.add_cloud()

    def draw(self, screen):
        for cloud in self.clouds:
            screen.blit(cloud['image'], cloud['rect'])
