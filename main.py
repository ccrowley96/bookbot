from stats import getNumWords, getNumCharOccDict, sortCharDictIntoList 
import sys

def getBookText(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    filePath = sys.argv[1]
    bookText = getBookText(filePath)   
    numWords = getNumWords(bookText) 
    numCharOcc = getNumCharOccDict(bookText)
    sortedCharOccList = sortCharDictIntoList(numCharOcc)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    for item in sortedCharOccList:
        if(item['char'].isalpha()):
            print(f"{item['char']}: {item['num']}")


    
main()
