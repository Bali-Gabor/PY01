sor=0
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
    