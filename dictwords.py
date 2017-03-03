import timeit
import funcy as f

def load_words(length, as_set=True):
    filename = "wordlists/scrabble_words_%d.txt" % length
    infile = open(filename,'r')
    content = infile.read()
    infile.close()
    content = content.strip().lower()
    word_list = content.split("\n")
    if as_set:
        word_list = set(word_list)
    return word_list

def load_all_words():
    word_list = []
    for i in range(1,9):
        filename = "wordlists/scrabble_words_%d.txt" % i
        infile = open(filename,'r')
        content = infile.read()
        infile.close()
        content = content.strip().lower()
        word_list=f.merge(word_list, content.split("\n"))
    return word_list

def load_prefix_lists():
    all_words = load_all_words()
    prefix_lists = {}
    for i in range(1,8): #only need prefixes up to 7, right? 
        prefix_lists[i] = set(f.walk(lambda d: d[0:i],all_words))
        prefix_lists[i]= f.select(lambda d: len(d)==i, prefix_lists[i])
    return prefix_lists
    # {'a': ['a','and','android'] ...}
# trying something different
# but what?
# some sort of dictionary of word beginnings
# ['apple','ant','cat','corn','car']
# what are we trying to do? know if any words start with a string.  that way if we dont check for 3 letter words that start with xqu, then 4 letter words, etc.
#{ 'a': {'p':{'p':{'l':{'e':'$'}}} 'n':{'t':'$'}} ...} something like that?




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
    #test_perf(num=100)
    print f.walk(len,load_prefix_lists().values())
  
