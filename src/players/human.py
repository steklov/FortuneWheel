from string import ascii_uppercase


class Human:
    def __init__(self, name):
        self.score = 0
        self.name = name

    @staticmethod
    def get_guess(available_letters):
        while True:
            guess = input('Input letter: ').upper()
            if len(guess) != 1:
                print('Incorrect input, try again.')
            elif guess not in ascii_uppercase:
                print('This is not a letter, try again.')
            elif guess not in available_letters:
                print('This letter is not available, try again.')
            else:
                break
        return guess
