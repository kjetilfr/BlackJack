def handIsSoft(playerHand):
    if 11 in playerHand and getSoftTotal(playerHand) <= 21:
        return True
    else:
        return False


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


def softHand(playerHand, dealerCard):
    # Dealer showing a 2
    if dealerCard == 2:
        # Player card is Ace + 2 to Ace + 6
        if getSoftTotal(playerHand) <= 17:
            return "Hit!"
        # Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 3
    elif dealerCard == 3:
        # Player card is Ace + 2 to Ace + 5
        if getSoftTotal(playerHand) <= 16:
            return "Hit!"
        # Player card is Ace + 6
        elif getSoftTotal(playerHand) == 17:
            return "Double!"
        # Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 4
    elif dealerCard == 4:
        # Player card is Ace + 2 or Ace + 3
        if getSoftTotal(playerHand) <= 14:
            return "Hit!"
        # Player card is Ace + 4 to Ace + 6
        elif 15 <= getSoftTotal(playerHand) == 17:
            return "Double!"
        # Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 5
    elif dealerCard == 5:
        # Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Double!"
        # Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 6
    elif dealerCard == 6:
        # Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Double!"
        # Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        # Player card is Ace + 8
        elif getSoftTotal(playerHand) == 19:
            return "Double! or Stand!"
        # Player card is Ace + 8
        elif getSoftTotal(playerHand) >= 20:
            return "Stand!"
    # Dealer showing a 7
    elif dealerCard == 7:
        # Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Hit!"
        # Player card is Ace + 7 or above
        elif getSoftTotal(playerHand) >= 18:
            return "Stand!"
    # Dealer showing an 8
    elif dealerCard == 8:
        # Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Hit!"
        # Player card is Ace + 7 or above
        elif getSoftTotal(playerHand) >= 18:
            return "Stand!"
    # Dealer showing a 9
    elif dealerCard == 9:
        # Player card is Ace + 7 or below
        if getSoftTotal(playerHand) <= 18:
            return "Hit!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand!"
    # Dealer showing a 10
    elif dealerCard == 10:
        # Player card is Ace + 7 or below
        if getSoftTotal(playerHand) <= 18:
            return "Hit!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand!"
    # Dealer showing an Ace
    elif dealerCard == 11:
        # Player card is Ace + 7 or below
        if getSoftTotal(playerHand) <= 18:
            return "Hit!"
        # Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand!"
    else:
        return "Unknown dealer card!"