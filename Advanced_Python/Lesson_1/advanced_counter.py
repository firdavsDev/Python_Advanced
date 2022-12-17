from collections import Counter, deque

#################################################### Counter ####################################################

words = ['a', 'b', 'c', 'f', 'c', 'f','c', 'f', 'a', 'a']
words_count = Counter(words)

print(words_count)
print(words_count.most_common(1))
print(sorted(words_count.elements()))


def example1():
    arr = [1, 2, 3, 4, 5, 6, 1, 2]
    counter = Counter(arr)
    print(counter)  # Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1})


def example2():
    # list of students in class 1
    class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah"
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # How many students in class 1 named James?
    print(c1["James"])

    # How many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "students in class 1 and 2")

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(class2)
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)


def main():
    example1()
    example2()


if __name__ == '__main__':
    main()


#################################################### deque ####################################################

# deque is a double-ended queue. It can be used to add or remove elements from both ends.
# It is thread-safe, which means that multiple threads can access it simultaneously.
# It is faster than the list in terms of execution time for appending and popping elements.

custom_deque = deque([], maxlen=3)

for i in range(1,10):
    custom_deque.append(i)
    print(custom_deque)

custom_deque.rotate()
custom_deque.rotate(2)
print(custom_deque)
