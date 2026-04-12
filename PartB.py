from PartA import Token, TokenMethod
import sys

def sameTokens(first: dict, sec: dict) -> None:
    # RUNTIME: O(n) as it iterates through an interesection of two dictionaries;
    # one with n elements and another with m elements.

    numSharedTokens = 0

    for commonToken in (first.keys() & sec.keys()):
        print(commonToken)
        numSharedTokens += 1
    
    print(numSharedTokens)
    


def main():
    # RUNTIME Utilizes sameTokens as well as all methods from Part A, besides main()
    # meaning that it takes on the highest runtime from the above methods. tokenize() has the highest runtime,
    # with its possibility of an O(n^2) runtime.

    if len(sys.argv) == 3:
        filePath1 = sys.argv[1]
        filePath2 = sys.argv[2]
        try:
            tm = TokenMethod
            tokenized1 = tm.tokenize(filePath1)
            frequencies1 = tm.computeWordFrequencies(tokenized1)

            tokenized2 = tm.tokenize(filePath2)
            frequencies2 = tm.computeWordFrequencies(tokenized2)

            sameTokens(frequencies1, frequencies2)
        
        except:
            print("Unable to open path or path is invalid. Please restart the program to try again.") # CHANGE LATER
    else:
        print("Please restart the program and specify two file paths")

if __name__ == "__main__":
    main()