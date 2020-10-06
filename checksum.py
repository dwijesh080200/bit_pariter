#!/usr/bin/env python3
v=input("Entrez un mot/string: ")
print("Lettre Valeur checksum1  checksum2")
check1=0
check2=0
for i in range(len(v)):   
    check1 = check1 + ord(v[i])
    check2 = check2 + check1
    print("   "+v[i]+"     "+str(ord(v[i]))+ "    "+str(check1)+"    "+str(check2) ) 
