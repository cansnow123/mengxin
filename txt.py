#!/usr/bin/env python
# coding=utf-8
# python 2.7
outfile = open('new.txt', 'w') #新的文件
list_1=[]
for line in open('test.txt'):  #老文件
    tmp = line.strip()
    if tmp not in list_1:
        list_1.append(tmp)
        outfile.write(line)
outfile.close()