# Blog: https://blog.csdn.net/fengbingchun/article/details/119966415

# reference: https://www.programiz.com/python-programming/iterator
my_list = [1, 3, 5] # define a list
if 0:
    my_iter = iter(my_list) # get an iterator using iter()
    print(next(my_iter)) # iterate through it using next()
    print(my_iter.__next__()) # next(obj) is name as obj.__next__()
    print(my_iter.__next__()) # 5
    #print(my_iter.__next__()) # this will raise error(StopIteration), no items left
else: # use the for loop
    for element in iter(my_list): # 迭代器对象可以使用for语句进行遍历
        print(element, end=" ")

'''
for element in iterable:
    # do something with element

Is actually implemented as:
# create an iterator object from that iterable
iter_obj = iter(iterable)
while True: # infinite loop
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
'''

# reference: https://www.geeksforgeeks.org/iterators-in-python/
class Test:
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object, Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3, we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x

# Prints numbers from 10 to 15
print("\n")
for i in Test(15):
    print(i, end=" ")

print("\n")
value = iter(Test(11))
print(next(value))
print(next(value))
#print(next(value)) # raise StopIteration

print("test finish")
