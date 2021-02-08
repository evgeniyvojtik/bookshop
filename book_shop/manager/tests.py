from django.test import TestCase

# Create your tests here.
class TestMyApp(TestCase):
    def test_one(self):
        a = 4
        b = 3
        c = a + b
        self.assertEqual(c, 7   , msg='Error mother fucker!')