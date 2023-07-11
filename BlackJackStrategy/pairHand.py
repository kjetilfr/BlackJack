def splitPairHand(playerHand, dealerCard, DAS = True):
    #Dealer showing a 2
    if dealerCard == 2:
        #Player card is 2 + 2 or 3 + 3
        if 2 <= playerHand[0] <= 3:
            if DAS:
                return True
            else:
                return False
        #Player card is 4 + 4 or 5 + 5
        elif 4 <= playerHand[0] <= 5:
            return False
        #Player card is 6 + 6
        elif playerHand[0] <= 6:
            if DAS:
                return True
            else:
                return False
        #Player card is 7 + 7 to 9 + 9
        elif 7 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 3
    elif dealerCard == 3:
        #Player card is 2 + 2 or 3 + 3
        if 2 <= playerHand[0] <= 3:
            if DAS:
                return True
            else:
                return False
        #Player card is 4 + 4 or 5 + 5
        elif 4 <= playerHand[0] <= 5:
            return False
        #Player card is 6 + 6 to 9 + 9
        elif 6 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 4
    elif dealerCard == 4:
        #Player card is 2 + 2 or 3 + 3
        if 2 <= playerHand[0] <= 3:
            return True
        #Player card is 4 + 4 or 5 + 5
        elif 4 <= playerHand[0] <= 5:
            return False
        #Player card is 6 + 6 to 9 + 9
        elif 6 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 5
    elif dealerCard == 5:
        #Player card is 2 + 2 or 3 + 3
        if 2 <= playerHand[0] <= 3:
            return True
        #Player card is 4 + 4
        elif playerHand[0] == 4:
            if DAS:
                return True
            else:
                return False
        #Player card is 5 + 5
        elif playerHand[0] == 5:
            return False
        #Player card is 6 + 6 to 9 + 9
        elif 6 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 6
    elif dealerCard == 6:
        #Player card is 2 + 2 or 3 + 3
        if 2 <= playerHand[0] <= 3:
            return True
        #Player card is 4 + 4
        elif playerHand[0] == 4:
            if DAS:
                return True
            else:
                return False
        #Player card is 5 + 5
        elif playerHand[0] == 5:
            return False
        #Player card is 6 + 6 to 9 + 9
        elif 6 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 7
    elif dealerCard == 7:
        #Player card is 2 + 2 or 3 + 3
        if 2 <= playerHand[0] <= 3:
            return True
        #Player card is 4 + 4, 5 + 5 or 6 + 6
        elif 4 <= playerHand[0] <= 6:
            return False
        #Player card is 7 + 7 or 8 + 8
        elif 7 <= playerHand[0] <= 8:
            return True
        #Player card is 9 + 9 or 10 + 10
        elif 9 <= playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 8
    elif dealerCard == 8:
        #Player card is 7 + 7 or below
        if playerHand[0] <= 7:
            return False
        #Player card is 8 + 8 or 9 + 9
        elif 8 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 9
    elif dealerCard == 9:
        #Player card is 7 + 7 or below
        if playerHand[0] <= 7:
            return False
        #Player card is 8 + 8 or 9 + 9
        elif 8 <= playerHand[0] <= 9:
            return True
        #Player card is 10 + 10
        elif playerHand[0] == 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing a 10
    elif dealerCard == 10:
        #Player card is 7 + 7 or below
        if playerHand[0] <= 7:
            return False
        #Player card is 8 + 8
        elif playerHand[0] == 8:
            return True
        #Player card is 9 + 9 or 10 + 10
        elif 9 <= playerHand[0] <= 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    #Dealer showing an Ace
    elif dealerCard == 11:
        #Player card is 7 + 7 or below
        if playerHand[0] <= 7:
            return False
        #Player card is 8 + 8
        elif playerHand[0] == 8:
            return True
        #Player card is 9 + 9 or 10 + 10
        elif 9 <= playerHand[0] <= 10:
            return False
        #Player card is Ace + Ace
        elif playerHand[0] == 11:
            return True
    else:
        return "Unknown dealer card!"
