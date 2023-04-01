import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# set up the game clock
clock = pygame.time.Clock()

# set up the game's colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
paddle_speed = 5

player_paddle = pygame.Rect(50, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# set up the ball
BALL_SIZE = 10
ball_speed = 5

ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_direction = [random.choice([-1, 1]), random.uniform(-1, 1)]

# set up the game loop
game_running = True
while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    # move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and player_paddle.bottom < WINDOW_HEIGHT:
        player_paddle.move_ip(0, paddle_speed)

    # move the AI paddle
    if ai_paddle.centery < ball.centery and ai_paddle.bottom < WINDOW_HEIGHT:
        ai_paddle.move_ip(0, paddle_speed)
    elif ai_paddle.centery > ball.centery and ai_paddle.top > 0:
        ai_paddle.move_ip(0, -paddle_speed)

    # move the ball
    ball.move_ip(ball_speed * ball_direction[0], ball_speed * ball_direction[1])

    # check for collisions with the paddles
    if ball.colliderect(player_paddle):
        ball_direction[0] = 1
    elif ball.colliderect(ai_paddle):
        ball_direction[0] = -1

    # check for collisions with the top and bottom of the screen
    if ball.top < 0 or ball.bottom > WINDOW_HEIGHT:
        ball_direction[1] = -ball_direction[1]

    # check for a goal
    if ball.left < 0 or ball.right > WINDOW_WIDTH:
        ball_direction = [random.choice([-1, 1]), random.uniform(-1, 1)]
        ball.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # draw the game elements
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
    pygame.display.flip()

    # control the game's frame rate
    clock.tick(60)

# quit Py
pygame.quit()
