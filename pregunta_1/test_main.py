import unittest
from main import addNumbers


class TestAddNumbers(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(addNumbers(2.3, 1.9), 4)

    def test_case_2(self):
        self.assertEqual(addNumbers(2.34, 5.7), 8)

    def test_case_3(self):
        self.assertEqual(addNumbers(1.1, 3.89), 4)

    def test_case_4(self):
        self.assertEqual(addNumbers(0.1, 0.9), 1)

    def test_case_5(self):
        self.assertEqual(addNumbers(999999.99, 0.01), 1000000)


if __name__ == "__main__":
    unittest.main()
