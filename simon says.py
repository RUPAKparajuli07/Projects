import pygame
import random
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simon Says")
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define button properties
button_size = 100
button_margin = 20

# Define button positions
button_1_pos = (button_margin, button_margin)
button_2_pos = (screen_width - button_size - button_margin, button_margin)
button_3_pos = (button_margin, screen_height - button_size - button_margin)
button_4_pos = (screen_width - button_size - button_margin, screen_height - button_size - button_margin)

# Define button colors
button_1_color = RED
button_2_color = GREEN
button_3_color = YELLOW
button_4_color = BLUE

# Define button order
button_order = []
# Main game loop
running = True
while running:

    # Display buttons
    pygame.draw.rect(screen, button_1_color, (button_1_pos[0], button_1_pos[1], button_size, button_size))
    pygame.draw.rect(screen, button_2_color, (button_2_pos[0], button_2_pos[1], button_size, button_size))
    pygame.draw.rect(screen, button_3_color, (button_3_pos[0], button_3_pos[1], button_size, button_size))
    pygame.draw.rect(screen, button_4_color, (button_4_pos[0], button_4_pos[1], button_size, button_size))

    # Play button sequence
    if len(button_order) < 4:
        button_order.append(random.choice([1, 2, 3, 4]))
    else:
        for button in button_order:
            pygame.time.wait(500)
            if button == 1:
                pygame.draw.rect(screen, WHITE, (button_1_pos[0], button_1_pos[1], button_size, button_size))
                pygame.display.update()
                pygame.time.wait(500)
                pygame.draw.rect(screen, button_1_color, (button_1_pos[0], button_1_pos[1], button_size, button_size))
            elif button == 2:
                pygame.draw.rect(screen, WHITE, (button_2_pos[0], button_2_pos[1], button_size, button_size))
                pygame.display.update()
                pygame.time.wait(500)
                pygame.draw.rect(screen, button_2_color, (button_2_pos[0], button_2_pos[1], button_size, button_size))
            elif        button == 3:
                pygame.draw.rect(screen, WHITE, (button_3_pos[0], button_3_pos[1], button_size, button_size))
                pygame.display.update()
                pygame.time.wait(500)
                pygame.draw.rect(screen, button_3_color, (button_3_pos[0], button_3_pos[1], button_size, button_size))
            elif button == 4:
                 pygame.draw.rect(screen, WHITE, (button_4_pos[0], button_4_pos[1], button_size, button_size))
                 pygame.display.update()
                 pygame.time.wait(500)
                 pygame.draw.rect(screen, button_4_color, (button_4_pos[0], button_4_pos[1], button_size, button_size))
            pygame.display.update()
        button_order = []

# Check player input
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            if button_order[0] == 1:
                print("Correct!")
            else:
                print("Incorrect!")
        elif event.key == pygame.K_2:
            if button_order[0] == 2:
                print("Correct!")
            else:
                print("Incorrect!")
        elif event.key == pygame.K_3:
            if button_order[0] == 3:
                print("Correct!")
            else:
                print("Incorrect!")
        elif event.key == pygame.K_4:
            if button_order[0] == 4:
                print("Correct!")
            else:
                print("Incorrect!")
pygame.quit()
