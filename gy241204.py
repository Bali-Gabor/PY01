# szoveg=input('Adj meg egy számsort ,-vel elválastva!  ')
# szamok=[]
# index=0
# seged1=0
# seged2=-1
# for x in szoveg:
#     if x==',':
#         seged1=seged2+1
#         seged2=index
#         szamok.append(int(szoveg[seged1:seged2]))  
#     if index==len(szoveg)-1:
#         seged1=seged2+1
#         szamok.append(int(szoveg[seged1:len(szoveg)]))
#     index+=1
# print(szamok)




"""Ez a program egy karaktersorozatból kiválogatja a számokat és float típusúként tárolja el egy listában. 
Erre azért van szükség, mert ha a szám nullával kezdődik, akkor már nem lehet integerré alakítani, 
vagy elveszik a nulla az elejéről."""

karaktersor=input('Adj meg egy karaktersort és kiválogatom belőle a számokat.  ')
szamok=[]
szam=''
referencia='0123456789'
for x in karaktersor:
    if x in referencia :
        szam=szam+x
    if (x not in referencia and szam!=''):
        if szam[0]=='0':
            szamok.append(int(szam)/10**(len(szam)-1))
            szam=''
        else:
            szamok.append(float(szam))
            szam=''
if szam!='':
    szamok.append(float(szam))
print(szamok)