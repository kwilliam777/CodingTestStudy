class WordDictionary:

    def __init__(self):
       
        # Initialize your data structure here.
        self.children = [None]*26
        self.isEndOfWord = False
       

    def addWord(self, word: str) -> None:

        # Adds a word into the data structure.
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
       
        curr.isEndOfWord = True;
       

    def search(self, word: str) -> bool:

        # Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
           
            if curr.children[ord(c) - ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]
       
        return curr != None and curr.isEndOfWord

# class WordDictionary(object):

#     def __init__(self):
#         self.dict, self.len2word  = defaultdict(set), defaultdict(set)

#     def addWord(self, word):
#         # self.dict: key is combination of index and character, value is a word set whose i-th letter is c
#         for i, c in enumerate(word): self.dict[(i, c)].add(word)
#         # self.len2word: key is length of word, value is a word set whose length is equal to key
#         self.len2word[len(word)].add(word)

#     def search(self, word):
#         ans = copy.deepcopy(self.len2word[len(word)])
#         for i, c in enumerate(word):
#             if c != '.': ans &= self.dict[(i, c)]
#         return True if len(ans) else False