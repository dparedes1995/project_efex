import unittest
from main import filter_and_sort_customers


class TestCustomerFiltering(unittest.TestCase):

    def test_filter_and_sort_customers(self):
        customers = [
            {'ID': 1, 'FIRST_NAME': 'Alex', 'LAST_NAME': 'White'},
            {'ID': 2, 'FIRST_NAME': 'Tyler', 'LAST_NAME': 'Hanson'},
            {'ID': 3, 'FIRST_NAME': 'Jordan', 'LAST_NAME': 'Fernandez'},
            {'ID': 4, 'FIRST_NAME': 'Drew', 'LAST_NAME': 'Bradley'},
            {'ID': 5, 'FIRST_NAME': 'Blake', 'LAST_NAME': 'Fuller'},
            {'ID': 6, 'FIRST_NAME': 'Spencer', 'LAST_NAME': 'Johnston'},
            {'ID': 7, 'FIRST_NAME': 'Ellis', 'LAST_NAME': 'Gutierrez'},
            {'ID': 8, 'FIRST_NAME': 'Morgan', 'LAST_NAME': 'Thomas'},
            {'ID': 9, 'FIRST_NAME': 'Riley', 'LAST_NAME': 'Garza'},
            {'ID': 10, 'FIRST_NAME': 'Peyton', 'LAST_NAME': 'Harris'}
        ]

        expected_output = [
            (1, 'Alex', 'White'),
            (9, 'Riley', 'Garza'),
            (5, 'Blake', 'Fuller'),
            (4, 'Drew', 'Bradley'),
            (2, 'Tyler', 'Hanson')
        ]

        result = filter_and_sort_customers(customers)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
