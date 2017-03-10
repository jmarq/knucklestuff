import timeit
import funcy as f


def load_word_set_by_length(length, as_set=True):
    filename = "wordlists/scrabble_words_%d.txt" % length
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    content = content.strip().lower()
    word_list = content.split("\n")
    if as_set:
        word_list = set(word_list)
    return word_list


def load_all_words():
    word_list = []
    for i in range(1, 9):
        filename = "wordlists/scrabble_words_%d.txt" % i
        infile = open(filename, 'r')
        content = infile.read()
        infile.close()
        content = content.strip().lower()
        word_list = f.merge(word_list, content.split("\n"))
    return word_list


def load_prefix_lists():
    all_words = load_all_words()
    prefix_lists = {}
    for i in range(1, 8):  # only need prefixes up to 7, right?
        # ignore words that are the length of the prefix or less
        long_enough_words = f.select(lambda d: len(d) > i, all_words)
        # grab the first i letters
        prefix_lists[i] = set(f.walk(lambda d: d[0:i], long_enough_words))
        # this line is probably extraneous at this point, right? 
        # prefix_lists[i]= f.select(lambda d: len(d)==i, prefix_lists[i])
    return prefix_lists
    # {'a': ['a','and','android'] ...}
# trying something different
# but what?
# some sort of dictionary of word beginnings
# ['apple','ant','cat','corn','car']
# what are we trying to do? know if any words start with a string.
# that way if we don't check for 3 letter words that start with xqu, then 4 letter words, etc.
# { 'a': {'p':{'p':{'l':{'e':'$'}}} 'n':{'t':'$'}} ...} something like that?


def test_perf(num=100):
    n = num
    l7 = load_word_set_by_length(7, as_set=False)
    s7 = load_word_set_by_length(7)

    def check_list():
        return "wishful" in l7
    
    def check_set():
        return "wishful" in s7
    l_time = float(timeit.timeit(check_list, number=n))
    s_time = float(timeit.timeit(check_set, number=n))
    ratio = l_time/s_time

    print "list takes %f times more than the set, using %d repetitions" % (ratio, n)
    print "list: %f " % l_time
    print "set: %f" % s_time


if __name__ == "__main__":
    # test_perf(num=100)
    print f.walk(len, load_prefix_lists().values())
