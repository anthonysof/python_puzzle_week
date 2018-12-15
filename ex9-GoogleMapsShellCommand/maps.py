#!/usr/bin/env python3
import sys, webbrowser
if len(sys.argv) > 1:
	map_string = ' '.join(sys.argv[1:])
	start = str(input("Give me starting point: "))
	webbrowser.open('https://www.google.com/maps/dir/' + start + '/' + map_string)
	
else:
	print("<usage: getdirs [address]>")