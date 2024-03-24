
import pygame
import sys
import time
import game

from database import GameDatabase

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Start Screen")

db = GameDatabase()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load button images
button_scale_size = (100, 50)
new_button_image = pygame.transform.scale(
    pygame.image.load('./asserts/Large_Buttons/Colored/start.png').convert_alpha(),
    button_scale_size
)

continue_button_image = pygame.transform.scale(
    pygame.image.load('./asserts/Large_Buttons/Colored/continue.png').convert_alpha(), 
    button_scale_size
)

# Function to draw things
def draw_buttons(surface, new_button_rect, continue_button_rect):
    surface.blit(new_button_image, new_button_rect)
    surface.blit(continue_button_image, continue_button_rect)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_input_box(surface, x, y, width, height, text, font, text_color, box_color=BLACK):
    pygame.draw.rect(surface, box_color, (x, y, width, height), 2)  # Draw the box border
    text_surface = font.render(text, True, text_color)
    surface.blit(text_surface, (x + 5, y + (height - text_surface.get_height()) // 2))


# Start screen function adjusted to use database
def start_screen(db):
    input_box_rect = pygame.Rect(300, 250, 200, 40)
    input_text = ''
    clock = pygame.time.Clock()
    
    # Define button rects for image buttons
    new_button_rect = new_button_image.get_rect(center=(screen_width // 2 - 75, screen_height // 2 + 85))
    continue_button_rect = continue_button_image.get_rect(center=(screen_width // 2 + 100, screen_height // 2 + 85))

    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Enter Your Name:", font, BLACK, screen, 300, 200)
        draw_input_box(screen, input_box_rect.x, input_box_rect.y, input_box_rect.width, input_box_rect.height, input_text, font, BLACK)
        
        # Draw buttons each frame
        draw_buttons(screen, new_button_rect, continue_button_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_button_rect.collidepoint(event.pos):
                    # New button logic
                    if db.check_if_user_exists(input_text):
                        # Notify user the name exists
                        print("Name exists, choose a different name.")
                    else:
                        db.create_new_player(input_text)
                        print("Start game...")
                        # TODO: Start the game
                        game.main()


                        
                elif continue_button_rect.collidepoint(event.pos):
                    # Continue button logic
                    if db.check_if_user_exists(input_text):
                        # Start the game with existing player
                        print("Continuing game...")
                        # TODO: Start the game
                        game.main()

                        
                    else:
                        # Notify user the name does not exist
                        print("No username found. Please try again.")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        clock.tick(30)

# Main game setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Start Screen")

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

player_name = start_screen(db)