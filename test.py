#!/usr/bin/python3

import unittest

from knapsack import WebinarKnapsack


class KnapsackTest(unittest.TestCase):

    def setUp(self):
        self.time_available = 7
        self.available_webinars_number = 4
        self.time_per_webinar = [2, 3, 4, 5]
        self.credits_per_webinar = [3, 4, 5, 5]
        self.obj = WebinarKnapsack(
            self.time_available, self.available_webinars_number,
            self.time_per_webinar, self.credits_per_webinar)

    def test_rec_knap_returns_zero_if_iterator_equals_zero(self):
        res = self.obj.rec_knap(0, self.time_available)
        self.assertEqual(res, 0)

    def test_rec_knap_returns_proper_value(self):
        res = self.obj.rec_knap(
            self.available_webinars_number, self.time_available)
        self.assertEqual(res, 9)

    def test_get_values_returns_proper_items(self):
        res = self.obj.get_values()
        self.assertEqual(len(res), 2)
        self.assertEqual(res[1], [(3, 4), (4, 5)])


if __name__ == '__main__':
    unittest.main()
