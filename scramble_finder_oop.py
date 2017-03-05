# this file is used to actually loop through starting tattoos, scramble them, and then check to see if the scrambles are composed of real words
from checkwords_oop import WordsChecker
from collections import deque
import scramble

# maybe make this a Class that can store the cache as self.cache

class ScrambleFinder(WordsChecker):
    def __init__(self, limit = False):
        super(ScrambleFinder,self).__init__()
        self.input_tats = []
        for i in range(0,4):
            for word in self.word_sets[i]:
                for word2 in self.word_sets[6-i]:
                    w1 = word+word2
                    self.input_tats.append(w1)
                    if i!=3:
                        w2 = word2+word
                        self.input_tats.append(w2)
        for word in self.word_sets[7]:
            #add the 8 letter words
            self.input_tats.append(word)
        #apply limit if exists
        if limit:
            self.input_tats = self.input_tats[0:limit]
        #get rid of duplicates
        self.input_tats = deque(set(self.input_tats))
    
    def checkScrambles(self):
        while(self.input_tats):
            self.checkScramble(self.input_tats.pop())

    def checkScramble(self,tat):
        scrambles = scramble.scramble(tat)
        for scrambled_tat in scrambles:
            if self.is_words(scrambled_tat):
                print "%s -> %s" % (tat,scrambled_tat)

if __name__ == "__main__":
    scramble_finder = ScrambleFinder()
    scramble_finder.checkScrambles()
