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

def draw_input_box( x, y, width, height, text, text_color, box_color=(255, 0, 0)):
    pygame.draw.rect(screen, box_color, (x, y, width, height), 2)  # Draw the box border
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x + 5, y + (height - text_surface.get_height()) // 2))


# Start screen function
def start_screen():
    input_box_rect = pygame.Rect(300, 425, 200, 40)
    input_text = ''
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        draw_text("Find the answer, Get a powerup!!", font, BLACK, screen, 50, 25)
        draw_text("Hints:", font, BLACK, screen, 50, 50)
        draw_text("-With wit and guile, it's hidden in style.", font, BLACK, screen, 50, 75)
        draw_text("-In woods deep and dark, my name does spark.", font, BLACK, screen, 50, 100)
        draw_text("-Like a tongue-twister whispered low, my name's spelling", font, BLACK, screen, 50, 125)
        draw_text(" dances to and fro.", font, BLACK, screen, 50, 150)
        draw_text("-Not a common name, nor one of might, but a name cackled ", font, BLACK, screen, 50, 175)
        draw_text(" jovially in the dead of night.", font, BLACK, screen, 50, 200)
        draw_text("-Though libraries vast with knowledge teem, my name evades ", font, BLACK, screen, 50, 225)
        draw_text(" most every scheme.", font, BLACK, screen, 50, 250)
        draw_text("-Amidst the creak of a spinning wheel's turn, my name lingers,", font, BLACK, screen, 50, 275)
        draw_text(" for those who discern..", font, BLACK, screen, 50, 300)
        draw_text("-‘Tis a name that rings true in a royal's despair, where straw", font, (255,0,0), screen, 50, 325)
        draw_text("  turns to gold in the midnight air.", font, (255,0,0), screen, 50, 350)

        draw_text("Enter Your Answer:",font, (0,255,0),screen,300,400)
        draw_input_box(input_box_rect.x, input_box_rect.y, input_box_rect.width, input_box_rect.height, input_text, (0,0,0))

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    game_screen(input_text) 
                else:
                    input_text += event.unicode
                

# Game screen function
def game_screen(input_text):
    while True:
        screen.fill(WHITE)
        if input_text == 'rumplestiltskin':
            draw_text("you won!",font, (0,255,0),screen,300,400)
        else:
            draw_text("you lost!",font, (255,0,0),screen,300,400)            
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
