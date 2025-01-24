class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for i in range(len(strs)):
            anagram = []
            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):     #O(n^2)
                    anagram.append(strs[j])
            if anagram not in result:
                result.append(anagram)
        return result

        anagram_group = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_group:
                anagram_group[sorted_word] = [word]
            else:
                anagram_group[sorted_word].append(word)
        result = []

        for i in anagram_group.values():
            result.append(i)
        return result