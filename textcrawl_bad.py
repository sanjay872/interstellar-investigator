import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Crawl")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the image
scale = 2
image_logo = pygame.image.load("images/CC.png").convert_alpha()
image = image_logo 

# Set the initial image size and position
image_rect = image.get_rect()
initial_image_height = screen_height // 2
image_height = initial_image_height
image_width = image_rect.width * image_height // image_rect.height
image = pygame.transform.scale(image, (image_width, image_height))
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

# Define text
text = "\n".join([
    "It is a period of war. The 2024 cicada uprising has drastically changed",
    "the landscape of Chicago. Brood XIII and Brood XIX have completely taken",
    "over, replacing the chatterings of politicians and local officials",
    "with the constant buzzing of their tymbal organs. It seems that no one",
    "can withstand their constant onslaught.",
    "No one, that is, except you.",
    "",
    "",
    "You see, a mysterious figure has taken a liking to you. Before the",
    "cicadas began their war against humanity, this figure provided you with",
    "a special spaceship and defense system. With it, you’ll be able to stand",
    "a chance against the horrible bugs. In exchange, this figure requested",
    "you provide it with your firstborn child. But oh no! You have no child,",
    "and wouldn’t give them away even if you did. So the mystery figure",
    "presented an alternative: if you can guess their name, the figure will",
    "kill all the cicadas before their numbers grow too large!",
    "",
    "",
    "When you see and hit *some very small and hard to hit special asteroid or",
    "something*, the game will pause and you’ll be provided with a clue on",
    "what the figure’s name is. Once you think you know the name, click the",
    "*button in the corner or something* to guess! But be careful! If you",
    "guess wrong, the cicadas will attack!"
])

# Set font
font = pygame.font.Font(None, 25)

# Define text rendering function
def render_text(text_lines):
    rendered_lines = []
    for line in text_lines:
        rendered_lines.append(font.render(line, True, WHITE))
    return rendered_lines

# Split text into lines and render text
text_lines = text.split('\n')
rendered_text = render_text(text_lines)

# Define initial text position
y_offset = screen_height

# Define scroll speed
scroll_speed = 2

# Define variables to track key states
up_pressed = False
down_pressed = False

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                y_offset += 10
                scale *= 1.5
            elif event.button == 5:  # Scroll down
                y_offset -= 10
                scale /= 1.5
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Arrow key up
                up_pressed = True
            elif event.key == pygame.K_DOWN:  # Arrow key down
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:  # Arrow key up released
                up_pressed = False
            elif event.key == pygame.K_DOWN:  # Arrow key down released
                down_pressed = False
        if .24 <= scale <= 2:
            image = pygame.transform.scale_by(image_logo, scale) 
            image_rect.center = (screen_width, screen_height / 2)

    # Adjust text position based on key state
    if up_pressed:
        y_offset += scroll_speed
        scale *= 1.5
    elif down_pressed:
        y_offset -= scroll_speed
        scale /= 1.5

    screen.fill(BLACK)

    # Blit the image onto the screen
    screen.blit(image, image_rect)

    # Render text on the screen
    for i, rendered_line in enumerate(rendered_text):
        text_width = rendered_line.get_width()
        x_offset = (screen_width - text_width) // 2
        screen.blit(rendered_line, (x_offset, y_offset + i * 30))

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
