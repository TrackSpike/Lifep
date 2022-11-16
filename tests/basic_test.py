import unittest

from tests.test_driver import drive


class TestMethods(unittest.TestCase):
    def test_atom(self):
        input = "5"
        expected = "5"
        self.assertTrue(drive(input, expected))

        input = "True"
        expected = "True"
        self.assertTrue(drive(input, expected))
        
        input = "False"
        expected = "False"
        self.assertTrue(drive(input, expected))

        input = "None"
        expected = "None"
        self.assertTrue(drive(input, expected))

    def test_list(self):
        input = "(2 3 4)"
        expected = "(2 3 4)"
        self.assertTrue(drive(input, expected))

        input = "(2 3 (1 2 3))"
        expected = "(2 3 (1 2 3))"
        self.assertTrue(drive(input, expected))
        
        input = "((2 3) 3 (1 2 3))"
        expected = "((2 3) 3 (1 2 3))"
        self.assertTrue(drive(input, expected))

        input = "((2 3) 3 (1 2 3))"
        expected = "((2 3) 3 (1 2 3))"
        self.assertTrue(drive(input, expected))