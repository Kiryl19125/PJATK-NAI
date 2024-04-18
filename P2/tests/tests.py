import unittest
from P2.main import multiply_vector


def add(a, b):
    return a + b


class TestScalarFunction(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 1)


class TestMultVector(unittest.TestCase):

    def test_1(self):
        self.assertEqual(multiply_vector([1, 2, 3, 4, 5], 2), [2, 4, 6, 8, 10])


if __name__ == '__main__':
    unittest.main()
