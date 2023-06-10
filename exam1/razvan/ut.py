import unittest
from exam import *


class MyTestCase(unittest.TestCase):
    def test_time_diff(self):
        assert time_diff(["Athens", "Vienna"]) == timedelta(hours=1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
