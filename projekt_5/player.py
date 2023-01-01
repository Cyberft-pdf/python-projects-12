import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        squere = random.choice(game.available_moves())
        return squere

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            squre = input(self.letter + "\" ted hraje. Kam ted(0-9) ")
            try:
                val= int(squre)
                if val not in game.availeble_moves():
                    raise ValueError

                valid_square = True

            except ValueError:
                print("Neplatný znak. Zkus to znova")

        return val




