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
    aset = AuthorSet("harry potter by rowling in 1997")

    # Danh sách 50 test case nâng cao
    test_cases = [
        "the casual vacancy by rowling in 2012",
        "the hobbit by tolkien in 1937",
        "The Silmarillion by Tolkien in 1977",              # kiểm tra hoa/thường
        "Foundation by Asimov in 1951",
        "foundation and empire by asimov in 1952",          # cùng tác giả
        "I, Robot by Asimov in 1950",                       # cùng tác giả khác sách
        "mockingjay by collins in 2010",
        "catching fire by collins in 2009",
        " the hunger games by collins in 2008 ",            # khoảng trắng thừa
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
        "VALIS by Dick in 1981",
        "Snow Crash by Stephenson in 1992",
        "cryptonomicon by stephenson in 1999",
        "the diamond age by stephenson in 1995",
        "mistborn by sanderson in 2006",
        "the well of ascension by sanderson in 2007",
        "the hero of ages by sanderson in 2008",
        "warbreaker by sanderson in 2009",
        "elantris by sanderson in 2005",
        "the way of kings by sanderson in 2010",
        "words of radiance by sanderson in 2014",
        "oathbringer by sanderson in 2017",
        "rhythm of war by sanderson in 2020",
        "wrong format example",                             # lỗi định dạng
        "missing in keyword by someauthor 2022",             # lỗi định dạng
        "spaces   by   authorx   in   2000",                 # nhiều khoảng trắng
        "BOOK WITH DASH by some-author in 2010",             # tên có dấu gạch
        "strange symbols #$@! by oddone in 2015",            # ký tự đặc biệt
        "   ",                                               # dòng trống
        "title by ROWLING in 2024",                         # kiểm tra hoa/thường
        "new book by newauthor in 2025",
        "another book by newauthor in 2026",
        "final book by authorx in 2001"
    ]

    for line in test_cases:
        aset.feed(line)

    # In kết quả kiểm tra nhiều trường hợp khác nhau
    print("rowling:", aset.countForAuthor("rowling"))                # 3
    print("tolkien:", aset.countForAuthor("tolkien"))                # 2
    print("asimov:", aset.countForAuthor("asimov"))                  # 3
    print("collins:", aset.countForAuthor("collins"))                # 3
    print("herbert:", aset.countForAuthor("herbert"))                # 3
    print("orwell:", aset.countForAuthor("orwell"))                  # 2
    print("george r. r. martin:", aset.countForAuthor("george r. r. martin"))  # 5
    print("bradbury:", aset.countForAuthor("bradbury"))              # 2
    print("dick:", aset.countForAuthor("dick"))                      # 3
    print("stephenson:", aset.countForAuthor("stephenson"))          # 3
    print("sanderson:", aset.countForAuthor("sanderson"))            # 6
    print("oddone:", aset.countForAuthor("oddone"))                  # 1
    print("some-author:", aset.countForAuthor("some-author"))        # 1
    print("authorx:", aset.countForAuthor("authorx"))                # 2
    print("newauthor:", aset.countForAuthor("newauthor"))            # 2
    print("unknown:", aset.countForAuthor("unknown"))                # 0

if __name__ == '__main__':
    main()
