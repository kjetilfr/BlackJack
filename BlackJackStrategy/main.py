from pairHand import splitPairHand
from hardHand import hardHand, getHardTotal
from softHand import softHand, getSoftTotal

global DAS, Resplit
DAS = True
Resplit = True
# DrawToSix = False
# StandOnSoft17 = False
# ResplitAces = False
# LateSurrender = False
# SplitTwiceOnly = False


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
        if splitPairHand(playerHand, dealerCard, DAS):
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
            print("UNKNOWN STUFF 1")
    elif handIsPair(playerHand):
        splitPairHand(playerHand, dealerCard, DAS)
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
            print("UNKNOWN STUFF 2")


Start()
