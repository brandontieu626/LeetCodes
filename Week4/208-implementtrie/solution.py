class TrieNode:
    def __init__(self):
        self.neighbors={}
        self.word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root

        for c in word:
            if c not in curr.neighbors:
                curr.neighbors[c]=TrieNode()
            curr=curr.neighbors[c]
        curr.word=True
     
    def search(self, word: str) -> bool:
        curr=self.root

        for c in word:
            if c not in curr.neighbors:
                return False
            curr=curr.neighbors[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr=self.root

        for c in prefix:
            if c not in curr.neighbors:
                return False
            curr=curr.neighbors[c]
        
        return True
