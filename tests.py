from checkwords import WordsChecker 
import timeit
import unittest

class TestWordCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.checker = WordsChecker()

    def setUp(self):
        self.checker.cache = {}

    def testWoodshed(self):
        self.assertEquals(self.checker.is_word("woodshed"), True)

    def testdog(self):
        self.assertEquals(self.checker.is_word("dog"),True)

    def testxxxyz(self):
        self.assertEquals(self.checker.is_word("xxxyz"),False) 

    # test multiword match
    def testboomboom(self):
        self.assertEquals(self.checker.is_words("boomboom"),True)


if __name__ == "__main__":
    unittest.main()
