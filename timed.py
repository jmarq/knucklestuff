from timeit import timeit
from scramble_finder import ScrambleFinder

def init_scramblefinder():
    scramble_finder = ScrambleFinder(limit=1000)

def run_scramblefinder():
    scramble_finder = ScrambleFinder(limit=10000)
    scramble_finder.checkScrambles()


def ptime(func, number=1):
    print "took %f seconds for %d iterations" % ( float(timeit(func,number=number)), number )


# ptime(init_scramblefinder)

ptime(run_scramblefinder)

