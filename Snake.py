import pygame
import random
pygame.init()
# Set up the window size and caption
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the font
FONT = pygame.font.SysFont(None, 30)

# Set up the game clock
CLOCK = pygame.time.Clock()

# Set up the snake and food sizes
BLOCK_SIZE = 10
SNAKE_SPEED = 15

class Snake:
    def __init__(self):
        self.snake_head = [250, 250]
        self.snake_body = [[250, 250], [240, 250], [230, 250]]
        self.direction = "RIGHT"
    
    def move(self):
        if self.direction == "UP":
            self.snake_head[1] -= BLOCK_SIZE
        elif self.direction == "DOWN":
            self.snake_head[1] += BLOCK_SIZE
        elif self.direction == "LEFT":
            self.snake_head[0] -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            self.snake_head[0] += BLOCK_SIZE
        
        self.snake_body.insert(0, list(self.snake_head))
        if self.snake_head == FOOD.food_pos:
            FOOD.generate_food()
        else:
            self.snake_body.pop()
    
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
    
    def draw(self, surface):
        for block in self.snake_body:
            pygame.draw.rect(surface, BLACK, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
            pygame.draw.rect(surface, WHITE, [block[0]+1, block[1]+1, BLOCK_SIZE-2, BLOCK_SIZE-2])

class Food:
    def __init__(self):
        self.food_pos = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                         random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
        self.food_spawned = True
    
    def generate_food(self):
        self.food_pos = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                         random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
    
    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

def game_loop():
    # Set up the snake and food objects
    snake = Snake()
    global FOOD
    FOOD = Food()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
        
        snake.move()
        
        if snake.snake_head[0] < 0 or snake.snake_head[0] > WINDOW_WIDTH-10:
            pygame.quit()
            quit()
        elif snake.snake_head[1] < 0 or snake.snake_head[1] > WINDOW_HEIGHT-10:
            pygame.quit()
            quit()
        
        for block in snake.snake_body[1:]:
            if snake.snake_head == block:
                pygame.quit()
                quit()
        
        SCREEN.fill(WHITE)
        snake.draw(SCREEN)
        FOOD.draw(SCREEN)
        
        pygame.display.update()
        CLOCK.tick(SNAKE_SPEED)
game_loop()
