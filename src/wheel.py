from random import choices

wheel_values = [
    (150, 1),
    (200, 3),
    (250, 2),
    (300, 1),
    (400, 2),
    (450, 1),
    (500, 2),
    (550, 1),
    (600, 2),
    (700, 1),
    (800, 1),
    (900, 2),
    (1000, 1),
    (3500, 1),
    ('skip', 1),
    ('bankrupt', 2)
]


class Wheel:
    values = [value[0] for value in wheel_values]
    weights = [value[1] for value in wheel_values]

    @staticmethod
    def get_random_sector():
        return choices(Wheel.values, Wheel.weights)[0]

    @staticmethod
    def is_sector_bankrupt(sector):
        return sector == 'bankrupt'

    @staticmethod
    def is_sector_skip(sector):
        return sector == 'skip'
