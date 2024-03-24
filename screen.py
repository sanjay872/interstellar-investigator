import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Screen Manager Example")

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

# Start screen function
def start_screen():
    while True:
        screen.fill(WHITE)
        draw_text("Start Screen", font, BLACK, screen, 300, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "game"

# Game screen function
def game_screen():
    while True:
        screen.fill(WHITE)
        draw_text("Game Screen pewpew", font, BLACK, screen, 300, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Screen manager function
def main():
    current_screen = "start"
    
    while True:
        if current_screen == "start":
            current_screen = start_screen()
        elif current_screen == "game":
            game_screen()

# Run the screen manager
main()
