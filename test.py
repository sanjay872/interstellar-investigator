import pygame
pygame.init()

from pygame import mixer
mixer.init()

#background-music
mixer.music.load('Rock_Metal_Valhalla_by_Alexander_Nakarada.mp3')
mixer.music.play(-1)

#laser sound while shooting
mixer.music.load('laser_shoot.mp3')
mixer.music.play()

#when player loses
mixer.music.load('videogame-death-sound.mp3')
mixer.music.play()

#boss music
mixer.music.load('high_beats.mp3')
mixer.music.play()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello, World with Music!")

# Set up colors
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Load music files
music_files = ["Rock_Metal_Valhalla_by_Alexander_Nakarada.mp3", "high_beats.mp3"]  # Add your music files here
current_music_index = 0
pygame.mixer.music.load(music_files[current_music_index])

# Function to play next music
def play_next_music():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
                if button_rect.collidepoint(mouse_pos):
                    play_next_music()

    # Fill the background with white
    screen.fill(WHITE)

    # Render text
    text = font.render("Hello, World!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))

    # Render button
    button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    button_text = font.render("Change Music", True, (0, 0, 0))
    button_text_rect = button_text.get_rect(center=button_rect.center)

    # Blit the text and button onto the screen
    screen.blit(text, text_rect)
    screen.blit(button_text, button_text_rect)

    # Update the display
    pygame.display.flip()

