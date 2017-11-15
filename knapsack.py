#!/usr/bin/python3

from functools import lru_cache
import fileinput
import sys


class Knapsack:

    _DATA_LENGTH_ERROR = 'Three lines required. File is {} lines long.'
    _DATA_INPUT_ERROR = 'Invalid input.'

    def __init__(self, weight_available, weight_per_item, value_per_item):

        self.wa = weight_available
        self.wpi = weight_per_item
        self.vpi = value_per_item

    @property
    def number_of_items(self):
        return len(self.wpi)

    @lru_cache(maxsize=None)
    def rec_knap(self, iterator, available_weight):
        """
        Performs recursive calculation of max value per weight given
        and number of items available.
        """
        if iterator == 0:
            return 0
        if self.wpi[iterator-1] > available_weight:
            # recursion
            return self.rec_knap(iterator-1, available_weight)
        # recursion (included values)
        return max(
            self.rec_knap(iterator-1, available_weight),
            (self.rec_knap(iterator-1, available_weight - self.wpi[iterator-1])
                + self.vpi[iterator-1]))

    def get_values(self):
        """
        Returns calculation of maximum value and related items.
        """
        j = self.wa
        values_used = []
        for i in range(self.number_of_items, 0, -1):
            if self.rec_knap(i, j) != self.rec_knap(i-1, j):
                # appending items used to values_used list
                values_used.append((self.wpi[i-1], self.vpi[i-1]))
                j -= self.wpi[i-1]

        # reversing list to display items in order given
        values_used = values_used[::-1]

        return self.rec_knap(self.number_of_items, self.wa), values_used

    @classmethod
    def process_input_data(cls, input_data):
        """
        Validates and processes input data. Returns list of items ready for
        object initailzation.
        """
        data = [line.strip() for line in input_data]

        if len(data) != 3:
            # file must be 3 lines long
            raise ValueError(cls._DATA_LENGTH_ERROR.format(len(data)))

        try:
            data_list = []
            # casting values to integers and appending them to data_list
            for element in data:
                if element in data[0]:
                    data_list.append(int(element))
                else:
                    data_list.append([int(char) for char in element.split(' ')])

        except Exception as ex:
            raise ValueError(str(ex))

        if len(data_list[1]) != len(data_list[2]):
                raise ValueError(cls._DATA_INPUT_ERROR)

        return data_list

    @staticmethod
    def print_values(max_points, values):
        """
        Prints max value for weight available and items included.
        """
        sys.stdout.write(str(max_points) + '\n')
        for value in values:
            sys.stdout.write('{0} {1}\n'.format(value[0], value[1]))


if __name__ == '__main__':

    with fileinput.input() as data_input:
        data = Knapsack.process_input_data(data_input)

    # initializing object with given data
    obj = Knapsack(*data)

    # calculating and storing object values
    max_value, items = obj.get_values()

    # printing values
    Knapsack.print_values(max_value, items)

    # print(Knapsack.rec_knap.cache_info())

"""
input file:
190                  - maximum weight
56 59 80 64 75 17    - weight of items
50 50 64 46 50 5     - items value

result:
150                  - max value produced
56 50                - used items listed
59 50                  with weight - value pairs
75 50
"""
