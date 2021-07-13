'''
Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can
still be iterated through with for loop.
They can be created using functions and the yield statement.
'''
def countdown():
    i= 5
    while i > 0:
        yield i
        i -=1
for i in countdown():
    print(i)
  

#
def countdown(i):
    while i > 0:
        yield i
        i -= 1
for i in countdown(i):
    print(list(countdown(9)))
    
#    
def countdown(i):
    while i > 0:
        yield i
        i -= 1
for i in countdown(9):
    print(list(countdown(9)))
#
def countdown(i):
    while i > 0:
        yield i
        i -= 1
for i in countdown(9):
    print(list(countdown(i)))
  
'''
Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
in fact, they can be infinite
'''
def infinite_sevens():
    while True:
        yield 7
for i in infinite_sevens():
    print(i)
'''
In short, generators aloow you to declaire a function that behaves like an iterator,
i.e. it can be used in a for loop

the generator creates and then "yields" only one value at a time. This saves time in creating 
because instead of the entire list being created before passing,
only one value is created then passed. Also saves space because only one the current exists.
'''

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
            
print(list(numbers(11)))
'''
using generators results in improved performance, which is the result of a lazy
(on damand)generation of values, which translates to lower memory usage. Furthermore, we do not need to wait
until all the elements have been generated before we start to use them.
'''


#practice
'''
create a generator function that splits the string into separate words and outputs the resulting list
'''

sentence =input('請輸入字串: ')
def strsplit():
    for w in sentence:
        sentence.split()
        yield w
        
print(list(strsplit()))  #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']




txt = input('請輸入字串: ')

def words():
    for w in txt.split():
        yield w
        
print(list(words()))  #['hello', 'world']



#練習
world = input('請輸入單字: ')
def make_world():
    word =""
    for ch in world:
        word += ch
        yield word
print(list(make_world()))


#

def make_world():
    word =""
    for ch in "spam":
        word += ch
        yield word
print(list(make_world()))
    
