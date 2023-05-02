import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game title
pygame.display.set_caption("Tomb of the Mask")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the player sprite
player_width = 50
player_height = 50
player = pygame.Rect(screen_width / 2 - player_width / 2, screen_height - player_height, player_width, player_height)

# Define the enemy sprite
enemy_width = 30
enemy_height = 30
enemy_speed = 5
enemy_list = []
for i in range(5):
    enemy_x = random.randrange(0, screen_width - enemy_width)
    enemy_y = random.randrange(-screen_height, 0)
    enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemy_list.append(enemy)

# Set the game clock
clock = pygame.time.Clock()

# Set the game score
score = 0
high_score = 0

# Set the game state
game_over = False

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = False
                score = 0
                enemy_speed = 5
                enemy_list = []
                for i in range(5):
                    enemy_x = random.randrange(0, screen_width - enemy_width)
                    enemy_y = random.randrange(-screen_height, 0)
                    enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
                    enemy_list.append(enemy)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < screen_width:
        player.x += 5
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < screen_height:
        player.y += 5

    # Move the enemies
    for enemy in enemy_list:
        enemy.y += enemy_speed
        if enemy.top > screen_height:
            enemy_x = random.randrange(0, screen_width - enemy_width)
            enemy_y = random.randrange(-screen_height, 0)
            enemy.x = enemy_x
            enemy.y = enemy_y
            score += 1

    # Check for collisions
    for enemy in enemy_list:
        if player.colliderect(enemy):
            game_over = True
            if score > high_score:
                high_score = score




    # Draw the sprites and background
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    for enemy in enemy_list:
        pygame.draw.rect(screen, BLACK, enemy)

    # Draw the score
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Score: {score} High Score: {high_score}", True, GREEN)
    screen.blit(text, (10, 10))

   # Draw the game over message
    if game_over:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over! Press SPACE to play again.", True, RED)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))

    # Update the display
    pygame.display.update()

    # Set the game clock
    clock.tick(60)

