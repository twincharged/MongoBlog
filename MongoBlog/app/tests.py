from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 2/1 always equals 2.
        """
        self.assertEqual(2/1, 2)