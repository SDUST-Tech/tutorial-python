'''
__author__ = "sunmaoxiang"
task_1     = "ok"
'''

import re
import os
import sys
from urllib import request
from bs4 import BeautifulSoup

URL = "http://192.168.119.211/JudgeOnline/contestrank.php?cid=3476"
HOMEURL = "http://192.168.119.211/JudgeOnline/"

def download(csv_url):
    response = request.urlopen(csv_url)
    f = open('rank.csv', 'w')
    f.write(str(response.read(), "utf-8"))
    f.close()

def Crawer():
    resp = request.urlopen(URL).read().decode("utf-8")
    soup = BeautifulSoup(resp, "html.parser")
    csv_url = soup.find("a", href=re.compile("contestrank.csv.php.*"), text="Download")["href"]
    csv_url = HOMEURL + csv_url
    download(csv_url)

if __name__ == '__main__':
    Crawer()