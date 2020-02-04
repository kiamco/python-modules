#!/usr/bin/python3
import re
import calendar

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
    if(month == "02"):
        is_leap(int(year))

    # build string if valid format
    try:
        if(len(month) == 2 and
         (len(date) == 2 and int(date) <= months.get(month).get("days")) and 
         len(year) == 4):
            convertedMonth = months.get(month).get("date")
            finalStr = f'{convertedMonth} {date}, {year}'
        else:
            raise SystemExit('invalid format')
    except(UnboundLocalError, AttributeError) as e:
        raise SystemExit('invalid format')

    return finalStr


def is_leap(year):
    if(calendar.isleap(year)):
        months["02"] = {"date": "February", "days": 29, "is_leap": True}
        

date = input("Enter a date (mm/dd/yyyy): ")
convertedDate = converter(date)
print(f"the converted date is: {convertedDate}")
