# -*- coding: utf-8 -*-
import unittest

class Rectangle(object):

    def is_type(self):
        return 'rectangle'

    def is_shape(self):
        return True

class RectangleTestCase(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle()

    def test_rectangle_type(self):
        self.assertEqual(self.rectangle.is_type(), 'rectangle')

    def test_is_shape(self):
        self.assertTrue(self.rectangle.is_shape())

if __name__ == '__main__':
    unittest.main()