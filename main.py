import datetime
import instalments as ins


print('Podaj wartość kapitału do spłaty:')
capital = int(input())
print('Podaj liczbę rat:')
nbrOfIns = int(input())
print('Podaj wysokość stopy w %:')
interestRate = int(input())
print('Wpisz 1,by liczyć odsetki metodą 30/360, wpisz 2, by liczyć odsetki metodą ACT/365')
typeOfIns=int(input())

if typeOfIns==1:
    test = ins.instalments30(capital, nbrOfIns, interestRate, datetime.date.today())
elif typeOfIns==2:
     test = ins.instalmentsACT(capital, nbrOfIns, interestRate, datetime.date.today())
else:
    print("Podałeś niepoprawny typ rozkładu odsetek!")

#print("Kapitał: ", capital, " Liczba rat:", nbrOfIns, " Stopa:", interestRate, "%")
for a in test:
    print(a)


