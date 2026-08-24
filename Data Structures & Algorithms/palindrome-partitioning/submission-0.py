class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(ss):
            return ss == ss[::-1]

        def split(j, i, path):

            if j >= len(s):
                result.append(path[:])
                return
            if i >= len(s):
                return

            if isPalindrome(s[j:i+1]):
                # print(f"found {s[j:i+1]}")
                path.append(s[j:i+1])
                split(i + 1, i+1, path)
                path.pop()


            split(j, i+1, path)

        split(0, 0, [])

        return result


