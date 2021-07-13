#function 函式/功能
#function 是用來收納程式碼的
#他只是個功能，但不會自己執行

def wash():   #def定義 配上 一個空格，加上自己想取的名子，最後加上():
    print('加水')
    print('加洗衣精')
    print('旋轉')
    
wash()     #這行才會真正啟動function


#parameter參數 ()裡面的東西，想像他是投幣口
def wash(dry):  
    print('加水')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')
wash(True)   #此時會把True丟進參數， 



def add(x, y):   #有幾個投幣口，就一定要投
    print(x + y)
    
add(3, 4)    #7  `

#如果參數一開始就有設定預設值，就可以不用投幣了，也可以只投一個，按順序給

def add(x = 1, y= 1):   #有幾個投幣口，就一定要投
    print(x + y)
    
add(5)    #x = 5 + y =1
add(y= 2)
  


def wash(dry= False, water= 8):  
    print('加水', water, ' 分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')
wash(True, 10)




def average(numbers):
    avg = sum(numbers) / len(numbers)  #進行除法自己會把答案變成FLOAT
    return avg
a = average([1, 2, 3])   #如果沒有return就沒辦法把他存進a



def average(numbers):
    return sum(numbers) / len(numbers) 
print(average([1, 2, 3]))

'''
這個比較特殊，影片中我沒有特別提出。所以請特別注意，不會印的原因是因為程式會出錯
，python規定參數的部分，"沒預設值的"　一定要在　"有預設值的"　的前面，所以上面這個程式不行運作，請看下一題
'''
def hello(x, y= 1):
    print(x, y)
hello(3, 4)   


'''
用FUNCTION檢視是否為潤年
'''


def is_leap(x):
   if x % 4 ==0 and x % 100 !=0:
       return True
   elif x % 400 == 0 and x %3200 != 0:
        return True
   else:
       return False
print(is_leap(2004)) 


def sum_of_list(x):
    return sum(x)

print(sum_of_list([1, 2, 3]))



# 以下的寫法是刻意要讓你看用for loop來做加總
def sum_of_list(numbers):
    sum_number = 0
    for num in numbers:
        sum_number += num
    return sum_number

def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)    

#because the return the func will stop at 0

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(4)) 
#3+3=6   
