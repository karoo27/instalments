def interestsact(capital, interestrate, noofdays):
    return round(capital * interestrate / 100 * noofdays / 365, 2)

def interests30(capital, interestrate):
    return round(capital * 30 / 360 * interestrate / 100, 2)