# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 19:26:43 2017

@author: scarl
"""

import requests
from lxml import objectify

period = 6
state_id = 44
divisions = 0
num_months = 8
year = 2016
template = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?parameter=tavg&state=%s&div=%s&month=%s&periods[]=%s&year=%s'
insert_these = (state_id, divisions, num_months, period, year)
template = template % insert_these


response = requests.get(template).content
root = objectify.fromstring(response)

my_wm_username = 'ydong03'
print my_wm_username

print 'value: ', root.data['value']
print 'twentiethCenturyMean: ', root.data['twentiethCenturyMean']
print 'lowRank: ', root.data['lowRank']
print 'highRank: ', root.data['highRank']