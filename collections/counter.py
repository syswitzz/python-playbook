from collections import Counter

'''Counter Object'''
c = Counter(cats = 4, dogs = 2)    # Counter({'cats': 4, 'dogs': 2})
c = Counter({'a': 1, 'b':2})    # Counter({'b': 2, 'a': 1})
c = Counter(['a', 'b', 'c', 'c'])   # Counter({'c': 2, 'a': 1, 'b': 1})
d = Counter("apple")    # Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})

# when an element do not exist in dictionary and we access it it will throw and error
# when an element do not exist in Counter and we access it it will give 0

'''Counter Functions'''
c.elements()    # gives all the elements
c.most_common(2)  # returns the most common element in tuple (element, count)
c.subtract(list or dict or set or tuple or Counter)    # subtracts the given data from the Counter
c.update(list or dict or set or tuple or Counter)    # adds the given data to the Counter
c.clear()   # empty counter object

'''Counter Operations'''
c + d   # adds the counter c and d
c - d   # subtracts the counter c and d
c & d   # intersection of c and d
c | d   # union of c and d