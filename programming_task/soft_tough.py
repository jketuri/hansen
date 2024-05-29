#!/usr/bin/python
# coding=utf-8

from logging import Logger
from argparse import ArgumentParser

LETTER_WORDS = {'S': 'Soft', 'T': 'Tough'}

class SoftTough:

    def convert_to_words(
            self,
            letter_codes: str,
            number: int
    ) -> list[str]:
        return list(map(
            lambda letter: LETTER_WORDS[letter], letter_codes[:number]))


    def convert_to_sentence(
            self,
            letter_codes: str,
            number: int
    ):
        words = []
        while len(words) < number:
            words.extend(
                self.convert_to_words(
                    letter_codes, number - len(words)))
        return ', '.join(
            words[:-1]) + f' and {words[-1]}.'


    def convert_to_text(
            self,
            letter_codes: str,
            numbers: list[int]
    ):
        sentences = []
        for number in numbers:
            sentences.append(
                self.convert_to_sentence(letter_codes, number))
        return '\n'.join(sentences)


def soft_tough():
    parser = ArgumentParser(
        prog='soft_tough', description='The application converts '
        'each character in a pattern with letters S or T into '
        'human readable text and output the corresponding text.')
    parser.add_argument('pattern')
    parser.add_argument('number', nargs='+', type=int)
    args = parser.parse_args()
    print(SoftTough().convert_to_text(
        letter_codes=args.pattern, numbers=args.number))


if __name__ == "__main__":
    soft_tough()
