class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        # self.children = {'d': PrefixTree(with o as key)}
        # then prefixtree(o) has self.children={'g':PrefixTree(empty)}

    def insert(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = PrefixTree()
            curr = curr.children[w]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            if w not in curr.children:
                return False
            
            curr = curr.children[w]
        
        if curr.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        
        curr = self
        for p in prefix:
            if p not in curr.children:
                return False
            
            curr = curr.children[p]
        
        return True
        