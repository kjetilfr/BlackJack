def getHardTotal(playerHand):
    hardTotal = 0
    for card in playerHand:
        if card == 11:
            hardTotal += 1
        else:
            hardTotal += card
    return hardTotal


def getSoftTotal(playerHand):
    softTotal = 0
    amountOfAces = 0
    for card in playerHand:
        if card == 11 and amountOfAces == 0:
            amountOfAces += 1
            softTotal += 11
        elif card == 11 and amountOfAces >= 1:
            amountOfAces += 1
            softTotal += 1
        else:
            softTotal += card
    return softTotal

def handIsSoft(playerHand):
    if 11 in playerHand and getSoftTotal(playerHand) <= 20:
        return True
    else:
        return False




print(handIsSoft([11, 9]))







hand = [5, 11, 11,11, 2]
#print(getSoftTotal(hand))
