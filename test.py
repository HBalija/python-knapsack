#!/usr/bin/python3

import unittest

from knapsack import Knapsack


class KnapsackTest(unittest.TestCase):

    def setUp(self):
        self.weight_available = 7
        weight_per_item = [2, 3, 4, 5]
        value_per_item = [3, 4, 5, 5]
        self.input_data = ['7', '2 3 4 5', '3 4 5 5']
        self.obj = Knapsack(self.weight_available, weight_per_item, value_per_item)

    def test_rec_knap_returns_zero_if_iterator_equals_zero(self):
        res = self.obj.rec_knap(0, self.weight_available)
        self.assertEqual(res, 0)

    def test_rec_knap_returns_proper_value(self):
        res = self.obj.rec_knap(
            self.obj.number_of_items, self.weight_available)
        self.assertEqual(res, 9)

    def test_get_values_returns_proper_items(self):
        res = self.obj.get_values()
        self.assertEqual(len(res), 2)
        self.assertEqual(res[1], [(3, 4), (4, 5)])

    def test_input_processes_and_returns_list_succeeds(self):
        res = Knapsack.process_input_data(self.input_data)
        self.assertEqual(res, [7, [2, 3, 4, 5], [3, 4, 5, 5]])

    def test_input_raises_value_error_if_wrong_len_of_data(self):
        self.input_data.pop(0)
        with self.assertRaises(ValueError) as e:
            Knapsack.process_input_data(self.input_data)
        self.assertTrue(
            Knapsack._DATA_LENGTH_ERROR.format(len(self.input_data))
            in str(e.exception))

    def test_input_raises_value_error_if_wrong_input(self):
        self.input_data[2] = '3 4 5'
        with self.assertRaises(ValueError) as e:
            Knapsack.process_input_data(self.input_data)
        self.assertTrue(Knapsack._DATA_INPUT_ERROR in str(e.exception))

    def test_input_raises_value_error_if_wrong_input_type(self):
        self.input_data[1] = '3 4 5 A'
        with self.assertRaises(ValueError) as e:
            Knapsack.process_input_data(self.input_data)
        self.assertTrue('invalid literal' in str(e.exception))


if __name__ == '__main__':
    unittest.main()
