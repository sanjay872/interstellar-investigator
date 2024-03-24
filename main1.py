from textcrawl import VideoPlayer
from game import Game
from front_form import GameStartScreen

def main():
    player = VideoPlayer('asserts/textcrawl.mp4')
    player.main()

    game_start_screen = GameStartScreen()
    game_start_screen.start_screen()

    game = Game()
    game.run()

main()