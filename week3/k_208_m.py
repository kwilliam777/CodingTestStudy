class Trie:

    def __init__(self):
        self.child = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        curr = self
        for letter in word:
            if letter not in curr.child:
                curr.child[letter] = Trie()
            curr = curr.child[letter]
           
        curr.child["end"] = True
               

    def search(self, word: str) -> bool:
        curr = self
        for letter in word:
            if letter not in curr.child:
                return False
            else:
                curr = curr.child[letter]
        if "end" not in curr.child:
            return False
        else:
            return True
               

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for letter in prefix:
            if letter not in curr.child:
                return False
            else:
                curr = curr.child[letter]    
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)