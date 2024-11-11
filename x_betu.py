sor=0
veg=0
while sor<=4:
    darab=1
    while darab<=sor:
        print(" ",end="")
        darab+=1
    print("-",end="")
    sor+=1
    veg=9
    veg=veg-darab*2
    while veg>=1:
        print(" ",end="") 
        veg-=1
    if darab<=4:
        print("-")
    if sor==5:
        print("") 
        veg+=2
while sor<=8:
    darab=8-sor
    while darab>0:
        print(" ",end="")
        darab-=1
    print("-",end="")
    sor+=1
    a=1
    while a<=veg:
        print(" ",end="")
        a+=1
    veg+=2
    print("-")