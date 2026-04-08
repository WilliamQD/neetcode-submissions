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
        # length = ""

        while i < len(s):
            # manual way
            # if s[i] == "#":
            #     length = int(length)
                
            #     result.append(s[i+1:i+length+1])
                
            #     i += (length + 1)
            #     length = ""
            # else:
            #     length += s[i]
            #     i += 1

            # better way
            # Find the next '#' starting from index i
            j = s.find("#", i)
            
            # The characters between i and j form the length
            length = int(s[i:j])
            
            # Extract the string based on that length
            # The string starts at j+1 and ends at j+1+length
            result.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next length-prefix
            i = j + 1 + length

            

        return result

