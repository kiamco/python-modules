import time;


def exp1(id):
    print("expression 1: ", "{0:.2f}".format(round((float(id) / 2), 2)))

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
    print("expression 6: ", 
    "{0:.2f}"
    .format(round(float(id) / (float(len) + 1100.00),2)))

def exp7(len, id):
    print("expression 7: " ,
     int(len) % int(len),
      " and ",
       int(id) * int(id) )

def exp8(id):
    try:
       print("expresison 8: ", int(id)/0)
    except:
        print("expresison 8: ", 1)



def exp9():
    print("expression 9: ",round(float(3.15),1))

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
    while True:
        lastname = input("what is your last name? ")
        
        if lastname.isalpha() and (len(lastname) >= 2 and len(lastname) <= 15) :
            break
        elif (len(lastname) <= 2 or len(lastname) >= 15 ):
            print('minimum char is 2 and maximum is 15')
        else:
            print("Please enter characters A-Z only ")

    while True:
        id = input("What is your student id? ")

        try:
            val = int(id)
            if len(id) == 8:
                break
            else:
                print("id need to hava 8 digits")

        except ValueError:
            print("id needs to be a number")

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

    ts = time.time()

    timestamp = time.strftime('%Y-%m-%d ', time.localtime(ts))

    print('----------------------------')
    print("Today's date is ", timestamp)





""" ------------------- RUN --------------------------
what is your last name? kiamco
What is your student id? 20259571
my_id:  31
n_let:  6
expression 1:  15.50
expression 2:  1
expression 3:  21
expression 4:  37
expression 5:  25
expression 6:  0.03
expression 7:  0  and  961
expresison 8:  1
expression 9:  3.1
----------------------------
Today's date is  2020-01-13

"""