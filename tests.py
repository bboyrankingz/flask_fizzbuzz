import unittest
import json

import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fizzbuzz.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, "Hello World!")

    def test_classic_fizzbuzz(self):
        rv = self.app.get('/fizzbuzz/')
        fizzbuzz = json.loads(rv.data)
        self.assertEqual(len(fizzbuzz), 100)
        self.assertEqual(fizzbuzz[2], "fizz")
        self.assertEqual(fizzbuzz[4], "buzz")
        self.assertEqual(fizzbuzz[14], "fizzbuzz")

if __name__ == '__main__':
    unittest.main()
