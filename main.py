import datetime
import pyexcel as p
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
    rozklad = ins.instalments30(capital, nbrOfIns, interestRate, datetime.date.today())
elif typeOfIns==2:
     rozklad = ins.instalmentsACT(capital, nbrOfIns, interestRate, datetime.date.today())
else:
    print("Podałeś niepoprawny typ rozkładu odsetek!")

#print("Kapitał: ", capital, " Liczba rat:", nbrOfIns, " Stopa:", interestRate, "%")
for a in rozklad:
    print(a)

p.save_as(array=rozklad, dest_file_name='kap'+str(capital)+'_rat'+str(nbrOfIns)+'_stopa'+str(interestRate)+'.csv', dest_delimiter=";")

