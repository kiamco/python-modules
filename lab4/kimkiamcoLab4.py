#!/usr/bin/python3

import re
import calendar

FEB = "02"

months = {
    "01": {"date":"January", "days":31},
    "02": {"date": "February","days": 28, "is_leap": False},
    "03": {"date": "March","days": 31},
    "04": {"date": "April","days": 30},
    "05": {"date": "May","days": 31},
    "06": {"date": "June","days": 30},
    "07": {"date": "July","days": 31},
    "08": {"date": "August","days": 31},
    "09": {"date": "September","days": 30},
    "10": {"date": "October","days": 31},
    "11": {"date": "Novemeber","days": 30},
    "12": {"date": "December","days": 31},
}

def converter(date):
    convert = re.split(r"\/",date)
    if(len(convert) == 3):
        try:
            month = convert[0]
            date = convert[1] 
            year = convert[2]
        except(IndexError) as e :
            raise SystemExit('invalid format')
    else:
        raise SystemExit('invalid format')
        
    #check if yea is leap
    if(month == FEB):
        try:    
            is_leap(int(year))
        except TypeError as e:
            raise SystemExit('invalid year')

    # build string if valid format
    try:
        if(len(month) == 2 and
         (len(date) == 2 and int(date) <= months.get(month).get("days")) and 
         len(year) == 4 and 
         is_valid_year(year) == True ):
            convertedMonth = months.get(month).get("date")
            finalStr = f'{convertedMonth} {date}, {year}'
        else:
            print('date does not exist')
        
            raise SystemExit('invalid format')
    except(UnboundLocalError, AttributeError,TypeError) as e:
        raise SystemExit('invalid format')

    return finalStr


def is_leap(year):
    if(calendar.isleap(year)):
        months[FEB] = {"date": "February", "days": 29, "is_leap": True}

def is_valid_year(year):

    if(list(year)[0] == '0'):
        return False
    else:
        return True

date = input("Enter a date (mm/dd/yyyy): ")
convertedDate = converter(date)
print(f"the converted date is: {convertedDate}")

while(date):
    date = input("Enter a date (mm/dd/yyyy): ")
    convertedDate = converter(date)
    print(f"the converted date is: {convertedDate}")


"""------------------ run ----------------------
Enter a date (mm/dd/yyyy): 02/28/2019
the converted date is: February 28, 2019
Enter a date (mm/dd/yyyy): 01/01/2020
the converted date is: January 01, 2020
Enter a date (mm/dd/yyyy): 03/03/1994
the converted date is: March 03, 1994
Enter a date (mm/dd/yyyy): 02/29/2020
the converted date is: February 29, 2020
Enter a date (mm/dd/yyyy): 02/29/0100
date does not exist
invalid format
"""


