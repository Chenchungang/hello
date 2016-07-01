#!/usr/bin/env python3
height = 1.75
weight = 80.5

bim = weight/(height**2)
#print (bmi)
if bim < 18.5 :
    print("过轻")
elif bim > 18.5 and bim < 25 :
    print("正常")
elif bim > 25 and bim < 28 :
    print("过重")
elif bim > 28 and bim < 32 :
    print("肥胖")
elif bim > 32 :
    print("严重肥胖") 
