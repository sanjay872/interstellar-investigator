import pygame
from database import GameDatabase
import environment


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = 800
score_column_start = 600 

def display_leaderboard(screen):
    db = GameDatabase()
    screen.fill(BLACK)  # Clear the screen or set a background
    leaderboard = db.get_leaderboard()
    font_title = pygame.font.Font("./asserts/font/data-latin.ttf", 48)
    font = pygame.font.Font("./asserts/font/data-latin.ttf", 36)

    title_surface = font_title.render("LEADERBOARD", True, WHITE)
    title_rect = title_surface.get_rect(center=(screen.get_width() / 2, 25))
    screen.blit(title_surface, title_rect)
    
    y_offset = 100

    exit_surface = font.render("USE <ESC> TO EXIT", True, WHITE)
    exit_rect = exit_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() - 50))
    screen.blit(exit_surface, exit_rect)

    pygame.display.flip()

    for rank, player in enumerate(leaderboard, start=1):
        #text_str = f"{rank}. {player['user_name']} - {player['score']}"
        name_str = f"{rank}. {player['user_name']}"
        score_str = f"{player['score']}"
        #text = font.render(text_str, True, WHITE)
        
        name_text = font.render(name_str, True, WHITE)
        name_text_rect = name_text.get_rect(left=100, top=y_offset)
        screen.blit(name_text, name_text_rect)

        score_text = font.render(score_str, True, WHITE)
        score_text_rect = score_text.get_rect(right=score_column_start, top=y_offset)
        screen.blit(score_text, score_text_rect)
            #screen.blit(text, (100, y_offset))
        y_offset += 40 
    
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Use ESC to return to the main screen
                #current_screen = "main"
                    return "start"
