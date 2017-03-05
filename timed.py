from timeit import timeit
from scramble_finder_oop import ScrambleFinder

def init_scramblefinder():
    scramble_finder = ScrambleFinder(limit=1000)

def run_scramblefinder():
    scramble_finder = ScrambleFinder(limit=1000000)
    scramble_finder.checkScrambles()


def ptime(func, number=1):
    print "took %f seconds" % float( timeit(func, number=number))


#ptime(init_scramblefinder)

ptime(run_scramblefinder)

