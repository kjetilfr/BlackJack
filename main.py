import random


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
    if 11 in playerHand and getSoftTotal(playerHand) <= 21:
        return True
    else:
        return False


def hardHand(playerHand, dealerCard):
    # Dealer showing a 2
    if dealerCard == 2:
        #Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        #Player card is 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12
        elif 10 <= getHardTotal(playerHand) == 12:
            return "Hit!"
        #Player card is 13 or above
        elif 12 <= getHardTotal(playerHand) >= 13:
            return "Stand!"
        else:
            return "Unknown"
    # Dealer showing a 3
    elif dealerCard == 3:
        #Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12
        elif 10 <= getHardTotal(playerHand) == 12:
            return "Hit!"
        #Player card is 13 or above
        elif 12 <= getHardTotal(playerHand) >= 13:
            return "Stand!"
    # Dealer showing a 4
    elif dealerCard == 4:
        #Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12 or above
        elif 12 <= getHardTotal(playerHand) >= 12:
            return "Stand!"
    # Dealer showing a 5
    elif dealerCard == 5:
        #Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12 or above
        elif 12 <= getHardTotal(playerHand) >= 12:
            return "Stand!"
    # Dealer showing a 6
    elif dealerCard == 6:
        #Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12 or above
        elif 12 <= getHardTotal(playerHand) >= 12:
            return "Stand!"
    # Dealer showing a 7
    elif dealerCard == 7:
        #Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        #Player card is 17
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing a 8
    elif dealerCard == 8:
        #Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        #Player card is 17
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing a 9
    elif dealerCard == 9:
        #Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        #Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        #Player card is 17
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing a 10
    elif dealerCard == 10:
        #Player card is 10 or below
        if getHardTotal(playerHand) <= 10:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif getHardTotal(playerHand) == 11:
            return "Double!"
        #Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        #Player card is 17
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing an Ace
    elif dealerCard == 11:
        #Player card is 10 or below
        if getHardTotal(playerHand) <= 10:
            return "Hit!"
        #Player card is 9, 10 or 11
        elif getHardTotal(playerHand) == 11:
            return "Double!"
        #Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        #Player card is between 17 and 20
        elif 17 <= getHardTotal(playerHand) <= 20:
            return "Stand!"
        #Player card is 21
        elif getHardTotal(playerHand) == 21:
            return "Blackjack!"
    else:
        return "Unknown dealer card!"
    
    


# print(handIsSoft([11, 9]))

hand = [random.randint(2,11), random.randint(2,11)]
dealerCard = random.randint(2,11)


print(str(getHardTotal(hand)) + " " + str(dealerCard))
print(hardHand(hand, dealerCard))






#print(getSoftTotal(hand))
