#!/usr/bin/python3

import threading 
  
FIVE = 5
def add(num): 
    print("thread 1 (5 + 5):{}".format(num + num)) 
  
def multiply(num): 
    print("thread 2 (5 * 5): {}".format(num * num)) 
  
if __name__ == "__main__": 
    thread1 = threading.Thread(target=add, args=(FIVE,)) 
    thread2 = threading.Thread(target=multiply, args=(FIVE,)) 
  
    thread1.start() 
    thread2.start() 
  
    thread1.join() 
    thread2.join() 
  
    print("threads completed") 
    
"""-------------------- run ----------------------
thread 1 (5 + 5):10
thread 2 (5 * 5): 25
threads completed
----------------------- end ----------------------"""
