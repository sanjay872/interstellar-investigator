import pygame
import sys
import time
from database import GameDatabase
from game import Game
from leaderboard import display_leaderboard


class GameStartScreen:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Start Screen")

        self.db = GameDatabase()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Load button images
        button_scale_size = (100, 50)
        self.new_button_image = pygame.transform.scale(
            pygame.image.load('./asserts/Large_Buttons/Colored/start.png').convert_alpha(),
            button_scale_size
        )

        self.continue_button_image = pygame.transform.scale(
            pygame.image.load('./asserts/Large_Buttons/Colored/continue.png').convert_alpha(),
            button_scale_size
        )

        self.leaderboard_button_image = pygame.transform.scale(
            pygame.image.load('./asserts/podium.png').convert_alpha(),
            button_scale_size
        )

        self.font = pygame.font.Font(None, 36)

    def draw_buttons(self, new_button_rect, continue_button_rect):
        self.screen.blit(self.new_button_image, new_button_rect)
        self.screen.blit(self.continue_button_image, continue_button_rect)

    def draw_leader(self):
        leaderboard_button_rect = self.leaderboard_button_image.get_rect(topright=(self.screen_width - 10, 10))
        self.screen.blit(self.leaderboard_button_image, leaderboard_button_rect)
        return leaderboard_button_rect


    def draw_text(self, text, color, x, y):
        text_obj = self.font.render(text, True, (255,0,0))
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)

    def draw_input_box(self, x, y, width, height, text, text_color, box_color=(255, 0, 0)):
        pygame.draw.rect(self.screen, box_color, (x, y, width, height), 2)  # Draw the box border
        text_surface = self.font.render(text, True, text_color)
        self.screen.blit(text_surface, (x + 5, y + (height - text_surface.get_height()) // 2))


    def start_screen(self):
        input_box_rect = pygame.Rect(300, 250, 200, 40)
        input_text = ''
        clock = pygame.time.Clock()
        current_screen = "start"

        # Define button rects for image buttons
        new_button_rect = self.new_button_image.get_rect(center=(self.screen_width // 2 - 75, self.screen_height // 2 + 85))
        continue_button_rect = self.continue_button_image.get_rect(center=(self.screen_width // 2 + 100, self.screen_height // 2 + 85))
        
        running = True
        while running:
            self.screen.fill((0,0,0))
            self.draw_text("Enter Your Name:", self.BLACK, 300, 200)
            self.draw_input_box(input_box_rect.x, input_box_rect.y, input_box_rect.width, input_box_rect.height, input_text, self.BLACK)

            leaderboard_button_rect = self.draw_leader()

            # Draw buttons each frame
            self.draw_buttons(new_button_rect, continue_button_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if current_screen == "start":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if leaderboard_button_rect.collidepoint(event.pos):
                            current_screen = "leaderboard"  # Switch to leaderboard screen
                        elif new_button_rect.collidepoint(event.pos):
                                # New button logic
                            if self.db.check_if_user_exists(input_text):
                                # Notify user the name exists
                                print("Name exists, choose a different name.")
                            else:
                                self.db.create_new_player(input_text)
                                print("Start game...")
                                # TODO: Start the game
                                return input_text
                        elif continue_button_rect.collidepoint(event.pos):
                                # Continue button logic
                            if self.db.check_if_user_exists(input_text):
                                # Start the game with existing player
                                print("Continuing game...")
                                # TODO: Start the game
                                return input_text
                            else:
                                # Notify user the name does not exist
                                print("No username found. Please try again.")

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode
                elif current_screen == "leaderboard":
                    current_screen= display_leaderboard(self.screen)
                print(current_screen)
                #time.sleep(3)


    def main(self):
        self.start_screen()