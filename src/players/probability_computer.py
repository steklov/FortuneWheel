from random import choices

letters_table = [
    ('E', 120),
    ('T', 90),
    ('A', 80),
    ('I', 80),
    ('N', 80),
    ('O', 80),
    ('S', 80),
    ('H', 64),
    ('R', 62),
    ('D', 44),
    ('L', 40),
    ('U', 34),
    ('C', 30),
    ('M', 30),
    ('F', 25),
    ('W', 20),
    ('Y', 20),
    ('G', 17),
    ('P', 17),
    ('B', 16),
    ('V', 12),
    ('K', 8),
    ('Q', 5),
    ('J', 4),
    ('X', 4),
    ('Z', 2),
]


class ProbabilityComputer:
    letters = [letter[0] for letter in letters_table]
    weights = [weight[1] for weight in letters_table]

    def __init__(self, name):
        self.name = name
        self.score = 0

    @staticmethod
    def get_guess(available_letters):
        while True:
            letter = choices(ProbabilityComputer.letters, ProbabilityComputer.weights)[0]
            if letter in available_letters:
                return letter
