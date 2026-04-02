class Token:
    def __init__(self, value: str):
        self._value = value.lower()

    def value(self):
        return self._value
    
class TokenMethod:

    def tokenize(TextFilePath: str) -> list[Token]:

        #NEED TO CHANGE THIS TO SUPPORT PUNCUTATION

        ''' Write a method/function that reads in a text file and returns a 
        list of the tokens in that file. For the purposes of this project,
        a token is a sequence of alphanumeric characters, independent of
        capitalization (so Apple, apple, aPpLe are the same token). You
        are not allowed to use regular expressions, and you are not allowed
        to import a tokenizer (e.g. from NLTK), since you are being asked to
        write a tokenizer. '''
        if (TextFilePath.startswith("\"") and TextFilePath.endswith("\"")) or (TextFilePath.startswith("\'") and TextFilePath.endswith("\'")):
            TextFilePath = TextFilePath[1:-1]

        # print("trying to open: " + TextFilePath)

        with open(TextFilePath, "r") as file:
            fileAsStr = file.read()

        puncutation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
        for character in puncutation:
            fileAsStr = fileAsStr.replace(character, " ")
            
        allWords = [Token(word) for word in fileAsStr.split() if word.isascii()]

        # print(allWords)

        return allWords

    def computeWordFrequencies(tokenList: list[Token]) -> dict:
        ''' returns Map<Token,Count>  
        Write another method/function that counts the number of occurrences
        of each token in the token list. Remember that you should write this
        assignment yourself from scratch so you are not allowed to import a
        counter when the assignment asks you to write that method. '''
        
        mappedFrequencies = {}
        for token in tokenList:
            if token.value() in mappedFrequencies.keys():
                mappedFrequencies[token.value()] += 1
            else:
                mappedFrequencies[token.value()] = 1
        return mappedFrequencies

    def print(frequencyMapping: dict) -> None:
        '''Finally, write a method that prints out the word frequency count
        onto the screen. The print out should be ordered by decreasing 
        frequency (so, the highest frequency words first). 

        Choose one of the following: 

        <token>\t<freq>
        <token> <freq>
                                 <token> - <freq>
        <token> = <freq>
        <token> > <freq>
        <token> -> <freq>
        <token> => <freq>'''


        # print(frequencyMapping)

        sortedFrequencies = sorted(frequencyMapping.items())
    
        # print("printing sorted Frequencies: ", sortedFrequencies)

        for token, frequency in sortedFrequencies:
            print(f'{token} - {frequency}')

def main():
    filePath = input("Please enter a text file to tokenize, or submit a null string to terminate the program.\n")
    if filePath:
        # try:
            tm = TokenMethod
            tokenized = tm.tokenize(filePath)
            frequencies = tm.computeWordFrequencies(tokenized)
            tm.print(frequencies)
            print()
        
        # except:
            print("Unable to open path. Try again.")
            print()
            main()

if __name__ == "__main__":
    main()