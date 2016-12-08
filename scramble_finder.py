# this file is used to actually loop through starting tattoos, scramble them, and then check to see if the scrambles are composed of real words
import checkwords
import scramble



def checkWordPairScrambles():
    words = checkwords.word_sets
    for i in range(0,4):
        for word in words[i]:
            #0 and 6 1 and 5 24 33
            for word2 in words[6-i]:
                w1 = word+word2
                checkScramble(w1)
                # can we skip w2 if i==3? i think so...
                if i!=3:
                    w2 = word2+word
                    checkScramble(w2)


def checkScramble(word):
    scrambles = scramble.scramble(word)
    # (s1,s2)
    for tat in scrambles:
        if checkwords.is_words(tat):
            print "%s -> %s" % (word,tat) 




checkWordPairScrambles()
