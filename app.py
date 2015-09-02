#!/usr/bin/env python
# encoding: utf-8
#
# Author : Rahul Sharma
#

import requests
from lxml import html
from datetime import datetime


BASE_URL = "http://wbutech.net"
ODD_SEM = '/show-result_odd.php'
EVEN_SEM = '/show-result_even.php'

result_type = None

headers = {
        'Origin': 'http://wbutech.net',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'http://wbutech.net/result_even.php',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

def main():
    
    print(" A FASTER WAY TO GET WBUT RESULTS :D ")
    roll_no = int(raw_input("Enter the roll no (11 digits) : "))
    semester = int(raw_input("Enter Semester : "))
    result_type = ODD_SEM if(datetime.now().month<=6) else EVEN_SEM
    data = 'semno={0}&rectype=1&rollno={1}'.format(semester,roll_no)
    resource = requests.post(BASE_URL+result_type, headers=headers, data=data)
    tree = html.fromstring(resource.content)
    candidate = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[2]/th[1]/text()')
    SGPA = tree.xpath('//*[@id="lblContent"]/table[3]/tbody/tr[2]/td/text()')

    print(candidate)
    print(SGPA)

if __name__=='__main__':
    main()