class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            word = s[j+1:j+length+1]
            result.append(word)

            i = j+length+1
        return result


