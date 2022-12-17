#problem 
# Find the year with the most number of people alive in Python


# Solution 1
from collections import Counter
from itertools import accumulate
import operator

def most_populated(population, single=True):
    delta = Counter(x[0] for x in population)
    delta.subtract(Counter(x[1]+1 for x in population))
    start, end = min(delta.keys()), max(delta.keys())
    years = list(accumulate(delta[year] for year in range(start, end)))
    return max(enumerate(years), key=operator.itemgetter(1))[0] + start if single else \
           [i + start for i, val in enumerate(years) if val == max(years)]
           

# print(most_populated([(1920, 1939), (1911, 1944),(1940, 1955), (1938, 1940)]))

# Solution 2
from collections import Counter
from itertools import chain

def most_pop(pop):
    pop_flat = chain.from_iterable(range(i,j+1) for i,j in pop)
    return Counter(pop_flat).most_common(1)
most_pop([(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939)])
