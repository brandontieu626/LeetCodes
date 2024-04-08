class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root

        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            
            curr=curr.children[c]
        
        curr.word=True

    def search(self, word: str) -> bool:

        def dfs(i,root):
            curr=root

            for i in range(i, len(word)):
                c=word[i]

                if c=='.':
                    for node in curr.children.values():
                        if dfs(i+1,node):
                            return True
                    return False
                else:
                    if c in curr.children:
                        curr=curr.children[c]
                    else:
                        return False
            
            return curr.word
        
        return dfs(0,self.root)