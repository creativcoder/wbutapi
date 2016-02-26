#!/usr/bin/env python
# encoding: utf-8
# Author : Rahul Sharma

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

def show_grade_card(exam_info,candidate_name,candidate_roll,reg_detail,grade_table,summary):
    pretty_printed = """
-------------------------------------------------------------------------------------
{0} 
-------------------------------------------------------------------------------------
{1}                                {2}
-------------------------------------------------------------------------------------
{3}
-------------------------------------------------------------------------------------
    |                  |       |          |           |                |
        """.format(exam_info,candidate_name,candidate_roll,reg_detail)
    print(pretty_printed)

    # Todo : better formatting for result
    for k,i in enumerate(grade_table[0]):
        for j in i:
            print j.text_content(),
            
        print("")

    print("---------------------------------------------------------------------------------")

    for k,i in enumerate(summary[0]):
        for j in i:
            print j.text_content(),

        print("")

    return pretty_printed
        


def fetch(sem=None,roll=None):
    
    print(" A FASTER WAY TO GET WBUT RESULTS :D ")
    if sem is None and roll is None:
        roll_no = int(raw_input("Enter the roll no (11 digits) : "))
        semester = int(raw_input("Enter Semester : "))
    else:
        roll_no = roll
        semester = sem
    result_type = ODD_SEM if(semester%2 is not 0) else EVEN_SEM
    data = 'semno={0}&rectype=1&rollno={1}'.format(semester,roll_no)
    resource = requests.post(BASE_URL+result_type, headers=headers, data=data)
    tree = html.fromstring(resource.content)
    # exam_detail = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[1]/th/text()')
    # candidate = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[2]/th[1]/text()')
    for_exam = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[1]/th/text()')
    candidate_name = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[2]/th[1]/text()')
    candidate_roll = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[2]/th[2]/text()')
    reg_detail = tree.xpath('//*[@id="lblContent"]/table[1]/tbody/tr[3]/th/text()')
    grade_table = tree.xpath('//*[@id="lblContent"]/table[2]/tbody')
    summary = tree.xpath('//*[@id="lblContent"]/table[3]/tbody')

    return show_grade_card(
        for_exam[0].strip(),
        candidate_name[0].strip(),
        candidate_roll[0].strip(),
        reg_detail[0].strip(),
        grade_table,
        summary
        )

if __name__=='__main__':
    fetch()