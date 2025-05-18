from typing import TypedDict


def getNumWords(text: str):
    return len(text.split())

def getNumCharOccDict(text: str):
    charOccDict = {}
    for char in text:
        lowerCaseChar = char.lower()
        if(lowerCaseChar in charOccDict):
            charOccDict[lowerCaseChar] += 1
        else:
            charOccDict[lowerCaseChar] = 1

    return charOccDict

class CharCount(TypedDict):
    char: str
    num: int

def sortCharDictIntoList(charOccDic: dict[str, int]) -> list[CharCount]: 
    charCountList = []

    for key, value in charOccDic.items():
        charCountList.append({'char': key, 'num': value})

    charCountList.sort(reverse=True, key = lambda dict: dict['num'])
    return charCountList
