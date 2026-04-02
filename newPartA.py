
class Token:
    def __init__(self, value: str):
        self._value = value

    def value(self):
        return self._value

    

    
class TokenList:
    def __init__(self):
        self.tokens = []
        self.frequencies = {}

    def tokenize(self, TextFilePath: str) -> list[Token]:
        ''' Write a method/function that reads in a text file and returns a 
        list of the tokens in that file. For the purposes of this project,
        a token is a sequence of alphanumeric characters, independent of
        capitalization (so Apple, apple, aPpLe are the same token). You
        are not allowed to use regular expressions, and you are not allowed
        to import a tokenizer (e.g. from NLTK), since you are being asked to
        write a tokenizer. '''

        with open(TextFilePath, "r") as file:
            allWords = [Token(word.lower()) for word in file.read().split() if word.isascii()]

        self.tokens = allWords
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


    def print() -> None:
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
        pass
    
    
if __name__ == "main":
    pass