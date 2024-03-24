import pygame
import cv2
import pygame.locals as pl
from pygame import mixer

class VideoPlayer:
    def __init__(self, video_path, window_width=800, window_height=600, skip_frames=30):
        self.video_path = video_path
        self.window_width = window_width
        self.window_height = window_height
        self.skip_frames = skip_frames
        self.video = None
        self.end_position = 0
        self.window = None
        self.clock = None
        self.running = False
        self.scrolled = False
        self.arrow_held = {'up': False, 'down': False}
        self.skip_button_rect = pygame.Rect(window_width - 100, window_height - 50, 80, 30)
        mixer.init()
        mixer.music.load('asserts/textmusic.mp3')
        pygame.mixer.music.set_volume(1)  # Set volume (0.0 to 1.0)
        mixer.music.play(-1)

    def load_video(self):
        self.video = cv2.VideoCapture(self.video_path)
        self.end_position = self.video.get(cv2.CAP_PROP_FRAME_COUNT)

    def resize_frame(self, frame):
        frame_height, frame_width, _ = frame.shape
        if frame_width > frame_height:
            new_height = int(frame_height * (self.window_width / frame_width))
            frame = cv2.resize(frame, (self.window_width, new_height))
        else:
            new_width = int(frame_width * (self.window_height / frame_height))
            frame = cv2.resize(frame, (new_width, self.window_height))
        return frame

    def scroll_video(self, direction):
        if direction == 'up':
            frame_pos = max(0, self.video.get(cv2.CAP_PROP_POS_FRAMES) - self.skip_frames)
            self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)
        elif direction == 'down':
            frame_pos = min(self.video.get(cv2.CAP_PROP_FRAME_COUNT) - 1, self.video.get(cv2.CAP_PROP_POS_FRAMES) + self.skip_frames)
            self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)

    def main(self):
        pygame.init()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Intro Textcrawl')

        self.load_video()

        self.clock = pygame.time.Clock()
        self.running = True
        self.scrolled = False

        ret, frame = self.video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = self.resize_frame(frame)
            frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            self.window.blit(frame, (0, 0))
            self.draw_skip()
            pygame.display.flip()

        while self.running:
            self.scrolled = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pl.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.scroll_video('up')
                        self.scrolled = True
                    elif event.button == 5:
                        self.scroll_video('down')
                        self.scrolled = True
                    elif event.button == 1:  # Check if left mouse button is clicked
                        if self.skip_button_rect.collidepoint(event.pos):  # Check if click is inside skip button
                            pygame.mixer.music.stop()
                            return # Quit Pygame

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.arrow_held['up'] = True
                    elif event.key == pygame.K_DOWN:
                        self.arrow_held['down'] = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.arrow_held['up'] = False
                    elif event.key == pygame.K_DOWN:
                        self.arrow_held['down'] = False

            for direction, held in self.arrow_held.items():
                if held:
                    self.scroll_video(direction)
                    self.scrolled = True

            if self.scrolled:
                ret, frame = self.video.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = self.resize_frame(frame)
                    frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                    self.window.blit(frame, (0, 0))
                    self.draw_skip()
                    pygame.display.flip()
                else:
                    self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    self.scrolled = False
            else:
                pass

            self.clock.tick(60)

            if self.video.get(cv2.CAP_PROP_POS_FRAMES) >= self.end_position:
                break

        pygame.quit()

    def draw_skip(self):
        pygame.draw.rect(self.window, (255, 255, 0), self.skip_button_rect)  
        skip_button_font = pygame.font.Font(None, 24)
        skip_button_text = skip_button_font.render("Skip", True, (0, 0, 0))
        skip_button_text_rect = skip_button_text.get_rect(center=self.skip_button_rect.center)
        self.window.blit(skip_button_text, skip_button_text_rect)