#!/usr/bin/python3

import unittest

from knapsack import WebinarKnapsack


class KnapsackTest(unittest.TestCase):

    def setUp(self):
        self.time_available = 7
        self.available_webinars_number = 4
        time_per_webinar = [2, 3, 4, 5]
        credits_per_webinar = [3, 4, 5, 5]
        self.input_data = ['7', '4', '2 3 4 5', '3 4 5 5']
        self.obj = WebinarKnapsack(
            self.time_available, self.available_webinars_number,
            time_per_webinar, credits_per_webinar)

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

    def test_input_processes_and_returns_list_succeeds(self):
        res = WebinarKnapsack.process_input_data(self.input_data)
        self.assertEqual(res, [7, 4, [2, 3, 4, 5], [3, 4, 5, 5]])

    def test_input_raises_value_error_if_wrong_len_of_data(self):
        self.input_data.pop(0)
        with self.assertRaises(ValueError) as e:
            WebinarKnapsack.process_input_data(self.input_data)
        self.assertTrue(
            WebinarKnapsack._DATA_LENGTH_ERROR.format(len(self.input_data))
            in str(e.exception))

    def test_input_raises_value_error_if_wrong_input(self):
        self.input_data[3] = '3 4 5'
        with self.assertRaises(ValueError) as e:
            WebinarKnapsack.process_input_data(self.input_data)
        self.assertTrue(WebinarKnapsack._DATA_INPUT_ERROR in str(e.exception))

    def test_input_raises_value_error_if_wrong_input_type(self):
        self.input_data[3] = '3 4 5 A'
        with self.assertRaises(ValueError) as e:
            WebinarKnapsack.process_input_data(self.input_data)
        self.assertTrue('invalid literal' in str(e.exception))


if __name__ == '__main__':
    unittest.main()
