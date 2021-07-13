#functional Programming
'''
it is a style of programming that(as the name suggest) is based around functions.
A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson
on functions as objects. Higher-order functions take other functions as arguments, or return them as results.
'''
#20
def apply_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x + 5
print(apply_twice(add_five, 10))

'''
This is difficult for me to explain in words but here goes.

Understanding this problem requires a basic understanding of an algebraic concept called "composition of functions."
Think back to algebra class in high school where you had to evaluate f(g(3)). You first need to evaluate the inner function g, with an input of 3. The output/result of g(3) becomes the input of the outer function f. 

i.e.
given f(x) = x + 2    and    g(x) = 2x - 1    evaluate f(g(3))

First, evaluate g(3).
g(3) = 2(3) - 1
g(3) = 6 - 1
g(3) = 5

Second, take the result/output of g(3) which is 5, and plug it into the outer function f.

f(5) = (5) + 2
f(5) = 7

Thus, 
f(g(3)) = 7

'''

'''
@Santhosh

apply_twice(add_five, 10)

This ↑, according to the actual DEFINITION of the apply_twice function they gave, REALLY means

add_five(add_five(10))

Now, just consider this very similar too the composition of functions of Algebra stuff mentioned above by a fairly long nice comment. Work from inside to outside. So, 

add_five(add_five(10))

really means
add_five(15)

as the inner function, namely add_five(10), Indeed, according to the argument 10 of the inner function add_five(10), along with the very DEFINITION of this add_five function, it is clear that add_five(10) simply will RETURN 10+5 so RETURNS REALLY 15.

Lastly, add_five(15) would RETURN 15+5 so REALLY RETURNS 20, based on similar lines of thinking.

Therefore, print(apply_twice(add_five, 10)) REALLY means print(20), giving 20 as output
'''
#30
def add(x, y):
    return x + y
def do_twice(plus, x, y):
    return plus(plus(x, y),plus(x,y))
a=5
b=10
print(do_twice(add, a, b))


#16
def test(func, arg):
    return func(func(arg))
def mult(x):
    return x * x
print(test(mult, 2))

# Pure Functions:
'''
Functional programming seeks to use pure functions. Pure functions have no side effects,
and return a value depends only on their arguments. This is hoe functions in math work:

    If the answer to all questions is "yes", your function is pure.

1. Does my function depend only on its arguments and nothing else? OR Does my function always return the same result given the same arguments?
2. Can I run my function anywhere in the script without causing any trouble or side effects whatsoever?
3. Can I run my function with the same arguments many times and still return the same result each time?
4. Is it true that my function does not change anything outside it, but only returns something?
5. Can my function be used by other functions or scripts with equal success?
'''
#pure function:
def pure_function(x, y):
    temp = x + 2* y
    return temp / (2*x + y)

#IMPURE FUNCTION:
some_list = []

def impure(arg):
    some_list.append(arg)
    
#Memoization    
'''
Using pure functions have both advantages and disadvantages.
Pure functions are:
1. easier to reason about and test.
2. more efficient. Once the function has been evaluated for an input, the result can be stored
and referred to the next time the function of that input is needed, reducing the number of times the function is called.
This is called memoization
3. easier to run in parallel.

the main disadvantage of using only pure functions is that they majorly complicate the otherwise simpple
task of I/O, since this appears to inherrently require side effects.
They can also be more difficult to write in some situations.
'''
'''
creating a function normally (using def) assigns it to a variable automtically.
This is different from the creation of other objects - such as strings and intergers- which
can be created on the fly, without assigning them to a variables.
The same is possible with functions, provided that they are created using lambda syntax.
Functions created this way are known as anonymous.
This approach is most commonly used when passing a simple function as an argument to another
function. The syntax is shown in the next example and consists of the lambdakeyworld followed
by a list of arguments, a colon, and the expression to evaluate and return.
'''

def my_func(f, arg):
    return f(arg)
my_func(lambda x: 2*x*x, 5)

#4
# lambda 2: 2**2 =4

square = (lambda x: x**2)
print(square(2))
'''
Ok. I had tough time in understanding the syntax. Here it is..

Myfunc(lambda x: 2*x*x, 5)

lambda -> keyword
x -> input argument to the anonymous function. 
2*x*x -> the expression to compute. 
5 -> the function argument. Passed as x.

So basically we are defining a lambda function and calling it at the same time with the argument 5

I am not thinking too much on the applications of this at this time. I hoped there will be much more useful examples in the upcoming lessons..

I think that is useful exactly because you don't want to store a variable or a function which is going to be used only once. A variable takes space
 into the memory. Alot of one time used variables are going to use alot of space into the memory.
'''
#範例1
double = lambda x: x*2
print(double(5))   #10



#範例2
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)  #[4, 6, 8, 12]

#範例3
var = lambda x, y : x + y
sum = var(20, 10)
print(sum)   #30
print(var(10,5))   #15

'''
Lambda functions arent as powerful as named functions.
They can only do things that require a single expression- usually equivalent to a single line of code
'''
#named function:
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))
#lambda
print((lambda x: x**2 + 5*x +4) (-4))

'''
Lambda functions can be assigned to variables, and used like normal functions.
However, there is rarely  good reason to do this- it is better to define a function with def instead.
'''
double = lambda x : x*2
print(double(7))


triple = lambda x: x*3
add = lambda x, y: x + y
print(add(triple(3),4))