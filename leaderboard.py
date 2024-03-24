import pygame
from database import GameDatabase


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def display_leaderboard(screen):
    uri = 'mongodb+srv://hhu:hhu@interstellar-investigat.k1riaic.mongodb.net/'
    db = GameDatabase(uri=uri, db_name='test_game_database')
    screen.fill(BLACK)  # Clear the screen or set a background
    leaderboard = db.get_leaderboard()
    font = pygame.font.Font(None, 36)
    y_offset = 50
    
    for rank, player in enumerate(leaderboard, start=1):
        # Format the string to display
        text_str = f"{rank}. {player['user_name']} - {player['score']}"
        text = font.render(text_str, True, WHITE)
        
        # Display each leaderboard entry on the screen
        screen.blit(text, (100, y_offset))
        y_offset += 40 

    pygame.display.flip()
