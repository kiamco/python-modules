#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import URLError

import re
from datetime import date


KEYWORDS = ["research", "climate", "evolution", "cultural",
            "leadership", "nation", "physical", 'science', 
            "biological", "engineering"]

def get_page():

    page_view =""

    try:
        to_read = urlopen('http://www.nasonline.org/')
        if(to_read != None):
            html = to_read.read()
            page_view = html.decode()
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)

    return page_view


def parse_page(page):
    key_count = {}

    if(page != None):
        for i in KEYWORDS:
            regex = re.compile(i, re.IGNORECASE);
            match = regex.findall(page)
            key_count[i] = len(match)

    return key_count

if __name__ == "__main__":
    print(f'Todays date is: {date.today()}')
    page = get_page()
    count_by_key = parse_page(page)

    for key in count_by_key:
        print(f'\"{key}\" apears {count_by_key[key]} times')



"""---------------------- run ---------------------------
Todays date is: 2020-02-15
"research" apears 10 times
"climate" apears 5 times
"evolution" apears 5 times
"cultural" apears 8 times
"leadership" apears 4 times
"nation" apears 37 times
"physical" apears 1 times
"science" apears 55 times
"biological" apears 1 times
"engineering" apears 5 times
"""