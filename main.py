from textcrawl import VideoPlayer
from game import Game
from front_form import GameStartScreen

def main():
    player = VideoPlayer('asserts/media/textcrawl.mp4')
    player.main()

    game_start_screen = GameStartScreen()
    name = game_start_screen.start_screen()

    game = Game(name)
    game.run()

main()