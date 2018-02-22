# -*- coding: utf-8 -*-
import unittest

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

if __name__ == '__main__':
    unittest.main()