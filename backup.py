from xml.sax.handler import property_interning_dict


class Node:
    def __init__(self):
        self.children = {}
        self.isVisited = False
        self.isEndofWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
            cur.isVisited = False
        cur.isEndofWord = True
        print(word, "has been added to the tree.")

    def searchIn(self, word, keyword):
        word_found = ""
        cur = self.root
        print("Searching for",keyword,"...")
        for ch in word:
            if ch in cur.children and cur.children[ch].isVisited==False:
                word_found += ch
                cur = cur.children[ch]
                cur.isVisited = True
            else:
                cur = self.root
                word_found = ""
            if cur.isEndofWord:
                if word_found == keyword:
                    print(keyword,"has been found.")
                    break
        
        if word_found != keyword:
            print(keyword,"is not found in", word)

# main program
enterInput = input("Enter a string: ")
wordArray = [str(x) for x in input("Enter the words you want to search in the string (, seperated):\n").split(', ')]

tree = Trie()
for word in wordArray:
    tree.add(word)
    tree.searchIn(enterInput, word)