import unittest

from exam1_pep import calculate_difference


class TestTimeGetter(unittest.TestCase):

    def test_diff(self):
        self.assertEqual(calculate_difference("+03:00", "+02:00"), '1')


if __name__ == '__main__':
    unittest.main()
