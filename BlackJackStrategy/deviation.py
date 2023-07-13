from saveLoad import readCount, readRules
from hardHand import getHardTotal
from pairHand import *
from softHand import *
from count import getTrueCount


def deviation(playerHand, dealerCard, S17=False):
    data = readCount()
    trueCount = data[0]["trueCount"]
    # 10 + 10 vs 4 Split at +6 or higher
    if handIsPair(playerHand) and playerHand[0] == 10 and dealerCard == 4 and not handIsSoft(playerHand) and trueCount >= 6:
        return True, "Split!"
    else:
        pass
    # 10 + 10 vs 5 Split at +5 or higher
    if handIsPair(playerHand) and playerHand[0] == 10 and dealerCard == 5 and not handIsSoft(playerHand) and trueCount >= 5:
        return True, "Split!"
    else:
        pass
    # 10 + 10 vs 6 Split at +4 or higher
    if handIsPair(playerHand) and playerHand[0] == 10 and dealerCard == 6 and not handIsSoft(playerHand) and trueCount >= 4:
        return True, "Split!"
    else:
        pass
    # 16 vs 10 Stand at higher than 0
    if getHardTotal(playerHand) == 16 and dealerCard == 10 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount > 0:
        return True, "Stand!"
    else:
        pass
    # 16 vs 9 Stand at +4 or higher
    if getHardTotal(playerHand) == 16 and dealerCard == 9 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 4:
        return True, "Stand!"
    else:
        pass
    # 15 vs 10 Stand at +4 or higher
    if getHardTotal(playerHand) == 15 and dealerCard == 10 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 4:
        return True, "Stand!"
    else:
        pass
    # 10 vs 10 Double at +4 or higher
    if getHardTotal(playerHand) == 10 and dealerCard == 10 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 4:
        return True, "Double!"
    else:
        pass
    # 12 vs 3 Stand at +2 or higher
    if getHardTotal(playerHand) == 10 and dealerCard == 10 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 2:
        return True, "Stand!"
    else:
        pass
    # 12 vs 2 Stand at +3 or higher
    if getHardTotal(playerHand) == 12 and dealerCard == 2 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 3:
        return True, "Stand!"
    else:
        pass
    # 11 vs Ace Double at +4 or higher
    if getHardTotal(playerHand) == 11 and dealerCard == 11 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 1:
        return True, "Double!"
    else:
        pass
    # 9 vs 2 Double at +1 or higher
    if getHardTotal(playerHand) == 9 and dealerCard == 2 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 1:
        return True, "Double!"
    else:
        pass
    # 10 vs Ace Double at +4 or higher
    if getHardTotal(playerHand) == 10 and dealerCard == 11 and not handIsPair(playerHand) and not handIsSoft(playerHand):
        # Stand on soft 17
        if S17 and trueCount >= 4:
            return True, "Double!"
        # Hit on soft 17
        elif not S17 and trueCount >= 3:
            return True, "Double!"
        else:
            pass
    else:
        pass
    # 9 vs 7 Double at +3 or higher
    if getHardTotal(playerHand) == 9 and dealerCard == 7 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 3:
        return True, "Double!"
    else:
        pass
    # 13 vs 2 Hit lower than -1
    if getHardTotal(playerHand) == 13 and dealerCard == 2 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount < -1:
        return True, "Hit!"
    else:
        pass
    # 12 vs 4 Hit at lower than 0
    if getHardTotal(playerHand) == 12 and dealerCard == 4 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount < 0:
        return True, "Hit!"
    else:
        pass
    # 12 vs 5 Hit lower than -2
    if getHardTotal(playerHand) == 12 and dealerCard == 5 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount < -2:
        return True, "Hit!"
    else:
        pass
    # 12 vs 6 Hit lower than -1
    if getHardTotal(playerHand) == 12 and dealerCard == 6 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount < -1:
        return True, "Hit!"
    else:
        pass
    # 13 vs 3 Hit lower than -2
    if getHardTotal(playerHand) == 13 and dealerCard == 3 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount < -2:
        return True, "Hit!"
    else:
        pass
    # 16 vs Ace Stand on 3 or above ONLY ON H17
    if getHardTotal(playerHand) == 16 and dealerCard == 11 and not S17 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 3:
        return True, "Stand!"
    else:
        pass
    # 15 vs Ace Stand on 5 or above ONLY ON H17
    if getHardTotal(playerHand) == 15 and dealerCard == 11 and not S17 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 5:
        return True, "Stand!"
    else:
        pass
    # 8 vs 6 Double on 2 or above
    if getHardTotal(playerHand) == 8 and dealerCard == 6 and not handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount >= 2:
        return True, "Double!"
    else:
        pass
    # Not added: Surrender and Soft Totals
    return False, "No deviation"


def insurance():
    # Insurance
    if getTrueCount() >= 3:
        return True
    else:
        return False
