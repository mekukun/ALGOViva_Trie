class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # * indicates the end of the word
        cur['*'] = word

    def searchIn(self, word):
        word_notfound = True
        cur = self.head
        for ch in word:
            if ch in cur:
                cur = cur[ch]

            if '*' in cur:
                print(cur['*'],"-- exists")
                word_notfound = False
                cur = self.head
        
        if word_notfound:
            print("There are none")

dictionary = Trie()
dictionary.add("fun")
dictionary.add("algo")
dictionary.searchIn("algorisfunalgoisgreat")