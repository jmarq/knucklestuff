import checkwords
import timeit
import unittest

class TestWordCheck(unittest.TestCase):
  
    def testWoodshed(self):
        self.assertEquals(checkwords.is_word("woodshed"), True)

    def dog(self):
        self.assertEquals(checkwords.is_word("dog"),True)


if __name__ == "__main__":
    unittest.main()
