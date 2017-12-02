import unittest
from .door1 import solve, solve2


class ExampleTestsPartOne(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve('1122'), 3)

    def test_example2(self):
        self.assertEqual(solve('1111'), 4)

    def test_example3(self):
        self.assertEqual(solve('1234'), 0)

    def test_example4(self):
        self.assertEqual(solve('91212129'), 9)


class ExampleTestsPartTwo(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve2('1212'), 6)

    def test_example2(self):
        self.assertEqual(solve2('1221'), 0)

    def test_example3(self):
        self.assertEqual(solve2('123425'), 4)

    def test_example4(self):
        self.assertEqual(solve2('123123'), 12)

    def test_example5(self):
        self.assertEqual(solve2('12131415'), 4)


if __name__ == '__main__':
    unittest.main()
