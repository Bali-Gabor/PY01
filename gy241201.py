# Írj egy Python programot, amely a következőket végzi el:

# Kérd be a felhasználótól, hogy adjon meg egy számot 
# 𝑁
# N (1 ≤ N ≤ 100).
# Készíts egy listát, amely 1-től 
# 𝑁
# N-ig terjedő véletlenszámokat tartalmaz. (A véletlenszámok egész számok legyenek).
# A program számolja meg, hány páratlan szám van a listában, és hány olyan szám van, amely osztható 3-mal.
# A lista elemeit növekvő sorrendbe rendezd.
# Kérdezd meg a felhasználótól, hogy szeretne-e egy számot keresni a listában. Ha igen, akkor kérd be tőle a keresett számot, és jelezd, hogy megtaláltad-e azt a listában.
# Ha a keresett szám nem szerepel a listában, akkor add hozzá a listához és rendezd újra.

from random import randint

szamok=[]
N=int(input('Adj meg egy számot 1 és 100 között!  '))
for _ in range(N):
    szamok.append(randint(1,N))
paratlan=0
oszthato=0
for szam in szamok:
    if szam%2!=0: paratlan+=1
    if szam%3==0: oszthato+=1
szamok.sort()
print(szamok)
print(f'A listában {paratlan} páratlan és {oszthato} 3-mal osztható szám van.')
valasz=input('Szeretnél keresni egy számot a listában?  ')
if valasz in ['igen', 'Igen', 'Yes', 'yes', 'YES', 'IGEN']: 
    adat=int(input('Add meg azt a számot, amit keresel a listában!  '))
    if adat in szamok: print('A keresett szám benne van a listában.')
    else: 
        print('A keresett szám nem volt a listában, de hozzáadtam.')
        szamok.append(adat)
    szamok.sort()
    print(szamok)
else: print('Rendben, talán majd máskor.')



