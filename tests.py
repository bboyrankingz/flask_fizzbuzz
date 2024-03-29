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
        self.assertEqual(rv.status, '200 OK')
        fizzbuzz = json.loads(rv.data)
        self.assertEqual(len(fizzbuzz), 100)
        self.assertEqual(fizzbuzz[2], "fizz")
        self.assertEqual(fizzbuzz[4], "buzz")
        self.assertEqual(fizzbuzz[14], "fizzbuzz")

    def test_fizzbuzz_with_one_parameter(self):
        rv = self.app.get('/fizzbuzz/?string1=bon')
        self.assertEqual(rv.status, '200 OK')
        fizzbuzz = json.loads(rv.data)
        self.assertEqual(len(fizzbuzz), 100)
        self.assertEqual(fizzbuzz[2], "bon")
        self.assertEqual(fizzbuzz[4], "buzz")
        self.assertEqual(fizzbuzz[14], "bonbuzz")

    def test_fizzbuzz_with_all_parameters(self):
        rv = self.app.get('/fizzbuzz/?string1=bon&string2=coin&int1=5&int2=9&limit=50')
        self.assertEqual(rv.status, '200 OK')
        fizzbuzz = json.loads(rv.data)
        self.assertEqual(len(fizzbuzz), 50)
        self.assertEqual(fizzbuzz[4], "bon")
        self.assertEqual(fizzbuzz[8], "coin")
        self.assertEqual(fizzbuzz[44], "boncoin")

if __name__ == '__main__':
    unittest.main()
