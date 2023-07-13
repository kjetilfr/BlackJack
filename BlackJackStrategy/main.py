from pairHand import handIsPair, splitPairHand
from hardHand import hardHand, getHardTotal
from softHand import handIsSoft, softHand, getSoftTotal
from count import count, getTrueCount
from deviation import deviation, insurance
from surrender import surrender

global DAS, Resplit, DrawToSix, StandOnSoft17, ResplitAces, LateSurrender, AceSplitOnlyDraw1

DAS = True
Resplit = True
S17 = False
canSurrender = True
typeSurrender = "Late Surrender"

# DrawToSix = False
# ResplitAces = False
# SplitTwiceOnly = False


def drawCard():
    # Draw new card
    newCard = int(input("New Card: "))
    count(newCard)
    return newCard


def Start():
    global canDouble
    canDouble = True
    Card1 = int(input("Card 1: "))
    Card2 = int(input("Card 2: "))
    dealerCard = int(input("Dealer upcard: "))
    playerHand = [Card1, Card2]

    for card in playerHand:
        count(card)
    count(dealerCard)
    
    # Insurance?
    if dealerCard == 11:
        if insurance():
            print("Take Insurance")
        else:
            print("Don't take Insurance")

    if playerHand[0] + playerHand[1] == 21:
        print("Blackjack!")
    elif canSurrender and surrender(playerHand, dealerCard, S17, typeSurrender):
        print("Surrender")
    elif deviation(playerHand, dealerCard, S17)[0]:
        print(deviation(playerHand, dealerCard)[0])
        newCard(playerHand, dealerCard)
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
            print("Not Splitting Hand")
            newCard(playerHand, dealerCard)
    elif handIsSoft(playerHand):
        newCard(playerHand, dealerCard)
    else:
        newCard(playerHand, dealerCard)


def newCard(playerHand, dealerCard):
    global canDouble
    if deviation(playerHand, dealerCard, S17)[0]:
        #If deviation
        print("DEVIATION")
        print("Hand: " + str(playerHand[0]) + " " + str(playerHand[1]) + " True Count: " + str(getTrueCount()))
        # Shorten to variable
        hand = deviation(playerHand, dealerCard)[1]
        #if hitting and getting a new card
        if hand == "Hit!":
            canDouble = False
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double!" and canDouble == False:
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double! or Stand!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double! or Stand!" and canDouble == False:
            print("Stand")
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double! or Hit!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double! or Hit!" and canDouble == False:
            print("Hit")
            playerHand.append(drawCard())
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Stand!":
            print("Stand")
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Split!":
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
            print("UNKNOWN STUFF 0")
    # If hand is still soft
    elif handIsSoft(playerHand):
        # Shorten to variable
        hand = softHand(playerHand, dealerCard, S17)
        # If hitting and getting a new card
        if hand == "Hit!":
            canDouble = False
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double!" and canDouble == False:
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Double! or Stand!" and canDouble == True:
            print("Double")
            playerHand.append(drawCard())
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double! or Stand!" and canDouble == False:
            print("Stand")
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Stand!":
            print("Stand")
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        else:
            print("UNKNOWN STUFF 1")
            print(playerHand)
            print(getSoftTotal(playerHand))
    elif handIsPair(playerHand) and splitPairHand(playerHand, dealerCard, DAS):
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
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        elif hand == "Double!" and canDouble == False:
            print("Hit")
            playerHand.append(drawCard())
            newCard(playerHand, dealerCard)
        elif hand == "Stand!":
            print("Stand")
            print(finishedPrint(playerHand) + " vs " + str(dealerCard))
        else:
            print("UNKNOWN STUFF 2")


def finishedPrint(playerHand):
    if handIsSoft(playerHand):
        return "Soft " + str(getSoftTotal(playerHand))
    else:
        return "Hard " + str(getHardTotal(playerHand))

Start()
