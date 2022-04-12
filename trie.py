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

    def searchIn(self, word):
        word_notfound = True
        cur = self.head
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                cur = self.head
                # re-check when cursor at root        
                if ch in cur:
                    cur = cur[ch]
                else:
                    cur = self.head

            if '*' in cur:
                print(cur['*'],"-- spotted")
                word_notfound = False
                cur = self.head
        
        # if '*' is not present,
        # that means no word found
        if word_notfound:
            print("There are no word found")

# main program
enterInput = input("Enter a string: ")
wordArray = [str(x) for x in input("Enter the words you want to search in the string (, seperated):\n").split(', ')]

tree = Trie()
for word in wordArray:
    tree.add(word)
tree.searchIn(enterInput)