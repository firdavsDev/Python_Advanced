from collections import Counter, namedtuple, defaultdict, deque



#################################################### Counter ####################################################

words = ['a', 'b', 'c', 'f', 'c', 'f','c', 'f', 'a', 'a']
words_count = Counter(words)

print(words_count)
print(words_count.most_common(1))
print(sorted(words_count.elements()))



#################################################### namedtuple ####################################################
Point = namedtuple('Point', 'x,y')
print(Point)
p = Point(x=4,y=5)
print(p.count(4))



#################################################### defaultdict ####################################################
QuerySet = namedtuple('QuerySet', 'name,age')
person = QuerySet(name='Ism', age=21)
print(person)

dict_1 = defaultdict(int)

dict_1['a'] = 5
dict_1['b'] = 6
dict_1['c'] = 8

print(dict_1['d'])

#################################################### deque ####################################################
custom_deque = deque([], maxlen=3)

for i in range(1,10):
    custom_deque.append(i)
    print(custom_deque)

custom_deque.rotate()
custom_deque.rotate(2)
print(custom_deque)
