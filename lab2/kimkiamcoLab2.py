/*
"""
Write a program that enforces the following expectations of a data set file:

The file must exist
The data in the file must have the following format:
 The file must start with an integer, n
The file must contain n data values
The program prompts the user for the name of a file.  The file is expected to contain data values.  The first line of the file should contain the total number of values, and the remaining lines contain the data. 

Three key potential errors to program for include:

The file might not begin with an integer
There might not be a sufficient number of data values
There may be additional input after reading all data values
For a valid data file, the processing data task is to compute the sum of all the data values in the file.  Print out a result message and the accumulated sum for a valid data file.

Testing Requirements
Error Checking: First, validate  if the user supplied filename exists. Then run the following 5 test files provided to use as test cases for your program.  4 test cases are expected to raise exception conditions.  1 test case is a valid data set.  Generate an accumulated sum for the valid data set.

Test Run Requirements: Use the provided 5 test files below as your test run validator.

bad1.datPreview the document
bad2.datPreview the document
bad3.datPreview the document
bad4.datPreview the document
good.datPreview the document
Here are some other tips and requirements:

1.    Keep provided test files intact

2.    Use a while loop to run test files as your input test suite to generate submission run output

3.    Create user defined functions 

4.    Provide an appropriate display message both for invalid and valid data files.

5.   Be sure to print out the sum value for a valid file.

Here is a sample partial run:

Please enter the file name: nofile.dat
Error: file not found.
Please enter the file name: bad1.dat
Error: file contents invalid.
… 
Please enter the file name: good.dat
The sum is:    

"""

#file reader
def readFile(filename):


#
def getSum():
    
if __name__ == "__main__":
    file = input("Please enter file name: ")
