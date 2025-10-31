import json
import random
class AuthorSet:
    def __init__(self, sentence: str):
        self.__authorDict = {}
        self.__title_to_author = {}
        self.feed(sentence)
    
    def feed(self, sentence: str):
        partValues = sentence.split(" by ")
        if len(partValues) != 2:
            return 
        textBefore = partValues[1]
        titleValue = partValues[0].strip().lower()
        authorValue = textBefore.split(" in ")[0].strip().lower()
        self.__authorDict[authorValue] = self.__authorDict.get(authorValue, 0) + 1
        self.__title_to_author[titleValue] = authorValue
    
    def countForAuthor(self, nameAuthor: str) -> int:
        return self.__authorDict.get(nameAuthor.lower(), 0)
    
    def countForSentence(self, sentence: str) -> int:
        titleValues =[]
        for t in sentence.split(","):
            t_value = t.strip().lower()
            if t_value:
                titleValues.append(t_value)
        totalValue = 0
        haveSeen = set()
        for i in titleValues:
            authorValue = self.__title_to_author.get(i)
            if authorValue and authorValue not in haveSeen:
                totalValue += self.__authorDict[authorValue]
                haveSeen.add(authorValue)
        return totalValue
    
    def mostProductiveAuthor(self) -> str:
        if not self.__authorDict:
            return ""
        maxCount = max(self.__authorDict.values())
        candidateValue = []
        for author, count in self.__authorDict.items():
            if count == maxCount:
                candidateValue.append(author)
        return min(candidateValue)
    def topKAuthors(self, k: int):
        if k <= 0 or not self.__authorDict:
            return []
        itemValues = list(self.__authorDict.items())
        itemValues.sort(key=lambda x: (-x[1], x[0]))
        result = []
        for i in range(min(k, len(itemValues))):
            result.append(itemValues[i][0])
        return result
    
    def feedFromFile(self, filename: str):
        try:
            f = open(filename, "r", encoding='utf-8')
            for line in f:
                line = line.strip()
                if line:
                    self.feed(line)
        except FileNotFoundError:
            pass

    def createJSONFile(self, filename: str):
        itemValue = list(self.__authorDict.items())
        itemValue.sort(key=lambda x: (-x[1], x[0]))
        sortedDict = {}
        for author, count in itemValue:
            sortedDict[author] = count
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(sortedDict, f, indent=2)

def main():

if __name__ == "__main__":
    main()