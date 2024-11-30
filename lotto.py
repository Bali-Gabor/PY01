from random import randint

print('LOTTÓSORSOLÁS')
valasz=int(input('Milyen lottót szeretnél játszani [ 5; 6; 7 ]?  '))
while valasz not in [5, 6, 7]:
    valasz=int(input('Nem jól adtad meg a választásod! Csak  ezekből válaszhatsz [ 5; 6; 7 ]!  '))
max=0
tipp=[]
match valasz:
    case 5: 
        max=90
        print('90/5-ös lottó')
    case 6: 
        max=45
        print('45/6-os lottó')
    case 7: 
        max=35 
        print('Skandináv lottó')
print('Most töltsd ki a szelvényt!')
while len(tipp)<valasz:
    szam=int(input(f'Add meg az {len(tipp)+1}. számot!  '))
    if szam<1 or szam>max: print(f'Csak 1 és {max} közötti számot lehet megadni!')
    elif szam in tipp: print('A számot már megjelölted, válassz másikat!')
    else: tipp.append(szam)
print(f'A megadott számaid: {sorted(tipp)}')
sorsolas=[]
while len(sorsolas)<valasz:
    gep=randint(1,max)
    if gep not in sorsolas: sorsolas.append(gep)
print(f'A kisorsolt számok: {sorted(sorsolas)}')
darab=0
for x in sorsolas:
    if x in tipp: darab+=1
print(f'{darab} találatod van.')
if darab >= valasz-3: print('NYERTÉL!!!')
else: print('Sajnos nem nyertél.')