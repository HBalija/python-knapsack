#!/usr/bin/python3

import sys


class WebinarKnapsack:

    def __init__(
        self, time_available, available_webinars_number,
            time_per_webinar, credits_per_webinar):

        self.ta = time_available
        self.wn = available_webinars_number
        self.tpw = time_per_webinar
        self.cpw = credits_per_webinar

    def rec_knap(self, iterator, time):
        if iterator == 0:
            return 0
        if self.tpw[iterator - 1] > time:
            return self.rec_knap(iterator - 1, time)
        return max(
            self.rec_knap(iterator - 1, time),
            self.rec_knap(iterator - 1, time - self.tpw[iterator - 1]) + self.cpw[iterator - 1])

    def get_values(self):
        j = self.ta
        values_used = []
        for i in range(self.wn, 0, -1):
            if self.rec_knap(i, j) != self.rec_knap(i - 1, j):
                values_used.append((self.tpw[i-1], self.cpw[i-1]))
                j -= self.tpw[i - 1]

        values_used = values_used[::-1]

        return self.rec_knap(self.wn, self.ta), values_used

    @staticmethod
    def print_values(maximized_time, values):
        sys.stdout.write(str(maximized_time) + '\n')
        for value in values:
            sys.stdout.write('{0} {1} \n'.format(value[0], value[1]))


if __name__ == '__main__':

    time_available = 7
    available_webinars_number = 4
    time_per_webinar = [2, 3, 4, 5]
    credits_per_webinar = [3, 4, 5, 5]

    obj = WebinarKnapsack(time_available, available_webinars_number, time_per_webinar, credits_per_webinar)
    maximum_time, values = obj.get_values()
    WebinarKnapsack.print_values(maximum_time, values)

"""
result:
9
3 4
4 5
"""
