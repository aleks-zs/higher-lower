from game import Game

the_game = Game()

the_game.game_initial_step()
while the_game.still_rolling:
    the_game.game_step()
