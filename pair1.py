#!/usr/bin/env python3

def pair(r):
	print("ascii code","","binary")
	for i in r:
		p = bin(i).strip('0b')
		print(i,"       ",p)
		if(p.count("1") % 2 == 0 ):
			u = "0" + p
			c = bytearray(u,'utf-8')
		else:
			u = "1" + p
			c = bytearray(u,'utf-8')
	print("")
	print(c)
q = input("entrer un mot/string: ")
r = bytearray(q,'utf-8')
pair(r)
