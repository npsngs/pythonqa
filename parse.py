#!/usr/bin/python
# -*- coding: UTF-8 -*-
dictFile = open('中文字典.txt','r+')
outFile = open('chinesec.txt', 'w+') 
ifPause = True
while True:
	line = dictFile.readline()
	print line
	if ('' == line):
		break
	print ':',

	if not ifPause:
		continue

	cmd = raw_input()
	if 'n' == cmd:
		continue
	elif 'c' == cmd:
		ifPause = False
		continue


def parseDict(lineStr):


	



