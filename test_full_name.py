import unittest
import full_name

class TestFullName(unittest.TestCase):
    def test_valid_name(self):
        self.assertEqual(full_name.fullName('Steve', 'Jobs'), 'Steve Jobs')

    #Should return an error (-1)
    def test_nonstring_name(self):
        self.assertEqual(full_name.fullName(45, 32), -1)

    #Should strip the whitespace in first and last name
    def test_whitespace(self):
        self.assertEqual(full_name.fullName('Bill  ', 'Gates'), 'Bill Gates')

if __name__ == '__main__':
    unittest.main(verbosity=2)