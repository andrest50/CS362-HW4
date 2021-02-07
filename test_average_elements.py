import unittest
import average_elements

class TestAverageElements(unittest.TestCase):
    def test_int_list(self):
        numbers = [2, 7, 1, 4, 11]
        self.assertEqual(average_elements.averageElements(numbers), 5)

    #Should return an error (-1)
    def test_empty_list(self):
        numbers = []
        self.assertEqual(average_elements.averageElements(numbers), -1)

    def test_float_list(self):
        numbers = [2.7, 3.4, 9.1, -2.1, 4.5]
        self.assertEqual(average_elements.averageElements(numbers), 3.52)

if __name__ == '__main__':
    unittest.main(verbosity=2)
