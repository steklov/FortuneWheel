from .players.human import Human
from .players.random_computer import RandomComputer
from .players.probability_computer import ProbabilityComputer
from .challenge import Challenge
from .wheel import Wheel
from random import choice


class Game:
    computers = [
        RandomComputer,
        ProbabilityComputer
    ]

    def __init__(self):
        self._challenges = self._generate_challenges()
        self._players = [Human('Human'), choice(Game.computers)('Computer1'), choice(Game.computers)('Computer2')]
        self._wheel = Wheel()
        self._current_player_id = 0

    @staticmethod
    def _generate_challenges():
        challenges = []
        for i in range(3):
            while True:
                challenge = Challenge()
                if challenge not in challenges:
                    challenges.append(challenge)
                    break
        return challenges

    def start(self):
        for game_round, challenge in enumerate(self._challenges, 1):
            print(f'Start of round {game_round}.')
            self._round(challenge)

    def _round(self, challenge):
        player = self._next_player(0)
        print(f'Topic is "{challenge.topic}".')

        while not challenge.is_challenge_solved():
            print(
                '\n'
                f'Word is "{challenge.get_hidden_word()}".\n'
                f"It's {player.name} turn. Their score is {player.score}."
            )

            wheel_value = self._wheel.get_random_sector()
            print(f'Wheel value is {wheel_value}.')

            if Wheel.is_sector_skip(wheel_value):
                print(f'{player.name} skips turn.')
                player = self._next_player()
            elif Wheel.is_sector_bankrupt(wheel_value):
                print(f'{player.name} is bankrupt.')
                player.score = 0
                player = self._next_player()
            else:
                letter = player.get_guess(challenge.available_letters)
                matches = challenge.get_letter_count(letter)
                if matches == 0:
                    print(f'Letter {letter} is absent in the word.')
                    player = self._next_player()
                else:
                    print(f'Letter {letter} is present in the word {matches} times.')
                    player.score += wheel_value * matches

        print(f'{player.name} wins the round with score {player.score}')
        self._cleanup_other_players(player)

    def _next_player(self, player_id=None):
        if player_id is not None:
            self._current_player_id = player_id
            return self._players[player_id]
        self._current_player_id = (self._current_player_id + 1) % len(self._players)
        return self._players[self._current_player_id]

    def _cleanup_other_players(self, player):
        for other in self._players:
            if other is not player:
                other.score = 0
