#!/usr/bin/python
# coding=utf-8

from unittest import TestCase
import unittest
from soft_tough import SoftTough

class TestSoftTough(TestCase):

    def test_convert_to_words(self):
        soft_tough = SoftTough()
        self.assertEqual(
            soft_tough._convert_to_words('SST', 3),
            ['Soft', 'Soft','Tough'])
        
    def test_convert_to_sentence(self):
        soft_tough = SoftTough()
        self.assertEqual(
            soft_tough._convert_to_sentence('SST', 5),
            'Soft, Soft, Tough, Soft and Soft.')

    def test_convert_to_text(self):
        soft_tough = SoftTough()
        self.assertEqual(
            soft_tough._convert_to_text('SST', [5, 2]),
            'Soft, Soft, Tough, Soft and Soft.\nSoft and Soft.')

if __name__ == '__main__':
    unittest.main()
