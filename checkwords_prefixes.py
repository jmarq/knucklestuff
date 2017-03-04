#check words using prefix lists in algorithm somehow?

from dictwords import load_words, load_prefix_lists

prefix_lists = load_prefix_lists()

word_sets = []
for i in range(0,8):
  word_sets.append(load_words(i+1)) 


def is_word(s):
    if len(s):
      return s in word_sets[len(s)-1]
    else: 
      return False



def is_words(s, cache):
    cached = cache.get(s,-1)
    if cached != -1:
#        print "using cached value for "+s
        return cached
    i = 1
    while i <= len(s):
        currently_checking = s[0:i]
        if is_word(s[0:i]):
            if len(s)==i:
                cache[s]=True
                return True
            elif is_words(s[i:],cache):
                cache[s]=True
                return True
        if i in prefix_lists and currently_checking in prefix_lists[i]:
            i+=1
        else: 
#            print "no words start with %s" % currently_checking
            cache[s]=False
            return False
    cache[s]=False
    return False


if __name__=="__main__":
    pass
