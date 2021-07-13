#argument論點 range(2,10,3) 裡面有三個arguments
#parentheses表示()括號
#DRY principle makes code easier to maintain
#WET principle makes code bad and repetitive
#defthat you can create ur own functions
def my_func():
    print('spam')
    print('egg')
    print('morning')
my_func()


#
def hello():
    print("hi")
hello()

#argument is defined inside the()
def AA(WORD):   
    print(WORD+"!")
AA("SPAM")
AA("EGG")

#define function with more than one arguments, separate with commas
def AA(x,y):
    print(x + y)
    print(x - y)
AA(5,8)

#parameten參數  
#define a function that prints "Yes", if its parameter is an even number, and "No" otherwise.
def even(x):
    if x % 2 == 0:
       print("Yes")
    else:
      print("No")
even(80)

#returning from funtion, such as int or str, return a value that can be used later
def max(x, y):
    if x >= y:
        return x
    else:
        return y
print(max(4, 7))
z = max(8, 5)
print(z)

#int 沒有長度，只有str可以
def shortest_str(x, y):
    if len(x) <= len(y):
        return(x)
    else:
        return(y)
    print(shortest_str("1","2"))

"""once you return a value from a function, it immediately stops being excuted. 
Any code after the return statement will never happen."""
    
def add_number(x, y):
    total = x + y
    return total
    print("this won't be print") 
print(add_number(4,5))

#defined function can be assined and reassigned to variables
def multiply(x, y):
    return x* y
a=4
b=7
opperation=multiply
print(opperation(a,b))
'''
opperation=multiply(4, 7)
print(opperation)
'''


#function can also be used as arguments of other functions
def add(x, y):
    return x + y
def do_twice(func, x, y):
    return func(func(x, y),func(x, y))  #return
a=5
b=10
print(do_twice(add,a,b))


#一樣得到相同的結果 plus可以用其他代稱
def add(x, y):
    return x + y
def do_twice(plus, x, y):
    return plus(plus(x, y),plus(x,y))
a=5
b=10
print(do_twice(add, a, b))

#
def square(x):
    return x* x
def test(func,x):
    test(square,42)

