import os
import sys

def dfs_print(path, depth):
    dirnames = os.listdir
    for item in os.listdir(path):
        newpath = path + '/' + item
        if os.path.isdir(newpath):
            print('-' * (depth * 2) + ' ' + item)
            dfs_print(newpath, depth + 1)
    for item in os.listdir(path):
        newpath = path + '/' + item
        if os.path.isfile(newpath):
            print('-' * (depth * 2) + ' ' + item)
    
def traverse_directory(name):
    filecnt = 0
    try:
        for dirpath, dirnames, filenames in os.walk(name):
            filecnt += len(filenames)
        dfs_print(name, 1)
    except Exception as e:
        print("Not Exist!")
        return
    print("\n文件数 %d\n===========================" % filecnt)

if __name__ == '__main__':
    print("===========================")
    for i in sys.argv[1:]:
        print("文件夹名：", i) 
        traverse_directory(i)
