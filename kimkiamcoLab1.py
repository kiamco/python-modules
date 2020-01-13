
def exp1(id):
    print("expression 1: ", int(id) / 2)

def exp2(id):
    print("expression 2: ", int(id) % 2)

def exp3(n):
    result = 0  

    for x in range(1, n + 1) : 
        result += x

    print("expression 3: ", result)
    
def exp4(x,y):
    print("expression 4: ", int(x) + int(y))
        
def exp5(len, id):
    print("expression 5: ", abs(int(len) - int(id)))

def exp6(id, len):
    print("expression 6: ", int(id) / (int(len) + 1100))

def exp7(len, id):

    # expression 7:            (n_let % n_let) and (my_id * my_id)
    print("expression 7: " , int(len) % int(len), " and ", int(id) * int(id) )

def exp8(id):
    try:
       print("expresison 8: ", int(id)/0)
    except:
        print("expresison 8: ", 1)



def exp9():
    print("expression 9: ",round(3.15,1))

def sumOfdigits(id):
    result = 0

    for x in id:
        result += int(x)
    
    return result

if __name__ == "__main__":
    # Input Error Checking: Validate all user input before computation. 
    #  A valid student id contains only digits and is of length 8. 
    #  A valid last name contains only characters and is of a minimum length 2, 
    # maximum length 15.
    lastname = input("what is your last name? ")
    id = input("What is your student id? ")
    my_id = sumOfdigits(id)
    n_let = len(lastname)

    print("my_id: ", my_id)
    print("n_let: ", n_let)
    exp1(my_id)
    exp2(my_id)
    exp3(n_let)
    exp4(my_id, n_let)
    exp5(n_let, my_id)
    exp6(my_id, n_let)
    exp7(n_let,my_id)
    exp8(my_id)
    exp9()





