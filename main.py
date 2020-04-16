import datetime
from dateutil.relativedelta import relativedelta
import interests as ins


def instalments30(capital, noofins, interestrate, startdate):
    x = [['Rata', 'Data','Kapital', 'Odsetki', 'Kwota raty', 'RPB']]
    capitalins = round((capital / noofins), 2)
    lastins= round(capital - capitalins * (noofins - 1), 2)

    for i in range(noofins):
        dateofins = startdate + relativedelta(months=i + 1)
        if i == noofins - 1:
            interests=ins.interests30(lastins, interestrate)
            x.append([noofins, str(dateofins), lastins, interests, round(lastins+interests,2), 0])
        else:
            interests=ins.interests30(capital - capitalins * i, interestrate)
            x.append([i + 1, str(dateofins),  capitalins, interests, round(capitalins+interests,2),
                      round(capital - capitalins * (i + 1), 2)])
    return x


def instalmentsACT(capital, noofins, interestrate, startdate):
    x = [['Rata', 'Data', 'Kapital', 'Odsetki', 'Kwota raty', 'RPB']]
    capitalins = round((capital / noofins), 2)
    lastins = round(capital - capitalins * (noofins - 1), 2)
    prevdate = startdate

    for i in range(noofins):
        dateofins = startdate + relativedelta(months=i+1)
        if i == noofins - 1:
            interests= ins.interestsact(lastins, interestrate, (dateofins-prevdate).days)
            x.append([noofins, str(dateofins), lastins, interests, round(lastins+interests,2), 0])
        else:
            interests=ins.interestsact(capital - capitalins * i, interestrate, (dateofins-prevdate).days)
            x.append([i + 1, str(dateofins), capitalins, interests, round(capitalins+interests,2),
                      round(capital - capitalins * (i + 1), 2)])
        prevdate = dateofins
    return x

print('Podaj wartość kapitału do spłaty:')
capital = int(input())
print('Podaj liczbę rat:')
noofins = int(input())
print('Podaj wysokość stopy w %:')
interestrate = int(input())

test = instalments30(capital, noofins, interestrate, datetime.date.today())
test2 = instalmentsACT(capital, noofins, interestrate, datetime.date.today())

print("Kapitał: ", capital, " Liczba rat:", noofins, " Stopa:", interestrate, "%")

print("Rozkład dla odsetek 30/360:")
for a in test:
    print(a)

print("Rozkład dla odsetek ACT/365:")
for a in test2:
    print(a)

