# this file is used to actually loop through starting tattoos, scramble them, and then check to see if the scrambles are composed of real words
import checkwords_prefixes as checkwords
import scramble



def checkWordPairScrambles():
    words = checkwords.word_sets
    input_tats = []
    cache = {}
    for i in range(0,4):
        #print i
        for word in words[i]:
            #0 and 6 1 and 5 24 33
            for word2 in words[6-i]:
                w1 = word+word2
                input_tats.append(w1)
                # can we skip w2 if i==3? i think so...
                if i!=3:
                    w2 = word2+word
                    input_tats.append(w2)
    checkScrambles(input_tats,cache)

def checkScramble(word, cache):
    scrambles = scramble.scramble(word)
    # (s1,s2)
    for tat in scrambles:
        if checkwords.is_words(tat,cache):
            print "%s -> %s" % (word,tat) 
            pass


def checkScrambles(word_list, cache):
    for word in word_list:
        checkScramble(word,cache)


if __name__ == "__main__":
    checkWordPairScrambles()
