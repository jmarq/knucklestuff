import timeit

def load_words(length, as_set=True):
    filename = "wordlists/words%d.txt" % length
    infile = open(filename,'r')
    content = infile.read()
    infile.close()
    content = content.strip()
    word_list = content.split("\n")
    if as_set:
        word_list = set(word_list)
    return word_list




def test_perf(num=100):
    n=num
    l7 = load_words(7, as_set=False)
    s7 = load_words(7)

    def checkList():
        return "wishful" in l7
    
    def checkSet():
        return "wishful" in s7
    l_time = float(timeit.timeit(checkList,number=n))
    s_time = float(timeit.timeit(checkSet, number=n))
    ratio = l_time/s_time

    print  "list takes %f times more than the set, using %d repetitions" % (ratio, n)
    print "list: %f " % l_time
    print "set: %f" % s_time
if __name__ == "__main__":
    test_perf(num=100)
  
