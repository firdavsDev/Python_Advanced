# #problem 
# # Find the year with the most number of people alive in Python


# # Solution 1
from collections import Counter
from itertools import accumulate
import operator

# def most_populated(population, single=True):
#     delta = Counter(x[0] for x in population)
#     delta.subtract(Counter(x[1]+1 for x in population))
#     start, end = min(delta.keys()), max(delta.keys())
#     years = list(accumulate(delta[year] for year in range(start, end)))
#     return max(enumerate(years), key=operator.itemgetter(1))[0] + start if single else \
#            [i + start for i, val in enumerate(years) if val == max(years)]
           

# # print(most_populated([(1920, 1939), (1911, 1944),(1940, 1955), (1938, 1940)]))

# Solution 2
from collections import Counter
from itertools import chain

def most_pop(pop):
    pop_flat = chain.from_iterable(range(i,j+1) for i,j in pop)
    print(list(pop_flat))
    return Counter(pop_flat).most_common(1)
# print(most_pop([(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939), (1900,2000), (1900,2000), (1900,2000), (1900,2000), (1900,2000)]))

# Solution 3
# a=[[1920,1939], [1911,1944],[1920,1955],[1938,1939], [1900, 2000],[1900, 2000],[1900, 2000],[1900, 2000],[1900, 2000]]
# a = [[1920, 1939], [1911, 1944], [1920, 1955], [1938, 1939],[1936, 1940],[1935, 1940],[1935, 1940]]
# birth_1=[]

# for i in range(0,len(a)):
#     birth_iteam=a[i][1]-1
#     birth_1.append(birth_iteam)

# db=Counter(birth_1)
# the_best_repeat=db.most_common(1)
# db=list(the_best_repeat[0])[0]
# print(db)


l=[(1920, 1938), (1911, 1944), (1920, 1955), (1938, 1939), (1900,2000), (1900,2000), (1900,2000), (1900,2000), (1900,2000)]
tg_yil, ol_yil, roy = list(map(lambda x:x[0],l)), list(map(lambda x:x[1],l)), {}
def func(x):
    l=[k for k in range(len(tg_yil)) if x>=tg_yil[k] and x<=ol_yil[k]]
    roy[x]=len(l)
    return len(l)
a=list(map(lambda x:func(x),range(min(tg_yil),max(ol_yil))))
xayot_max=set(map(lambda x:x if roy[x]==max(a) else 0,roy ))
xayot_max.remove(0)
print([min(xayot_max),max(xayot_max)],max(a)) 