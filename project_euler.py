# project euler python functions
def if_multiple(nat_num):
    '''Return True if it is a multiple of 3 or 5. Return False if not'''
    if nat_num % 3 == 0 or nat_num % 5 == 0:
        return True
        return nat_num
    else:
        return False
    
def append_to_array(myList, item_to_append):
    '''Appends a list'''
    myList.append(item_to_append)
    return myList
    print myList
    
def run_myList():
    '''Creates a list from 1 to 100 that is divisible by 3 or 5'''
    myList = [] 
    for i in range(1,100):
        if if_multiple(i):
            append_to_array(myList,i)
    return myList   

def sumNum():
    '''Sums a list created by the function run_myList'''
    x = run_myList()
    sum = 0 
    for i in x:
        sum = sum + int(i)
    return sum
    print sum

def main(x):
    '''I eventually want all my functions to do this'''
    ls = []
    total = 0
    for i in range(x):
        if i%3 == 0 or i%5 ==0:
            print i
            total+= i
            ls.append(i)
    
    print  total
    print ls
