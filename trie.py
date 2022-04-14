class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # '*' indicates the end of the word
        cur['*'] = word
        print(word,"has been added to the trie.")

    def searchIn(self, word):
        word_notfound = True
        cur = self.head
        print("Searching...")
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                cur = self.head
                # re-check when cursor at root        
                if ch in cur:
                    cur = cur[ch]

            if '*' in cur:
                print(cur['*'],"-- spotted")
                word_notfound = False
                cur = self.head
        
        # if '*' is not present,
        # that means no word found
        if word_notfound:
            print("There are no word found")

# main program
tree = Trie()
tree.add("fun")
tree.add("algo")
tree.searchIn("algorisfunalgoisgreat")