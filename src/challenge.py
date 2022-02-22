from .questions import questions
from random import choice
from string import ascii_uppercase


class Challenge:
    def __init__(self):
        self.topic = choice(list(questions))
        self.answer = choice(questions[self.topic])
        self.available_letters = ascii_uppercase

    def get_hidden_word(self):
        answer = ''
        for letter in self.answer:
            if letter in self.available_letters:
                answer += '*'
            else:
                answer += letter
        return answer

    def is_challenge_solved(self):
        for letter in self.answer:
            if letter in self.available_letters:
                return False
        return True

    def get_letter_count(self, letter):
        self.available_letters = self.available_letters.replace(letter, '')
        return self.answer.count(letter)

    def __eq__(self, other):
        return self.topic == other.topic and self.answer == other.answer
