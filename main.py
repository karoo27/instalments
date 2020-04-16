import datetime
from dateutil.relativedelta import relativedelta
import install as ins


def rozkladNaRaty30(capital, liczbaRat, interestrate):
    x = [['Rata', 'Kapital', 'Odsetki', 'RPB']]
    rataKapitalowa = round((capital / liczbaRat), 2)
    ostatniaRata = round(capital - rataKapitalowa * (liczbaRat - 1), 2)

    for i in range(liczbaRat):
        if i == liczbaRat - 1:
            x.append([liczbaRat, ostatniaRata, ins.interests30(ostatniaRata, interestrate), 0])
        else:
            x.append([i + 1, rataKapitalowa, ins.interests30(capital - rataKapitalowa * i, interestrate),
                      round(capital - rataKapitalowa * (i + 1), 2)])
    return x


def rozkladNaRatyReal(capital, liczbaRat, interestrate, start):
    x = [['Rata', 'Data', 'Kapital', 'Odsetki', 'RPB']]
    rataKapitalowa = round((capital / liczbaRat), 2)
    ostatniaRata = round(capital - rataKapitalowa * (liczbaRat - 1), 2)
    dataPoprzRaty = start

    for i in range(liczbaRat):
        dataObecRaty = dataPoprzRaty + relativedelta(months=1)
        if i == liczbaRat - 1:
            x.append([liczbaRat, str(dataObecRaty), ostatniaRata,
                      ins.interestsact(ostatniaRata, interestrate, dataPoprzRaty, dataObecRaty), 0])
        else:
            x.append([i + 1, str(dataObecRaty), rataKapitalowa,
                      ins.interestsact(capital - rataKapitalowa * i, interestrate, dataPoprzRaty, dataObecRaty),
                      round(capital - rataKapitalowa * (i + 1), 2)])
        dataPoprzRaty = dataObecRaty
    return x


capital = 10000
liczbaRat = 24
interestrate = 2

test = rozkladNaRaty30(capital, liczbaRat, interestrate)
test2 = rozkladNaRatyReal(capital, liczbaRat, interestrate, datetime.date.today())

print("Kapitał: ", capital, " Liczba rat:", liczbaRat, " Stopa:", interestrate, "%")

print("Rozkład dla odsetek 30/360:")
for a in test:
    print(a)

print("Rozkład dla odsetek ACT/365:")
for a in test2:
    print(a)

