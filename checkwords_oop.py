#check words using prefix lists in algorithm somehow?

from loadwords import load_words, load_prefix_lists

class WordsChecker(object):
    def __init__(self):
        super(WordsChecker,self).__init__()
        self.word_sets = []
        for i in range(0,8):
            self.word_sets.append(load_words(i+1))
        self.prefix_lists = load_prefix_lists()
        self.cache = {}

    def is_word(self,s):
        if s:
            return s in self.word_sets[len(s)-1]
        else:
            return False
    
    def is_words(self,s):
        cached = self.cache.get(s,-1)
        if cached != -1:
            return cached
        i = 1
        len_s = len(s)
        while i <= len_s:
            currently_checking = s[0:i]
            if self.is_word(currently_checking):
                if len_s==i:
                    self.cache[s]=True
                    return True
                elif self.is_words(s[i:]):
                    self.cache[s]=True
                    return True
            if i in self.prefix_lists and currently_checking in self.prefix_lists[i]:
                i+=1
            else:
                self.cache[s]=False
                return False
        self.cache[s]=False
        return False


if __name__=="__main__":
    pass
