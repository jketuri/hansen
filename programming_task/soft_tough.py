#!/usr/bin/python
# coding=utf-8

''' module for soft tough application '''

from argparse import ArgumentParser
import logging
import re

_LETTER_WORDS = {'S': 'Soft', 'T': 'Tough'}

_LOGGER = logging.getLogger(__name__)


class SoftTough:
    ''' class for soft tough application '''

    def _convert_to_words(
            self,
            letter_codes: str,
            number: int
    ) -> list[str]:
        ''' Converts ST-codes to a word list '''
        _LOGGER.info(
            'Converting %s to a word list with number %d', letter_codes,
            number)
        return list(map(
            lambda letter: _LETTER_WORDS[letter], letter_codes[:number]))

    def _convert_to_sentence(
            self,
            letter_codes: str,
            number: int
    ):
        ''' Converts ST-codes to a sentence '''
        _LOGGER.info(
            'Converting %s to a sentence with number %d', letter_codes, number)
        words = []
        while len(words) < number:
            words.extend(
                self._convert_to_words(
                    letter_codes, number - len(words)))
        return ', '.join(
            words[:-1]) + f' and {words[-1]}.'

    def convert_to_text(
            self,
            letter_codes: str,
            numbers: list[int]
    ):
        ''' Converts letter codes to a text '''
        _LOGGER.info(
            'Converting %s to a text with numbers %s', letter_codes, numbers)
        sentences = []
        for number in numbers:
            sentences.append(
                self._convert_to_sentence(letter_codes, number))
        return '\n'.join(sentences)

    @staticmethod
    def validate_pattern(
            pattern: str
    ) -> str:
        ''' validates letter codes pattern '''
        if not re.match('^[ST]*$', pattern):
            raise ValueError
        return pattern


def soft_tough():
    ''' Converts letter codes to a text '''
    parser = ArgumentParser(
        prog='soft_tough', description='The application converts '
        'each character in a pattern with letters S or T into '
        'human readable text and output the corresponding text.')
    parser.add_argument('pattern', type=SoftTough.validate_pattern)
    parser.add_argument('number', nargs='+', type=int)
    args = parser.parse_args()
    print(SoftTough().convert_to_text(
        letter_codes=args.pattern, numbers=args.number))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    soft_tough()
