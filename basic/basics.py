# ORIDNAL VALUE (ASCII)
print('a'> 'Z')   #true
print(ord('a'))   #97
print(ord('Z'))   #90   
print('ab' > 'ac')    #false


# F-STRINGS
y = 4
x = f'hello {5+y}' # f-string allows you to embed expressions inside string literals, using curly braces `{}`.


# ORDER:  not -1st, and -2nd, or -last
print(True or False)   #true
print(True and False)  #false
print(True and not False)  #true


# LISTS -  lists are mutable that means they do not store copy to the list but instead a reference to the list
list1 = [True, "hello", 69] # order is important
print(len(list1))
print(len("hi"))
list1.append(4)
list1.extend([4,5])
list1.pop()  # remove and return last element
list1.pop(3)    # pop the 4th element
print(list1[0])
list1[0] = 'owo'
list2 = [[], list1, [[[]]], ([]), (), "hey"]


# TUPLE - immutable list. means we cannot change, append or remove elements
tuple1 = ("hi", False, 68)


# FOR LOOP
for i in range(1, 10, 2):   # start = 1, stop 10, skip_by = 2  // it goes till stop but stop is not included
    print(i, end=' ')
for i in list1:
    print(i, end=' ')
for i in range(len(list1)):
    print(list1[i], end=' ')
for i, element in enumerate(list1):
    print(i, element, end=' ')


# SLICE OPERATOR - [start:stop:step]  // note that stop is not included it goes till stop but doesnt include it
sliced = [1,2,3,4,5,6][::-1]    # prints reverse of the list
sliced = [1,2,3,4,5,6][4:1:-1]  # start = 1, stop 10, skip_by = 2
sliced2 = "helo world"[1:8:2]
print(sliced, " ", sliced2)


# SET - unordered unique collection of elements. fast lookups, removals or additions. usually used to check if certain elements exist or not
set1 = set()    # dont use set1 = {} because it will create dictionary if left empty
set2 = {3,4,1,3,5,5}

print(4 in set2)   # true (Set does this faster than List)

set1.add(2)
set2.remove(3)
set1.union(set2)
set1.difference(set2)
set1.intersection(set2)


# DICTIONARY - {key, value} pair
dict1 = {"key": 4}
dict1[2] = True

print(dict1['key'])
print(2 in dict1)

dict1.keys()
list3 = [dict1.values()]

del dict1[2]

for key, value in dict1.items():
    print(key, value)
for key in dict1:
    print(key, dict1[key])


# COMPREHENSIONS 
x = [x-1 for x in range(5) if True]   # list [-1,0,1,2,3 ]
x1 = {x+1:x*5 for x in range(5) if True} # dict
x2 = {x+1 for x in range(5) if True} # set


# FUNCTIONS
def func(x:int, y:str="hi"):
    return x, y # function returns in touple

hello, world = func(7, "hello")

# *args allows a function to accept any number of positional arguments as a tuple, while
# **kwargs lets a function accept any number of keyword arguments as a dictionary.
def example(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

example(1, 2, 3, a=4, b=5)  #args: (1, 2, 3)\n kwargs: {'a': 4, 'b': 5}


# LAMBDA, MAP & FILTER - one line anonymous function
function1 = lambda i, j: i+j    # function1 is a lambda function of parameters i and j. operation: i+j
condition = lambda i: i%2==0  # condition is a lambda function that checks if i is even
li2 = map(function1, [1,2,3,4,5,6,7,8,9,10])  # map applies the function1 x to each element in the list
li3 = filter(condition, [1,2,3,4,5,6,7,8,9,10])  # filter applies the condition to each element in the list and returns only those that return True


# EXCEPTIONS
try:
    print("338"+0)
except Exception as e:
    print("well you cant add int to string")
    print(e)
finally:
    print('338'+'0')

raise Exception("Bad. jk, just an example")
