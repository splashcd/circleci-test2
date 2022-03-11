import json
import unittest

from myPackage.some_class import SomeClass


class SomeClassTest(unittest.TestCase):
    def setUp(self):
        self._sc = SomeClass()

    def tearDown(self):
        pass

    def test_eval_arg(self):
        retVal = self._sc.eval_arg("String")
        self.assertIsNone(retVal)
        retVal = self._sc.eval_arg({"key": "String"})
        self.assertIsNone(retVal)
        retVal = self._sc.eval_arg()
        self.assertIsNone(retVal)

    def test_echo_me(self):
        word = "Hello"
        retVal = self._sc.echo_me(word)
        self.assertEqual(retVal, f"{word} {word}")


if __name__ == "__main__":
    unittest.main()
