# import os.path
# num=1
# def traverse_directory(name):
#     for filename in traverse_directory(name):
#         pathname = os.path.join(name,filename)
#         if (os.path.isfile(filename)):
#             print pathname
#             num++
#             traverse_directory(pathname)
# name = "/home/du/1"
# traverse_directory(name)
# print(num)
import os
num=1
def traverse_directory(name):
	# root遍历的文件夹,dirs遍历的文件夹下的所有文件夹
	# files遍历的文件夹下的所有文件
    for root,dirs,files in os.walk(name):
        for filename in files:
            print(os.path.join(root,filename))
            num++
            for dir in dirs:
                traverse_directory(dir)
name = "/home/du/1"
traverse_directory(name)
print(num)