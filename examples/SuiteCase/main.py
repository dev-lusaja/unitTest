# -*- coding: utf-8 -*-
import unittest

# Car

class Car(object):

    def start_engine(self):
        return 1

    def stop_engine(self):
        return 0

class CarTestCase(unittest.TestCase):
    def setUp(self):
        """Configure your Test Case
        """
        self.car = Car()

    def test_start_engine(self):
        self.assertEqual(self.car.start_engine(), 1)

    def test_stop_engine(self):
        self.assertEqual(self.car.stop_engine(), 0)

    def tearDown(self):
        """Clean your Test Case
        """
        self.car = None

# Rectangle

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


# Test Suite Manual

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CarTestCase('test_start_engine'))
    suite.addTest(CarTestCase('test_stop_engine'))
    suite.addTest(RectangleTestCase('test_rectangle_type'))
    suite.addTest(RectangleTestCase('test_is_shape'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
