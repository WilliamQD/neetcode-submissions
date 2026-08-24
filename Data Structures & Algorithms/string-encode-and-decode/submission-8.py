class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # 1. Instantly find the index of the next '#' starting from i
            j = s.find('#', i)
            
            # 2. Grab the length
            length = int(s[i:j])
            
            # 3. Extract the word
            word = s[j + 1 : j + 1 + length]
            result.append(word)
            
            # 4. Jump i forward to the start of the next encoded chunk
            i = j + 1 + length
            
        return result


