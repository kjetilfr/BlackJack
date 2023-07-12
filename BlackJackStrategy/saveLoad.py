import json


def readRules():
    f = open('./rules.json')
    data = json.load(f)
    f.close()
    return data["settings"]


def readCount():
    f = open('./rules.json')
    data = json.load(f)
    f.close()
    return data["count"]


def writeRunningCount(runningCount):
    with open("./rules.json", "r+") as f:
        data = json.load(f)
        # data  = profileName
        data["count"][0]["runningCount"] += runningCount

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()


def writeTrueCount(trueCount):
    with open("./rules.json", "r+") as f:
        data = json.load(f)
        # data  = profileName
        data["count"][0]["trueCount"] = trueCount

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()


def writeCurrentDeckSize(deckSize):
    with open("./rules.json", "r+") as f:
        data = json.load(f)
        # data  = profileName
        data["count"][0]["currentDeckSize"] = deckSize

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()
