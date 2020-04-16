def interestsact(capital, interestrate, poprzedniaRata, obecnaRata):
    noofdays = obecnaRata - poprzedniaRata
    return round(capital * interestrate / 100 * noofdays.days / 365, 2)

def interests30(capital, interestrate):
    return round(capital * 30 / 360 * interestrate / 100, 2)