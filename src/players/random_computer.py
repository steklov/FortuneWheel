from random import choice


class RandomComputer:
    def __init__(self, name):
        self.name = name
        self.score = 0

    @staticmethod
    def get_guess(available_letters):
        return choice(available_letters)
