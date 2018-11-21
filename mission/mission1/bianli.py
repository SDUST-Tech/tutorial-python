#!/usr/bin/python
# coding:gbk

import os
def traverse_directory(name):
    name=os.getcwd()
    #name="Lib"
    if not os.path.exists(name):
        print("Not Exist!")
        return
    else:
        count=0
        for root, dirs, files in os.walk(name):
            for each in files:
                count =count + 1
            print("--",root)
            if(dirs):
                print("----",dirs)
            if(files):
                 print("------",files)
            print(count)
if  __name__ == "__main__":
    traverse_directory(".")
