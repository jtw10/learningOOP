# Learning Object-Oriented Programming in Python 3
import datetime


class BigBrain:

    # number of objects in this class
    num_bigbrains = 0

    # class viarbale which dictates the iq growth rate
    iq_growth = 1.01

    def __init__(self, first, last, iq):
        self.first = first
        self.last = last
        self.iq = iq

        # every time a new instance of BigBrain is initiated, increment total by 1
        BigBrain.num_bigbrains += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise_iq(self):
        self.iq = int(self.iq * self.iq_growth)

    @classmethod
    def set_iq_growth(cls, amount):
        cls.iq_growth = amount

    @classmethod
    def from_string(cls, bb_str):
        first, last, iq = bb_str.split('-')
        return cls(first, last, iq)  # this line creates a new object

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False


bb_1 = BigBrain('dhruv', 'ppap', 9001)
bb_2 = BigBrain('jim', 'bob', 9001)

bb_str_1 = 'jimbob1-bob-9001'
bb_str_2 = 'jimbob2-bob-9001'
bb_str_3 = 'jimbob3-bob-9001'

new_bb_1 = BigBrain.from_string(bb_str_1)
print(new_bb_1.first)

"""
The two following lines of code will print the same result.
print(bb_1.fullname())
print(BigBrain.fullname(bb_1))
"""

BigBrain.set_iq_growth(1.05)

print(BigBrain.iq_growth)
print(bb_1.iq_growth)
print(bb_2.iq_growth)

# 2019-08-13 is a tuesday, so the BigBrain.is_weekend() of this date should return false
my_date = datetime.date(2019, 8, 13)
print(BigBrain.is_weekend(my_date))
