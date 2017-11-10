#!/usr/bin/python3

from functools import lru_cache
import fileinput
import sys


class WebinarKnapsack:

    _DATA_LENGTH_ERROR = 'Four lines required.'
    _DATA_INPUT_ERROR = 'Invalid input.'

    def __init__(
        self, time_available, available_webinars_number,
            time_per_webinar, credits_per_webinar):

        self.ta = time_available
        self.wn = available_webinars_number
        self.tpw = time_per_webinar
        self.cpw = credits_per_webinar

    @classmethod
    def process_input_data(cls, input_data):
        """
        Validates and processes input data. Returns list of items ready for
        object initailzation.
        """
        data = [line.replace(' ', '').strip() for line in input_data]

        if len(data) != 4:
            raise ValueError(cls._DATA_LENGTH_ERROR)
        if len(data[0]) != 1 or len(data[1]) != 1 or len(data[2]) != len(data[3]):
            raise ValueError(cls._DATA_INPUT_ERROR)

        try:
            data_list = []
            for element in data:
                if len(element) == 1:
                    data_list.append(int(element))
                else:
                    data_list.append([int(char) for char in element])
            if data_list[1] != len(data_list[2]):
                raise ValueError(cls._DATA_INPUT_ERROR)
            return data_list
        except Exception as ex:
            raise ValueError(str(ex))

    @lru_cache(maxsize=None)
    def rec_knap(self, iterator, time):
        """
        Performs recursive calculation of max number of points per time given
        and number of courses available.
        """
        if iterator == 0:
            return 0
        if self.tpw[iterator-1] > time:
            # recursion
            return self.rec_knap(iterator-1, time)
        # recursion (included values)
        return max(
            self.rec_knap(iterator-1, time),
            (self.rec_knap(iterator-1, time - self.tpw[iterator-1]) +
                self.cpw[iterator-1]))

    def get_values(self):
        """
        Returns calculation of maximum points and related courses.
        """
        j = self.ta
        values_used = []
        for i in range(self.wn, 0, -1):
            if self.rec_knap(i, j) != self.rec_knap(i-1, j):
                # appending courses used to values_used list
                values_used.append((self.tpw[i-1], self.cpw[i-1]))
                j -= self.tpw[i-1]

        # reversing list to display courses in order given
        values_used = values_used[::-1]

        return self.rec_knap(self.wn, self.ta), values_used

    @staticmethod
    def print_values(max_points, values):
        """
        Prints max value of points for time available and courses included.
        """
        sys.stdout.write(str(max_points) + '\n')
        for value in values:
            sys.stdout.write('{0} {1}\n'.format(value[0], value[1]))


if __name__ == '__main__':

    with fileinput.input() as data_input:
        data = WebinarKnapsack.process_input_data(data_input)

    # initializing object with given data
    obj = WebinarKnapsack(*data)

    # calculating and storing object values
    maximum_time, values = obj.get_values()

    # printing values
    WebinarKnapsack.print_values(maximum_time, values)

    # print(WebinarKnapsack.rec_knap.cache_info())

"""
input file:
7
4
2 3 4 5
3 4 5 5

result:
9
3 4
4 5
"""
