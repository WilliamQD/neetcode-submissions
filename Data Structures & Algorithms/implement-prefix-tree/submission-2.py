class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
        # Legacy comment: this wqas before added TrieNode
        # self.children = {'d': PrefixTree(with o as key)}
        # then prefixtree(o) has self.children={'g':PrefixTree(empty)}

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            
            curr = curr.children[w]
        
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            
            curr = curr.children[p]
        
        return True
        