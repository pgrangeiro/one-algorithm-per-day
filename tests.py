# coding: utf-8
from unittest import TestCase

from bubble_sort import *


class BubbleSortTestCase(TestCase):

    def test_sort_random_list_correctly(self):
        import random

        random_list = [random.choice([item for item in range(1000)]) for count in range(10)]
        BubbleSort.sort(random_list)

        for index in range(len(random_list) - 1):
            self.assertTrue(random_list[index] < random_list[index + 1])

    def test_sort_random_list_sort_all_items(self):
        import random

        random_list = [random.choice([item for item in range(100)]) for count in range(10)]
        test_list = random_list[:]
        BubbleSort.sort(test_list)

        self.assertTrue(all([
            item in random_list
            for item in test_list
        ]))
