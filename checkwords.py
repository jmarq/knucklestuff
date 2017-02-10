from loadwords import load_words

word_sets = []
for i in range(0,8):
  word_sets.append(load_words(i+1)) 


def is_word(s):
    if len(s):
      return s in word_sets[len(s)-1]
    else: 
      return False


# is a string composed of a sequence of words? see if the beginning is a word, then call this recursively on the "tail"
def is_words(s):
    i = 1
    while i <= len(s):
        if is_word(s[0:i]):
            if len(s)==i:
                return True
            elif is_words(s[i:]):
                return True
        i+=1
    return False


if __name__=="__main__":
    pass
