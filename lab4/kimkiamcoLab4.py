#!/usr/bin/python3
import re


months = {
    "01": {"date":"January", "days":31},
    "02": {"date": "February","days": 31},
    "03": {"date": "March","days": 31},
    "04": {"date": "April","days": 31},
    "05": {"date": "May","days": 31},
    "06": {"date": "June","days": 31},
    "07": {"date": "July","days": 31},
    "08": {"date": "August","days": 31},
    "09": {"date": "September","days": 31},
    "10": {"date": "October","days": 31},
    "11": {"date": "Novemeber","days": 31},
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
    
    try:
        if(len(month) == 2 and
         (len(date) == 2 and int(date) < months.get(month).get("days"))
          and len(year) == 4):
            convertedMonth = months.get(month).get("date")
            finalStr = f'{convertedMonth} {date}, {year}'
        else:
            raise SystemExit('invalid format')
    except(UnboundLocalError) as e:
        raise SystemExit('invalid format')

    return finalStr



date = input("Enter a date (mm/dd/yyyy): ")
convertedDate = converter(date)
print(f"the converted date is: {convertedDate}")
