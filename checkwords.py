# check words using prefix lists in algorithm somehow?

from loadwords import load_word_set_by_length, load_prefix_lists, load_all_words


class WordsChecker(object):
    def __init__(self):
        super(WordsChecker, self).__init__()
        self.word_sets = []
        for i in range(0, 8):
            self.word_sets.append(load_word_set_by_length(i+1))
        self.prefix_lists = load_prefix_lists()
        self.all_words = set(load_all_words())
        self.cache = {}

    def is_word(self, s):
        # eventually you should more precisely time the difference between these two.  it is close, but which is better?
        #  use one big list rather than 8 lists
        #  and get rid of length checks, word_sets lookup, subtraction, etc.
        # if s:
        #    return s in self.all_words
        # else:
        #    return False
        return s in self.all_words
    
    # need to make the use of a cache optional, in case machine doesn't have enough memory.
    # how best to do this, without adding much extra checking to the method itself,
    #   which will be called millions of times?
    # maybe another method entirely, and the decision on which one to use could be made once upfront,
    #  either in init method here or in the code that actually calls .is_words(s)
    def is_words(self, s):
        cached = self.cache.get(s, -1)
        if cached != -1:
            return cached
        i = 1
        len_s = len(s)
        while i <= len_s:
            currently_checking = s[0:i]
            if self.is_word(currently_checking):
                if len_s == i:
                    self.cache[s] = True
                    return True
                elif self.is_words(s[i:]):
                    self.cache[s] = True
                    return True
            if i in self.prefix_lists and currently_checking in self.prefix_lists[i]:
                i += 1
            else:
                self.cache[s] = False
                return False
        self.cache[s] = False
        return False


if __name__ == "__main__":
    pass
