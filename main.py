
def numberOfCharacter(text):
    characters = {}
    loweredText = text.lower()
    
    for x in loweredText:
        if x in characters.keys():
            characters[x] += 1
        else:
            characters[x] = 1
            
    return characters

def numberOfWord(text):
    words = text.split()
    
    return len(words)

def removeNonAlpha(charDict):
    newCharDict = {}
    for x in charDict:
        if x.isalpha():
            newCharDict[x] = charDict[x]
    
    return newCharDict
    
def convertToList(charDict):
    charlist =[]
    
    for x in charDict:
        charlist.append(
            {
                "name": x,
                "num" : charDict[x]
            }
        )
    
    return charlist
    
def sortDict(toSort):
    return toSort["num"]

def getReport(num_words, char_list):
    report = "--- begin report of book/frankenstein.txt ---"
    report += f"\n{num_words} words found in the document"
    
    char_list.sort(reverse=True, key=sortDict)
    
    for x in char_list:
        report += f"\n The \'{x['name']}\' character was found {x['num']} times"
        
        
    return report

def main():

    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    
    num_words = numberOfWord(file_content)
    char_dict = numberOfCharacter(file_content)
    char_dict = removeNonAlpha(char_dict)
    char_list = convertToList(char_dict)
    
    
    report = getReport(num_words, char_list)
    print(report)
    
if __name__ == "__main__":
    main()