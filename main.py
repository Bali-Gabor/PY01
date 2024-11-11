nev=input('Szia, hogy hívnak?: ')
print(f'Hello {nev}! ')
print(f'Milyen szép név az, hogy {nev}!')
valasz=input(f'Szeretsz programozni {nev}?:')
if valasz=='igen':
    print('Akkor még sokra viheted itt! :)')
else:
    print('Nem baj, majd megszereted!')
szam=int(input('Hányszor írjam ki a neved?:'))
for x in range(szam):
    print(nev)