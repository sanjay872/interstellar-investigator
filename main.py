import pygame
from leaderboard import display_leaderboard
from database import GameDatabase

pygame.init()


screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shooter Game')


#color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# fonts
font = pygame.font.Font(None, 36)

def draw_button(screen, position, image, text):
    font = pygame.font.Font(None, 36)
    text_render = font.render(text, True, WHITE)
    image_rect = image.get_rect(center=position)
    
    screen.blit(image, image_rect)
    
    text_rect = text_render.get_rect(center=image_rect.center)
    
    screen.blit(text_render, text_rect)
    
    return image_rect 


def main():
    running = True
    show_leaderboard = False
    start_button_image = pygame.image.load('start_button.png').convert_alpha()
    leaderboard_button_image = pygame.image.load('leaderboard_button.png').convert_alpha()


    while running:
        screen.fill(BLACK)

        if show_leaderboard:
            display_leaderboard(screen) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    show_leaderboard = False 
        else:
            start_button_rect = draw_button(screen, (200, 100), start_button_image, "Start Game")
            leaderboard_button_rect = draw_button(screen, (200, 200), leaderboard_button_image, "Leaderboard")


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if start_button_rect.collidepoint(mouse_pos):
                        # Start the game logic here
                        print("Game started!")
                    elif leaderboard_button_rect.collidepoint(mouse_pos):
                        show_leaderboard = True

        pygame.display.flip()


if __name__ == "__main__":
    main()
