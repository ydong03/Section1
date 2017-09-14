# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 21:46:38 2017

@author: scarl
"""

import requests
from bs4 import BeautifulSoup as bsoup
    
my_wm_username = 'ydong03'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

parsed_html = bsoup(response.content, "lxml")

target_rows = parsed_html.find_all('tr') 

all_data = []
for row in target_rows:
    new_row = []
    for x in row.find_all('td'):
        s = x.text.encode("ascii",'ignore')
        new_row.append(s)  
    all_data.append(new_row)
    
print my_wm_username
print 'Number of rows:', len(all_data)
print all_data
