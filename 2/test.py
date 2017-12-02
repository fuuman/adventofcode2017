import unittest
from .door2 import solve, solve2


class ExampleTestsPartOne(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve('5 1 9 5\n7 5 3\n2 4 6 8'), 18)

    def test_1(self):
        self.assertEqual(solve('5 2 9 5\n7 5 3 12\n1 4 6 8'), 23)

    def test_2(self):
        self.assertEqual(solve('5 2 9 5\n7 5 3 12\n1 4 6 8\n1 5 8 5 5 3\n1 2 4 3'), 33)


class ExampleTestsPartTwo(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve2('5 9 2 8\n9 4 7 3\n3 8 6 5'), 9)

    def test_1(self):
        self.assertEqual(solve2('4 2 9\n7 5 3 12\n4 6 8'), 8)

    def test_2(self):
        self.assertEqual(solve2('5 10 14\n3 6 11\n2 14 3'), 11)


if __name__ == '__main__':
    unittest.main()
