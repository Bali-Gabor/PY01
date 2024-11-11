sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        osszeg=oszlop+sor
        if osszeg==6:
            print("O ",end="")
        elif sor==2 and osszeg==8 or sor==3 and osszeg==10 or sor==4 and osszeg==12:
            print("O ",end="")
        elif oszlop==1 and sor>5:
            print("O ",end="")
        elif oszlop==9 and sor>5:
            print("O ",end="")
        elif sor==5 and oszlop<10:
            print("O ",end="")
        elif sor==10 and oszlop<10:
            print("O ",end="")
        else:
            print("  ",end="")
        oszlop+=1
    print("")
    sor+=1
