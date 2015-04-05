from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_division(self):
        # Tests that 2/1 always equals 2.

        self.assertEqual(2/1, 2)
