sor=1
a=0
b=10
while sor<=5:
    darab=0
    while darab<=10:
        if a==darab:
            print("O",end="")
        elif b==darab:
            print("O",end="")
        else:
            print("-",end="")
        darab+=1
    a+=1
    b-=1
    sor+=1
    print("")
while sor>=5 and sor<=11:
    darab=0
    while darab<=10:
        if a==darab:
            print("O",end="")
        elif b==darab:
            print("O",end="")
        else:
            print("-",end="")
        darab+=1
    a-=1
    b+=1
    sor+=1
    print("")