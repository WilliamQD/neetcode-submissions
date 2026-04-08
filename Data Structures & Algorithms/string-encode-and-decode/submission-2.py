class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prepend length and '#' to EVERY string
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        result = []
        
        i = 0
        length = ""

        while i < len(s):
            if s[i] == "#":
                length = int(length)
                
                result.append(s[i+1:i+length+1])
                
                i += (length + 1)
                length = ""
            else:
                length += s[i]
                i += 1
            

        return result

