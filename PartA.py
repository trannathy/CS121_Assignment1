import sys

class Token:
    def __init__(self, value: str):
        self._value = value.lower()

    def value(self):
        return self._value
    
class TokenMethod:

    def tokenize(TextFilePath: str) -> list[Token]:

        # RUNTIME: this should, for the most part, run in O(n), but O(n^2) in rare cases.
        # Most of the parsing in done in the O(n) puncuation loop and the list comprehensions.
        # In most cases, notAlNum should be empty, but if it is not, there is a nested
        # for loop that runs in (ON^2) 


        if (TextFilePath.startswith("\"") and TextFilePath.endswith("\"")) or (TextFilePath.startswith("\'") and TextFilePath.endswith("\'")):
            TextFilePath = TextFilePath[1:-1]

        with open(TextFilePath, "r", encoding="ascii", errors="replace") as file:
            fileAsStr = file.read()

        #O(n)
        puncutation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~�"
        for character in puncutation:
            fileAsStr = fileAsStr.replace(character, " ")

        words = fileAsStr.split()
        allTokens = [Token(word) for word in fileAsStr.split() if word.isalnum()]
        notAlNum = [word for word in words if not word.isalnum()]

        #O(n^2)
        for word in notAlNum: 
            for character in word:
                if not character.isalnum():
                    word = word.replace(character, " ")

            newWords = word.split()
            for alNum in newWords:
                allTokens.append(Token(alNum))

        # print(allTokens)

        return allTokens

    def computeWordFrequencies(tokenList: list[Token]) -> dict:
        
        # RUNTIME: This should run in O(n), as it iterates through each
        # token in the dictionary


        mappedFrequencies = {}
        for token in tokenList:
            if token.value() in mappedFrequencies.keys():
                mappedFrequencies[token.value()] += 1
            else:
                mappedFrequencies[token.value()] = 1
        return mappedFrequencies

    def print(frequencyMapping: dict) -> None:
    
        # RUNTIME: This should run in O(n), as it iterates through each
        # token in the dictionary.items().

        #reversal from anossov's first code block in https://www.reddit.com/r/learnpython/comments/2anwld/how_do_i_sort_dictionary_keys_by_their_values/
        sortedFrequencies = sorted(frequencyMapping.items(), key=lambda pair: pair[1], reverse=True)
    
        for token, frequency in sortedFrequencies:
            print(f'{token} - {frequency}')

def main():
    # RUNTIME Utilizes above functions with no loops, meaning that it takes on the 
    # highest runtime from the above methods. tokenize() has the highest runtime,
    # with its possibility of an O(n^2) runtime.
    
    if len(sys.argv) == 2:
        filePath = sys.argv[1]
        try:
            tm = TokenMethod
            tokenized = tm.tokenize(filePath)
            frequencies = tm.computeWordFrequencies(tokenized)
            tm.print(frequencies)
            print()
        
        except:
            print("Unable to open path or path is invalid. Please restart the program to try again.") # CHANGE LATER
    else:
        print("Please restart the program and specify one file path")
   
if __name__ == "__main__":
    main()