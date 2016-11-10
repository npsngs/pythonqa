#!/usr/bin/python
# -*- coding: UTF-8 -*-
dictFile = open('中文字典.txt','r+')
outFile = open('chinesec.txt', 'w+') 
ifPause = True
lineOut = u''

def onBegin(lineOut):
	global outFile
	if len(lineOut) > 0:
		lineOut +='\n'
		#print lineOut
		outFile.write(lineOut.encode('utf-8'))
		lineOut = u''




def parseDict(lineStr):
	global lineOut
	if lineStr.startswith('*'):
		onBegin(lineOut)
		lineOut = lineStr[1:2] + '\t'
		idx = lineStr.find(',')
		if idx >= 0:
			lineOut += lineStr[2:idx]







while True:
	line = dictFile.readline()
	line = line.decode('utf-8')
	print line
	if ifPause:
		print ':',

	if ('' == line):
		break
	else:
		parseDict(line)
	
	if not ifPause:
		continue

	cmd = raw_input()
	if 'n' == cmd:
		continue
	elif 'c' == cmd:
		ifPause = False
		continue

outFile.flush()	



