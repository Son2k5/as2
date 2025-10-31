import random
class AuthorSet:
    def __init__(self, sentence: str):
        self.__authorDict = {}
        self.feed(sentence)
    
    def feed(self, sentence: str):
        partValues = sentence.split(" by ")
        if len(partValues) != 2:
            return 
        textBefore = partValues[1]
        authorValue = textBefore.split(" in ")[0].strip().lower()
        self.__authorDict[authorValue] = self.__authorDict.get(authorValue, 0) + 1
    
    def countForAuthor(self, nameAuthor: str) -> int:
        return self.__authorDict.get(nameAuthor.lower(), 0)

def main():
   

if __name__ == '__main__':
    main()
