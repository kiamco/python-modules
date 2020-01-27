#file reader
def readFile(filename):
    try:
        sed = open(filename, 'r')
        return sed
    except FileNotFoundError:
        print("file does not exist")
        
def getSum(nums):
    sum = 0

    #accumulate
    for x in range(1, len(nums)):
        sum += int(nums[x])
    return sum

def digits(num):
    try:
        return int(num)
    except:
        return num
        
def runTests():
    print('----------- running tests -----------')
    files = ['bad1.dat','bad2.dat','bad3.dat','bad4.dat','good.dat']
    for x in files:
        input = readFile(x).readlines()
        
        if(isinstance(digits(input[0]), int) 
           and 
           digits(input[0]) == len(input) - 1):
            print(x,': good file, sum: ', getSum(input))
        else:
            print(x,': bad file')
    print('------------- end --------------------\n')
            
        
    
if __name__ == "__main__":
    runTests()
    
    trigger = True
    
    while trigger:
        try:  
            file1 = input("\nPlease enter file name? ")
            line = readFile(file1).readlines()
            trigger = False
            if(file1 ==""):
                line = ''
            else:
                line = readFile(file1).readlines()
        except (AttributeError, TypeError,IndexError) as e:
            print(e)
        
    while True:
        try: 
            if(isinstance(digits(line[0] or ''), int)
                and
                 digits(line[0]or '') == len(line) - 1):
                print(file1,': good file, sum: ', getSum(line))
            else:
                print(file1,': bad file')
                
            file1 = input("Please enter file name? ")


            if(file1 ==""):
                line = ['na']
                file1 = "file does not exist"
            else:
                line = readFile(file1).readlines()
        except (AttributeError, TypeError, IndexError) as e:
            print(e)
       
"""
----------------- run --------------------------------------

----------- running tests -----------
bad1.dat : bad file
bad2.dat : bad file
bad3.dat : bad file
bad4.dat : bad file
good.dat : good file, sum:  55
------------- end --------------------


Please enter file name? bad1.dat
bad1.dat : bad file
Please enter file name? good.dat
good.dat : good file, sum:  55
Please enter file name? bad2.dat
bad2.dat : bad file
Please enter file name?
file does not exist : bad file
Please enter file name?

------------- end---------------------------------------------
"""