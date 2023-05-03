import pygame

class Game():

    def __init__(self, caption='My first game', screen_width=640, screen_height=480):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.keep_screen_open = True
        self.screen_width, self.screen_height = screen_width, screen_height
        self.circle_x, self.circle_y = screen_width // 2, screen_height // 2
        self.circle_radius = 20
        self.circle_x_factor, self.circle_y_factor = 5, 5
        self.paused = False

    def run(self):
        while self.keep_screen_open:
            self.capture_events()
            self.draw()
        else:
            print('Quit game because self.keep_screen_open is', self.keep_screen_open)
    
    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.keep_screen_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.reset_circle()
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

    def draw_circle(self):
        circle_color = (255, 0, 0)
        if not self.paused:
            # Move the circle before drawing it (CHANGE COORDINATES)
            self.circle_x += self.circle_x_factor
            self.circle_y += self.circle_y_factor
        # Verify if circle is inside the screen limits (top, botton, left, right)
        if self.circle_x - self.circle_radius < 0 or self.circle_x + self.circle_radius > self.screen_width:
            self.circle_x_factor = - self.circle_x_factor
        if self.circle_y - self.circle_radius < 0 or self.circle_y + self.circle_radius > self.screen_height:
            self.circle_y_factor = - self.circle_y_factor
        pygame.draw.circle(self.screen, circle_color, (self.circle_x, self.circle_y), self.circle_radius)
    # render(draw or make the screen update) the change on screen
    def draw(self):
        self.screen.fill((255,255,255))
        self.draw_circle()
        pygame.display.flip()
        pygame.time.delay(20)

    def reset_circle(self):
        self.circle_x = self.screen_width // 2
        self.circle_y = self.screen_height // 2