from string import puncutation
class Token:
    def __init__(self, value: str):
        self._value = value.lower()

    def value(self):
        return self._value
    
class TokenList:

    def tokenize(self, TextFilePath: str) -> list[Token]:

        #NEED TO CHANGE THIS TO SUPPORT PUNCUTATION

        ''' Write a method/function that reads in a text file and returns a 
        list of the tokens in that file. For the purposes of this project,
        a token is a sequence of alphanumeric characters, independent of
        capitalization (so Apple, apple, aPpLe are the same token). You
        are not allowed to use regular expressions, and you are not allowed
        to import a tokenizer (e.g. from NLTK), since you are being asked to
        write a tokenizer. '''

        with open(TextFilePath, "r") as file:
            fileAsStr = file.read()

        for character in puncutation:
            fileAsStr.replace(character, " ")
            
        allWords = [Token(word) for word in fileAsStr.split() if word.isascii()]
        return allWords

    def computeWordFrequencies(tokenList: list[Token]) -> dict:
        ''' returns Map<Token,Count>  
        Write another method/function that counts the number of occurrences
        of each token in the token list. Remember that you should write this
        assignment yourself from scratch so you are not allowed to import a
        counter when the assignment asks you to write that method. '''
        
        mappedFrequencies = {}
        for token in tokenList:
            if token in mappedFrequencies.keys():
                mappedFrequencies[token.value] += 1
            else:
                mappedFrequencies[token.value] = 1
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

        #sorted method originated from https://flexiple.com/python/python-sort-dictionary-by-value
        flippedList = sorted((value, key) for (key, value) in frequencyMapping.items())
        sortedMapping = dict([k, v] for v, k in flippedList.reverse())

        for token, freq in enumerate(sortedMapping):
            print(f'{token} - {freq}')
        
    
if __name__ == "main":
    pass