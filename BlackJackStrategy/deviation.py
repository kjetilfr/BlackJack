from saveLoad import readCount, readRules
from pairHand import *
from hardHand import *
from softHand import *


def deviation(playerHand, dealerCard):
    data = readCount()
    trueCount = data[0]["trueCount"]
    print("DEVIATION")
    print("Hand: " + str(playerHand[0]) + " " + str(playerHand[1]) + " True Count: " + str(trueCount))
    # 16 vs 9 Stand at +5 or higher
    if getHardTotal(playerHand) == 16 and dealerCard == 9 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount > 5:
        return True, "Stand!"
    else:
        pass
    # 16 vs 10 Stand at 0 or higher
    if getHardTotal(playerHand) == 16 and dealerCard == 10 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount > 0:
        return True, "Stand!"
    else:
        pass
    # 15 vs 10 Stand at 5 or higher
    if getHardTotal(playerHand) == 15 and dealerCard == 10 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount > 4:
        return True, "Stand!"
    else:
        pass
    # 13 vs 2 Stand at -1 or lower
    if getHardTotal(playerHand) == 13 and dealerCard == 2 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount < -1:
        return True, "Hit!"
    else:
        pass
    # 13 vs 3 Stand at -2 or lower
    if getHardTotal(playerHand) == 13 and dealerCard == 3 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount < -2:
        return True, "Hit!"
    else:
        pass
    # 12 vs 2 Stand at 4 or higher
    if getHardTotal(playerHand) == 12 and dealerCard == 2 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount > 4:
        return True, "Stand!"
    else:
        pass
    # 12 vs 3 Stand at 2 or higher
    if getHardTotal(playerHand) == 12 and dealerCard == 3 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount > 2:
        return True, "Stand!"
    else:
        pass
    # 12 vs 4 Stand at -1 or higher
    if getHardTotal(playerHand) == 12 and dealerCard == 4 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount > 0:
        return True, "Stand!"
    else:
        pass
    # 12 vs 5 Stand at -1 or higher
    if getHardTotal(playerHand) == 12 and dealerCard == 5 and not handIsSoft(playerHand) and not handIsPair(playerHand) and trueCount < -1:
        return True, "Hit!"
    else:
        pass
    # 12 vs 6 Hit at -1/-3 or lower
    if getHardTotal(playerHand) == 12 and dealerCard == 6 and not handIsSoft(playerHand) and not handIsPair(playerHand):
        data = readRules()
        # at - 1 or higher, Game is stand on soft 17
        if data[0]["StandOnSoft17"] == 1 and trueCount < -1:
            return True, "Hit!"
        # at - 3 or higher, Game is hit on soft 17
        elif data[0]["StandOnSoft17"] == 0 and trueCount < -3:
            return True, "Hit!"
        else:
            pass
    else:
        pass
    # 11 vs Ace
    # Always double 11?
    # 10 vs 10 Double or hit at 4 or higher
    if getHardTotal(playerHand) == 10 and dealerCard == 10 and not handIsSoft(playerHand) and trueCount > 4:
        return True, "Double! or Hit!"
    else:
        pass
    # 10 vs Ace Double or hit at 4/3 or higher
    if getHardTotal(playerHand) == 10 and dealerCard == 11 and not handIsSoft(playerHand):
        data = readRules()
        # at 4 or higher, Game is stand on soft 17
        if data[0]["StandOnSoft17"] == 1 and trueCount > 4:
            return True, "Double! ot Hit!"
        # at 3 or higher, Game is hit on soft 17
        elif data[0]["StandOnSoft17"] == 0 and trueCount > 3:
            return True, "Double! or Hit!"
        else:
            pass
    else:
        pass
    # 9 vs 2 Double or hit at 1 or higher
    if getHardTotal(playerHand) == 9 and dealerCard == 2 and not handIsSoft(playerHand) and trueCount > 1:
        return True, "Double! or Hit!"
    else:
        pass
    # 9 vs 7 Stand at 4 or higher
    if getHardTotal(playerHand) == 9 and dealerCard == 7 and not handIsSoft(playerHand) and trueCount > 4:
        return True, "Double! or Hit!"
    else:
        pass
    # 10 + 10 vs 5 Split at 5 or higher
    if playerHand[0] == 10 and dealerCard == 5 and handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount > 5:
        return True, "Split!"
    else:
        pass
    # 10 + 10 vs 6 Split at 5 or higher
    if playerHand[0] == 10 and dealerCard == 6 and handIsPair(playerHand) and not handIsSoft(playerHand) and trueCount > 5:
        return True, "Split!"
    else:
        pass
    return False, "No deviation"


def insurance(trueCount):
    data = readCount()
    trueCount = data[0]["trueCount"]
    # Insurance
    if trueCount > 3:
        return True
    else:
        return False
