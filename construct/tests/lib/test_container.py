import unittest

from construct.lib.container import Container

class TestContainer(unittest.TestCase):

    def test_getattr(self):
        c = Container(a=1)
        self.assertEqual(c["a"], c.a)

    def test_setattr(self):
        c = Container()
        c.a = 1
        self.assertEqual(c["a"], 1)

    def test_delattr(self):
        c = Container(a=1)
        del c.a
        self.assertFalse("a" in c)

    def test_eq_eq(self):
        c = Container(a=1)
        d = Container(a=1)
        self.assertEqual(c, d)

    def test_ne_wrong_type(self):
        c = Container(a=1)
        d = {"a": 1}
        self.assertNotEqual(c, d)

    def test_bool_false(self):
        c = Container()
        self.assertFalse(c)

    def test_bool_true(self):
        c = Container(a=1)
        self.assertTrue(c)

    def test_in(self):
        c = Container(a=1)
        self.assertTrue("a" in c)

    def test_not_in(self):
        c = Container()
        self.assertTrue("a" not in c)
