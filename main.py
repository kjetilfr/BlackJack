import random


DAS = True
# DrawToSix = False
# StandOnSoft17 = False
# ResplitAces = False
# LateSurrender = False
# SplitTwiceOnly = False



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


def handIsPair(playerHand):
    if playerHand[0] == playerHand[1]:
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
        #Player card is 17 or above
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
        #Player card is 17 or above
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
        #Player card is 17 or above
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
        #Player card is 17 or above
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
        #Player card is 17 or above
        elif getHardTotal(playerHand) >= 17:
            return "Stand!"
    else:
        return "Unknown dealer card!"
    
    
def softHand(playerHand, dealerCard):
    # Dealer showing a 2
    if dealerCard == 2:
        #Player card is Ace + 2 to Ace + 6
        if getSoftTotal(playerHand) <= 17:
            return "Hit!"
        #Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 3
    elif dealerCard == 3:
        #Player card is Ace + 2 to Ace + 5
        if getSoftTotal(playerHand) <= 16:
            return "Hit!"
        #Player card is Ace + 6
        elif getSoftTotal(playerHand) == 17:
            return "Double!"
        #Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 4
    elif dealerCard == 4:
        #Player card is Ace + 2 or Ace + 3
        if getSoftTotal(playerHand) <= 14:
            return "Hit!"
        #Player card is Ace + 4 to Ace + 6
        elif 15 <= getSoftTotal(playerHand) == 17:
            return "Double!"
        #Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 5
    elif dealerCard == 5:
        #Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Double!"
        #Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand"
    # Dealer showing a 6
    elif dealerCard == 6:
        #Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Double!"
        #Player card is Ace + 7
        elif getSoftTotal(playerHand) == 18:
            return "Double! or Stand!"
        #Player card is Ace + 8
        elif getSoftTotal(playerHand) == 19:
            return "Double! or Stand!"
        #Player card is Ace + 8
        elif getSoftTotal(playerHand) >= 20:
            return "Stand!"
    # Dealer showing a 7
    elif dealerCard == 7:
        #Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Hit!"
        #Player card is Ace + 7 or above
        elif getSoftTotal(playerHand) >= 18:
            return "Stand!"
    # Dealer showing a 8
    elif dealerCard == 8:
        #Player card is Ace + 6 or below
        if getSoftTotal(playerHand) <= 17:
            return "Hit!"
        #Player card is Ace + 7 or above
        elif getSoftTotal(playerHand) >= 18:
            return "Stand!"
    # Dealer showing a 9
    elif dealerCard == 9:
        #Player card is Ace + 7 or below
        if getSoftTotal(playerHand) <= 18:
            return "Hit!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand!"
    # Dealer showing a 10
    elif dealerCard == 10:
        #Player card is Ace + 7 or below
        if getSoftTotal(playerHand) <= 18:
            return "Hit!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand!"
    # Dealer showing an Ace
    elif dealerCard == 11:
        #Player card is Ace + 7 or below
        if getSoftTotal(playerHand) <= 18:
            return "Hit!"
        #Player card is Ace + 8 or above
        elif getSoftTotal(playerHand) >= 19:
            return "Stand!"
    else:
        return "Unknown dealer card!"


def splitPairHand(playerHand, dealerCard):
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


def surrender(playerHand, dealerCard):
    if not handIsPair(playerHand):
        if (dealerCard == 9 or dealerCard == 10 or dealerCard == 11) and getHardTotal(playerHand) == 16:
            return True
        elif dealerCard == 10 and getHardTotal(playerHand) == 15:
            return True
        else:
            return False


def drawCard():
    # Draw new card
    return int(input("New Card: "))


def Start():
    global canDouble
    canDouble = True
    Card1 = int(input("Card 1: "))
    Card2 = int(input("Card 2: "))
    dealerCard = int(input("Dealer upcard: "))

    playerHand = [Card1, Card2]
    if playerHand[0] + playerHand[1] == 21:
        print("Blackjack!")
    elif surrender(playerHand, dealerCard):
        print("Surrender")
    elif handIsPair(playerHand):
        if splitPairHand(playerHand, dealerCard):
            print("Splitting Hand")
            playerHand1 = [playerHand[0]]
            print("Hand 1: ")
            playerHand1.append(drawCard())
            newCard(playerHand1, dealerCard)
            playerHand2 = [playerHand[1]]
            print("Hand 2: ")
            playerHand2.append(drawCard())
            newCard(playerHand2, dealerCard)
        else:
            pass
    elif handIsSoft(playerHand):
        newCard(playerHand, dealerCard)
    else:
        newCard(playerHand, dealerCard)


def newCard(playerHand, dealerCard):
    global canDouble
    # If hand is still soft
    if handIsSoft(playerHand):
        # Shorten to variable
        hand = softHand(playerHand, dealerCard)
        # If hitting and getting a new card
        if hand == "Hit!":
            canDouble = False
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(str(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double!" and canDouble == False:
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double! or Stand!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(str(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double! or Stand!" and canDouble == False:
            print("Stand")
            print(str(playerHand) + " vs " + str(dealerCard))
        elif hand == "Stand!":
            print("Stand")
            print(str(playerHand) + " vs " + str(dealerCard))
        else:
            print("UNKNOWN STUFF")
    else:
        # Shorten to variable
        hand = hardHand(playerHand, dealerCard)
        # If hitting and getting a new card
        if hand == "Hit!":
            canDouble = False
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(str(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double!" and canDouble == False:
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Stand!":
            print("Stand")
            print(str(playerHand) + " vs " + str(dealerCard))
        else:
            print("UNKNOWN STUFF")


Start()
