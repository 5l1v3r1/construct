import unittest

from construct import GreedyRepeater, OptionalGreedyRepeater, UBInt8
from construct import RangeError

class TestGreedyRepeater(unittest.TestCase):

    def setUp(self):
        self.c = GreedyRepeater(UBInt8("foo"))

    def test_trivial(self):
        pass

    def test_empty_parse(self):
        self.assertRaises(RangeError, self.c.parse, "")

    def test_parse(self):
        self.assertEqual(self.c.parse("\x01"), [1])
        self.assertEqual(self.c.parse("\x01\x02\x03"), [1, 2, 3])
        self.assertEqual(self.c.parse("\x01\x02\x03\x04\x05\x06"),
            [1, 2, 3, 4, 5, 6])

    def test_empty_build(self):
        self.assertRaises(RangeError, self.c.build, [])

    def test_build(self):
        self.assertEqual(self.c.build([1, 2]), "\x01\x02")

class TestOptionalGreedyRepeater(unittest.TestCase):

    def setUp(self):
        self.c = OptionalGreedyRepeater(UBInt8("foo"))

    def test_trivial(self):
        pass

    def test_empty_parse(self):
        self.assertEqual(self.c.parse(""), [])

    def test_parse(self):
        self.assertEqual(self.c.parse("\x01\x02"), [1, 2])

    def test_empty_build(self):
        self.assertEqual(self.c.build([]), "")

    def test_build(self):
        self.assertEqual(self.c.build([1, 2]), "\x01\x02")
