import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Colorful Lines and Eraser")

# Define colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define color options
color_options = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, BLACK, WHITE]
current_color_index = 0

# Set up drawing variables
drawing = False
last_pos = None
brush_size = 5
brush_color = BLACK

# Set up game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                brush_color = WHITE
            elif event.key == pygame.K_c:
                current_color_index = (current_color_index + 1) % len(color_options)
                brush_color = color_options[current_color_index]

    # Draw lines of different colors
    if drawing:
        current_pos = pygame.mouse.get_pos()
        if last_pos is not None:
            pygame.draw.line(screen, brush_color, last_pos, current_pos, brush_size)
        last_pos = current_pos

    # Handle mouse events
    if event.type == pygame.MOUSEBUTTONDOWN:
        drawing = True
        last_pos = pygame.mouse.get_pos()

    elif event.type == pygame.MOUSEBUTTONUP:
        drawing = False

    # Handle key events
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
            brush_size += 1
        elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
            brush_size -= 1
        elif event.key == pygame.K_r:
            current_color_index = 0
            brush_color = RED
        elif event.key == pygame.K_o:
            current_color_index = 1
            brush_color = ORANGE
        elif event.key == pygame.K_y:
            current_color_index = 2
            brush_color = YELLOW
        elif event.key == pygame.K_g:
            current_color_index = 3
            brush_color = GREEN
        elif event.key == pygame.K_b:
            current_color_index = 4
            brush_color = BLUE
        elif event.key == pygame.K_p:
            current_color_index = 5
            brush_color = PURPLE
        elif event.key == pygame.K_k:
            current_color_index = 6
            brush_color = BLACK

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

