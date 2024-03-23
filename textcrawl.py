import pygame
import pygame.locals as pl
import cv2

# Function to load a video file
def load_video(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap

# Function to resize the frame to fit window dimensions
def resize_frame(frame, window_width, window_height):
    frame_height, frame_width, _ = frame.shape
    if frame_width > frame_height:
        new_height = int(frame_height * (window_width / frame_width))
        frame = cv2.resize(frame, (window_width, new_height))
    else:
        new_width = int(frame_width * (window_height / frame_height))
        frame = cv2.resize(frame, (new_width, window_height))
    return frame

# Function to get the next or previous frame based on scroll direction
def scroll_video(video, direction, skip_frames=10):
    if direction == 'up':
        # Move to the previous frame
        frame_pos = max(0, video.get(cv2.CAP_PROP_POS_FRAMES) - skip_frames)
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)
    elif direction == 'down':
        # Move to the next frame
        frame_pos = min(video.get(cv2.CAP_PROP_FRAME_COUNT) - 1, video.get(cv2.CAP_PROP_POS_FRAMES) + skip_frames)
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)

# Main function
def main():
    pygame.init()

    # Set up Pygame window
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Scrolling Video')

    # Load the video
    video_path = 'material/textcrawl.mp4'  # Change this to your video file path
    video = load_video(video_path)

    clock = pygame.time.Clock()
    running = True
    scrolled = False

    # Display the first frame of the video
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB
        frame = resize_frame(frame, window_width, window_height)
        frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))  # Swap axes for Pygame display
        window.blit(frame, (0, 0))
        pygame.display.flip()

    while running:
        scrolled = False  # Reset scrolled flag
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pl.MOUSEBUTTONDOWN:
                if event.button == 4:  # scroll up
                    scroll_video(video, 'up')
                    scrolled = True
                elif event.button == 5:  # scroll down
                    scroll_video(video, 'down')
                    scrolled = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scroll_video(video, 'up')
                    scrolled = True
                elif event.key == pygame.K_DOWN:
                    scroll_video(video, 'down')
                    scrolled = True

        if scrolled:
            ret, frame = video.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB
                frame = resize_frame(frame, window_width, window_height)
                frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))  # Swap axes for Pygame display
                window.blit(frame, (0, 0))
                pygame.display.flip()
            else:
                # Reset video to loop
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                scrolled = False
        else:
            # Pause the video by not reading the next frame
            pass

        clock.tick(60)  # Adjust the frame rate as needed

    pygame.quit()

if __name__ == "__main__":
    main()