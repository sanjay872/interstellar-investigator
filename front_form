
import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Start Screen")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Function to display text with a given font
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to display input box
def draw_input_box(surface, x, y, width, height, text):
    pygame.draw.rect(surface, BLACK, (x, y, width, height), 2)
    if len(text) > 0:
        draw_text(text, font, BLACK, surface, x + 5, y + 5)

#buttonnnnnn

# Function to draw buttons
def draw_buttons(surface):
    # Red Button
    RED=(255,0,0)
    red_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 60, 100, 50)
    pygame.draw.rect(surface, RED, red_button_rect)
    red_button_text = font.render("New", True, WHITE)
    red_button_text_rect = red_button_text.get_rect(center=red_button_rect.center)
    surface.blit(red_button_text, red_button_text_rect)

    # Blue Button
    BLUE=(0,0,255)
    blue_button_rect = pygame.Rect(screen_width // 2+50, screen_height // 2 + 60, 150, 50)
    pygame.draw.rect(surface, BLUE, blue_button_rect)
    blue_button_text = font.render("Continue", True, WHITE)
    blue_button_text_rect = blue_button_text.get_rect(center=blue_button_rect.center)
    surface.blit(blue_button_text, blue_button_text_rect)


# Main loop
def start_screen():
    input_box_rect = pygame.Rect(300, 250, 200, 40)
    input_text = ''
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Enter Your Name:", font, BLACK, screen, 300, 200)
        draw_input_box(screen, 300, 250, 200, 40, input_text)
        pygame.display.flip()

        draw_buttons(screen)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        clock.tick(30)

# Example usage
player_name = start_screen()
screen.fill((0, 0, 0))  # Fill the screen with black

# Render text
text_surface = font.render("Welcome to Interstellar Invaders "+player_name, True, (255, 255, 255))  # Render text with antialiasing and white color
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))  # Center the text on the screen
# Blit the text surface onto the screen
screen.blit(text_surface, text_rect)
# Update the display
pygame.display.flip()
time.sleep(5)


