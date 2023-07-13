from pairHand import handIsPair
from hardHand import getHardTotal


def surrender(playerHand, dealerCard, S17, typeSurrender="Late Surrender"):
    if not handIsPair(playerHand):
        if (dealerCard == 9 or dealerCard == 10 or dealerCard == 11) and getHardTotal(playerHand) == 16:
            return True
        elif dealerCard == 10 and getHardTotal(playerHand) == 15:
            return True
        elif dealerCard == 11 and getHardTotal(playerHand) == 17 and not S17:
            return True
        else:
            return False
