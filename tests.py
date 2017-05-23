import unittest
import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fizzbuzz.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, "Hello World!")

if __name__ == '__main__':
    unittest.main()
