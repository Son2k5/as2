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



def main():
    test_cases = [
    "harry potter and the philosopher's stone by rowling in 1997",
    "harry potter and the chamber of secrets by rowling in 1998",
    "harry potter and the prisoner of azkaban by rowling in 1999",
    "harry potter and the goblet of fire by rowling in 2000",
    "harry potter and the order of the phoenix by rowling in 2003",
    "harry potter and the half-blood prince by rowling in 2005",
    "harry potter and the deathly hallows by rowling in 2007",
    "the casual vacancy by rowling in 2012",
    "the hobbit by tolkien in 1937",
    "the fellowship of the ring by tolkien in 1954",
    "the two towers by tolkien in 1954",
    "the return of the king by tolkien in 1955",
    "the silmarillion by tolkien in 1977",
    "foundation by asimov in 1951",
    "foundation and empire by asimov in 1952",
    "second foundation by asimov in 1953",
    "i, robot by asimov in 1950",
    "the caves of steel by asimov in 1954",
    "the naked sun by asimov in 1957",
    "the hunger games by collins in 2008",
    "catching fire by collins in 2009",
    "mockingjay by collins in 2010",
    "dune by herbert in 1965",
    "dune messiah by herbert in 1969",
    "children of dune by herbert in 1976",
    "brave new world by huxley in 1932",
    "1984 by orwell in 1949",
    "animal farm by orwell in 1945",
    "a game of thrones by george r. r. martin in 1996",
    "a clash of kings by george r. r. martin in 1998",
    "a storm of swords by george r. r. martin in 2000",
    "a feast for crows by george r. r. martin in 2005",
    "a dance with dragons by george r. r. martin in 2011",
    "neuromancer by gibson in 1984",
    "count zero by gibson in 1986",
    "mona lisa overdrive by gibson in 1988",
    "fahrenheit 451 by bradbury in 1953",
    "the martian chronicles by bradbury in 1950",
    "do androids dream of electric sheep by dick in 1968",
    "ubik by dick in 1969",
    "valis by dick in 1981",
    "snow crash by stephenson in 1992",
    "cryptonomicon by stephenson in 1999",
    "the diamond age by stephenson in 1995",
    "mistborn by sanderson in 2006",
    "the well of ascension by sanderson in 2007",
    "the hero of ages by sanderson in 2008",
    "elantris by sanderson in 2005",
    "warbreaker by sanderson in 2009",
    "oathbringer by sanderson in 2017"
]


    # Feed toàn bộ dữ liệu test
    for line in test_cases:
        aset.feed(line)

    # ---- Kiểm tra countForAuthor() ----
    print("rowling:", aset.countForAuthor("rowling"))
    print("tolkien:", aset.countForAuthor("tolkien"))
    print("asimov:", aset.countForAuthor("asimov"))
    print("collins:", aset.countForAuthor("collins"))
    print("herbert:", aset.countForAuthor("herbert"))
    print("huxley:", aset.countForAuthor("huxley"))
    print("orwell:", aset.countForAuthor("orwell"))
    print("george r. r. martin:", aset.countForAuthor("george r. r. martin"))
    print("gibson:", aset.countForAuthor("gibson"))
    print("bradbury:", aset.countForAuthor("bradbury"))
    print("dick:", aset.countForAuthor("dick"))
    print("stephenson:", aset.countForAuthor("stephenson"))
    print("sanderson:", aset.countForAuthor("sanderson"))

    # ---- Kiểm tra countForSentence() ----
    print(aset.countForSentence("foundation, the hobbit, mockingjay"))
    print(aset.countForSentence("mistborn, the hero of ages, elantris"))
    print(aset.countForSentence("1984, animal farm"))
    print(aset.countForSentence("neuromancer, valis"))
    print(aset.countForSentence("harry potter and the goblet of fire, brave new world"))

    # ---- Kiểm tra mostProductiveAuthor() ----
    print("most productive:", aset.mostProductiveAuthor())

    # ---- Kiểm tra topKAuthors() ----
    print("top 3:", aset.topKAuthors(3))
    print("top 5:", aset.topKAuthors(5))

if __name__ == '__main__':
    main()
