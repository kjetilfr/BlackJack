def getHardTotal(playerHand):
    hardTotal = 0
    for card in playerHand:
        if card == 11:
            hardTotal += 1
        else:
            hardTotal += card
    return hardTotal


def hardHand(playerHand, dealerCard, S17=False):
    # Dealer showing a 2
    if dealerCard == 2:
        # Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        # Player card is 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12
        elif 10 <= getHardTotal(playerHand) <= 12:
            return "Hit!"
        # Player card is 13 or above
        elif 12 <= getHardTotal(playerHand) >= 13:
            return "Stand!"
        else:
            return "Unknown"
    # Dealer showing a 3
    elif dealerCard == 3:
        # Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12
        elif 10 <= getHardTotal(playerHand) <= 12:
            return "Hit!"
        # Player card is 13 or above
        elif 12 <= getHardTotal(playerHand) >= 13:
            return "Stand!"
    # Dealer showing a 4
    elif dealerCard == 4:
        # Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12 or above
        elif 12 <= getHardTotal(playerHand) >= 12:
            return "Stand!"
    # Dealer showing a 5
    elif dealerCard == 5:
        # Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12 or above
        elif 12 <= getHardTotal(playerHand) >= 12:
            return "Stand!"
    # Dealer showing a 6
    elif dealerCard == 6:
        # Player card is 8 or below
        if getHardTotal(playerHand) <= 8:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 9 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12 or above
        elif 12 <= getHardTotal(playerHand) >= 12:
            return "Stand!"
    # Dealer showing a 7
    elif dealerCard == 7:
        # Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        # Player card is 17 or above
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing a 8
    elif dealerCard == 8:
        # Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        # Player card is 17 or above
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing a 9
    elif dealerCard == 9:
        # Player card is 9 or below
        if getHardTotal(playerHand) <= 9:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif 10 <= getHardTotal(playerHand) <= 11:
            return "Double!"
        # Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        # Player card is 17 or above
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing a 10
    elif dealerCard == 10:
        # Player card is 10 or below
        if getHardTotal(playerHand) <= 10:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif getHardTotal(playerHand) == 11:
            return "Double!"
        # Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        # Player card is 17 or above
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    # Dealer showing an Ace
    elif dealerCard == 11:
        # Player card is 10 or below
        if getHardTotal(playerHand) <= 10:
            return "Hit!"
        # Player card is 9, 10 or 11
        elif getHardTotal(playerHand) == 11:
            if S17:
                return "Hit!"
            else:
                return "Double!"
        # Player card is 12 to 16
        elif 12 <= getHardTotal(playerHand) <= 16:
            return "Hit!"
        # Player card is 17 or above
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    else:
        return "Unknown dealer card!"