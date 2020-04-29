from dateutil.relativedelta import relativedelta

def interestsact(capital, interestRate, nbrOfDays):
    return round(capital * interestRate / 100 * nbrOfDays / 365, 2)

def interests30(capital, interestRate):
    return round(capital * 30 / 360 * interestRate / 100, 2)

def instalments30(capital, nbrOfIns, interestRate, startDate):
    x = [['Rata', 'Data','Kapital', 'Odsetki', 'Kwota raty', 'RPB']]
    capitalIns = round((capital / nbrOfIns), 2)
    lastIns= round(capital - capitalIns * (nbrOfIns - 1), 2)

    for i in range(nbrOfIns):
        dateOfIns = startDate + relativedelta(months=i + 1)
        if i == nbrOfIns - 1:
            interests=interests30(lastIns, interestRate)
            x.append([nbrOfIns, str(dateOfIns), lastIns, interests, round(lastIns+interests,2), 0])
        else:
            interests=interests30(capital - capitalIns * i, interestRate)
            x.append([i + 1, str(dateOfIns),  capitalIns, interests, round(capitalIns+interests,2),
                      round(capital - capitalIns * (i + 1), 2)])
    return x


def instalmentsACT(capital, nbrOfIns, interestRate, startDate):
    x = [['Rata', 'Data', 'Kapital', 'Odsetki', 'Kwota raty', 'RPB']]
    capitalIns = round((capital / nbrOfIns), 2)
    lastIns = round(capital - capitalIns * (nbrOfIns - 1), 2)
    prevDate = startDate

    for i in range(nbrOfIns):
        dateOfIns = startDate + relativedelta(months=i+1)
        if i == nbrOfIns - 1:
            interests= interestsact(lastIns, interestRate, (dateOfIns-prevDate).days)
            x.append([nbrOfIns, str(dateOfIns), lastIns, interests, round(lastIns+interests,2), 0])
        else:
            interests=interestsact(capital - capitalIns * i, interestRate, (dateOfIns-prevDate).days)
            x.append([i + 1, str(dateOfIns), capitalIns, interests, round(capitalIns+interests,2),
                      round(capital - capitalIns * (i + 1), 2)])
        prevDate = dateOfIns
    return x