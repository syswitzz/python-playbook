from collections import deque

# USE - faster if you want to access/remove first/last element

# DECLARATION
deck = deque('hello')   # same as namedtuple we can give this any iterable argument
print(deck)    # deque(['h', 'e', 'l', 'l', 'o'])

# METHODS
deck.append(4)
deck.appendleft('left')     # appends to the first index
deck.pop()
deck.popleft()      # removes from first index
deck.clear()    # removes everything from deck
deck.extend('456')   # takes an iterable argument, appends it to end
deck.extendleft('hello')
print(deck)     # deque(['o', 'l', 'l', 'e', 'h', '4', '5', '6'])

# USEFUL METHODS
deck.rotate(-1)     # deque(['l', 'l', 'e', 'h', '4', '5', '6', 'o'])
deck5 = deque('hellow', maxlen=5)   # deque(['e', 'l', 'l', 'o', 'w'], maxlen=5)
deck5.extend('123')    # deque(['o', 'w', '1', '2', '3'], maxlen=5)
