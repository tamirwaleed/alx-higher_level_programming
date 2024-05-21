#!/usr/bin/python3
""" Unittests for max integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ the unittest class """
    def test_no_arg(self):
        """ no arg """
        self.assertEqual(max_integer(), None)

    def test_normal(self):
        """ normal """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty(self):
        """ a unittest """
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """ a unittest """
        self.assertEqual(max_integer([5]), 5)

    def test_same(self):
        """ a unittest """
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_negative(self):
        """ a unittest """
        self.assertEqual(max_integer([-3, -5, -12]), -3)

    def test_float(self):
        """ a unittest """
        self.assertEqual(max_integer([1.2, 5.6, 3.2, 7.9]), 7.9)

    def test_mix(self):
        """ a unittest """
        self.assertEqual(max_integer([-45, 4.6, -7.6, 0, 45, 12]), 45)

    def test_string(self):
        """ a unittest """
        self.assertEqual(max_integer("tamir"), "t")

    def test_lists(self):
        """ a unittest"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),                            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),float('inf'))
        def test_nan(self):
            """Unittest for max_integer([..])"""
            self.assertEqual(max_integer([99, float('nan'), 100]), 100)

        def test_mixed_list(self):
            """Unittest for max_integer([..])"""
            with self.assertRaises(TypeError):
                max_integer([[], [2], [4], [2, 9], 99, "foo"])

        def test_mixed_list_int_str(self):
            """Unittest for max_integer([..])"""
            with self.assertRaises(TypeError):
                max_integer([99, "foo"])

        def test_none(self):
             """Unittest for max_integer([..])"""
             with self.assertRaises(TypeError):
                 max_integer(None)

        def test_dict(self):
            """Unittest for max_integer([..])"""
            with self.assertRaises(TypeError):
                max_integer([{20: 23, 14: 45}, {"a": "b"}])

        def test_int(self):
            """Unittest for max_integer([..])"""
            with self.assertRaises(TypeError):
                max_integer(98)

        def test_float_err(self):
            """Unittest for max_integer([..])"""
            with self.assertRaises(TypeError):
                max_integer(9.8)
