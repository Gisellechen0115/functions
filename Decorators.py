#Decorators:that modify other functions.
'''
decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you 
don't want to modify.
'''

def decor(func):
   def wrap():
        print("==============")
        func()
        print("==============")
   return  wrap
def print_text():
    print("hello world!")
    print("Good Night")
    
 
decorated = decor(print_text)
decorated()
print_text() #只印出字串



#to understand the last statement about multiple decorations


def decor(func):
   def wrap():
        print("==============")
        func()
        print("==============")
   return  wrap
def decor1(func):
   def wrap1():
        print("*" *15)
        func()
        print("*" *15)
   return  wrap1    

@decor1
@decor
def print_text():
    print("hello world!")
    
print_text();
#show as below
'''
***************
==============
hello world!
==============
***************
'''





def decor(func):
        print("==============")
        func()
        print("==============")
        return  
def print_text():
    print("hello world!")
    print("Good Night")
 
def print_number():
    print(123456789)
    
print_text = decor(print_text)
print_text = decor(print_number)

#print(decor(print_text))  #WE GOT A "NONE" AT THE END


def decor(x):
   def wrap():
        print("==============")
        print(x)
        print("==============")
   return  wrap
def print_text(x):
    return x
 
    
decorated = decor(print_text("hello world!"))
decorated() 


def decorr(x):
        print("==============")
        print(x)
        print("==============")
      
x = input()
decorr(x)
   


def decor(func,func2= "decor"):
    print("==============")
    func()
    print("==============")
    if func2 == "decor":
        print("X"*10)
        print("NICE TRY")
        print("X"*10)
       
def print_text():
    print("hello world!")
    print("Good Night")
    
 
decorated = decor(print_text, "0")



