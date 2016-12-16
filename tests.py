import checkwords
import timeit
import unittest

class TestWordCheck(unittest.TestCase):
  
    def testWoodshed(self):
        self.assertEquals(checkwords.is_word("woodshed"), True)

    def testdog(self):
        self.assertEquals(checkwords.is_word("dog"),True)

    def testxxxyz(self):
        self.assertEquals(checkwords.is_word("xxxyz"),False) 

    # test multiword match
    def testboomboom(self):
        self.assertEquals(checkwords.is_words("boomboom"),True)


if __name__ == "__main__":
    unittest.main()
