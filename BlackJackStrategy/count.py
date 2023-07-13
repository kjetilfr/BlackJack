from saveLoad import *

data = readCount()
runningCount = data[0]["runningCount"]
decks = data[0]["totalDecks"]
deckSize = data[0]["currentDeckSize"]


def count(card):
    global runningCount
    deckSizeMinus1()
    if 2 <= card <= 6:
        runningCount += 1
    elif card == 10 or card == 11:
        runningCount -= 1
    else:
        runningCount += 0
    setRunningCount(runningCount)
    setTrueCount()


def setTrueCount():
    global runningCount, deckSize
    writeTrueCount(runningCount / deckSize)
    

def getTrueCount():
    data = readCount()
    return data[0]["trueCount"]


def deckSizeMinus1():
    global deckSize
    deckSize = deckSize * 52
    deckSize -= 1
    deckSize = deckSize / 52
    writeCurrentDeckSize(deckSize)
