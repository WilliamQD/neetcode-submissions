from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for words in strs:
            char_list = [0] * 26

            for char in words:
                char_list[ord(char) - ord('a')] += 1

            hashmap[tuple(char_list)].append(words)

        return list(hashmap.values())