import unittest

from tests.test_driver import drive


class TestMethods(unittest.TestCase):
    def test_def(self):
        input = "(def! a 6)"
        expected = "6"
        self.assertTrue(drive(input, expected))
        input = "a"
        expected = "6"
        self.assertTrue(drive(input, expected))

        input = "(def! a (+ 2 3))"
        expected = "5"
        self.assertTrue(drive(input, expected))
        input = "a"
        expected = "5"
        self.assertTrue(drive(input, expected))

    def test_let(self):
        input = "(let* (c 2) c)"
        expected = "2"
        self.assertTrue(drive(input, expected))
        input = "c"
        with self.assertRaises(Exception):
            drive(input, expected)
    
    def test_if(self):
        input = "(if True 1 2)"
        expected = "1"
        self.assertTrue(drive(input, expected))

        input = "(if False 1 2)"
        expected = "2"
        self.assertTrue(drive(input, expected))

        input = "(if (if True False True) 1 2)"
        expected = "2"
        self.assertTrue(drive(input, expected))

        input = "(if True 1)"
        expected = "1"
        self.assertTrue(drive(input, expected))

        input = "(if False 1)"
        expected = "None"
        self.assertTrue(drive(input, expected))
    
    def test_fn(self):
        input = "(fn* (a) a)"
        expected = "Function"
        self.assertTrue(drive(input, expected))

        input = "( (fn* (a) a) 7)"
        expected = "7"
        self.assertTrue(drive(input, expected))

        input = "( (fn* (a) (+ a 1)) 10)"
        expected = "11"
        self.assertTrue(drive(input, expected))

        input = "( (fn* (a b) (+ a b)) 2 3)"
        expected = "5"
        self.assertTrue(drive(input, expected))

        input = "(def! fib (fn* (N) (if (= N 0) 1 (if (= N 1) 1 (+ (fib (- N 1)) (fib (- N 2)))))))"
        expected = "Function"
        self.assertTrue(drive(input, expected))

        input = "(fib 1)"
        expected = "1"
        self.assertTrue(drive(input, expected))

        input = "(fib 10)"
        expected = "89"
        self.assertTrue(drive(input, expected))