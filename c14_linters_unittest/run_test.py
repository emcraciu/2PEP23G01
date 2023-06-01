import unittest
from part2 import my_area_function


class TestAreaFunction(unittest.TestCase):

    def test_valid_area(self):
        self.assertEqual(my_area_function(2, 3), 6)

    def test_length_str(self):
        self.assertRaises(TypeError, my_area_function, '2', 3)

    def test_value_error(self):
        self.assertRaises(ValueError, my_area_function, -2, 3)

    # def test_high_str(self):
    #     self.assertRegex(my_area_function(2, '3'), r'\d\d')


if __name__ == "__main__":
    unittest.main()
