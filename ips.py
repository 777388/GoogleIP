import sys

i = sys.argv[1]
x = 256
for v in range(0, x, 10):
    print("site:***"+str(v)+" | site:***"+str(v+1)+" | site:***"+str(v+2)+" | site:***"+str(v+3)+" | site:***"+str(v+4)+" | site:***"+str(v+5)+" | site:***"+str(v+6)+" | site:***"+str(v+7)+" | site:***"+str(v+8)+" | site:***"+str(v+9)+" | site:***"+str(v+10)+" & intext:\""+i+"\" ")
    print()
