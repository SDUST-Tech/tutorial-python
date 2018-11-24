'''
__author__ = "sunmaoxiang"
task_1     = "ok"
task_2     = "ok"
'''

import re
import os
import csv
import sys
from urllib import request
from bs4 import BeautifulSoup

rankurl = "http://192.168.119.211/JudgeOnline/contestrank.php?cid="
HOMEURL = "http://192.168.119.211/JudgeOnline/"

def download(csv_url, times):
    response = request.urlopen(csv_url)
    f = open('RankList-' + times + '.csv', 'w')
    f.write(str(response.read(), "utf-8"))
    f.close()

def Crawer(URL, times):
    resp = request.urlopen(URL).read().decode("utf-8")
    soup = BeautifulSoup(resp, "html.parser")
    csv_url = soup.find("a", href=re.compile("contestrank.csv.php.*"), text="Download")["href"]
    csv_url = HOMEURL + csv_url
    download(csv_url, times)
    print("over!")

def GetRankList():
    resp = request.urlopen("http://192.168.119.211/JudgeOnline/contest.php").read().decode("utf-8")
    soup = BeautifulSoup(resp, "html.parser")
    allurl = soup.findAll("a", href=re.compile("contest.*"), text=re.compile("软件工程.*实验.*"))
    for url in allurl[::-1]:
        print(u"正在下载<" + url.string + u">成绩单")
        Crawer(rankurl + str(url["href"]).split("cid=")[1], str(url.string).split(u"——实验")[1])
    print(u"所有软件工程实验成绩单下载完毕~")

def Statistics():
    student = {}
    print(u"正在统计......")
    path_list = os.listdir(".")
    cnt = 0
    for filename in path_list:
        if os.path.splitext(filename)[1] == ".csv":
            cnt += 1
            f = open(filename, 'r')
            csv_keyword = csv.reader(f)
            for row in csv_keyword:
                try:
                    if(row[0] == 'Rank'):
                       continue
                    elif row[1] not in student:
                        student.update({row[1] : {'name' : row[2], 'Mark' : [row[4], ]}})
                    else:
                        student[row[1]]['Mark'].append(row[4])
                except IndexError as e:
                    continue
            for (k, v) in student.items():
                if len(v['Mark']) != cnt:
                    v['Mark'].append('0000')
            f.close()
    f = open("statistics.csv", "w+")
    f.write("User,Nick")
    for i in range(0, len(student['201701100121']['Mark'])):
        f.write(",Mark-" + str(i+1))
    f.write('\n')
    for (k, v) in student.items():
        f.write(k + "," + v['name'])
        for mark in v['Mark']:
            f.write(',' + mark)
        f.write('\n')
    f.close()

if __name__ == '__main__':
    GetRankList()
    Statistics()