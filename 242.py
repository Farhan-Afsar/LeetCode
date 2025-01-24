class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS,CountT = {} , {}

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],0)          #O(n)
            CountT[t[i]] = 1 + CountT.get(t[i],0)

        return CountS == CountT


        t = list(t)

        for char in s:
            if char in t:
                t.remove(char)            #O(n^2)
            else:
                return False
        return len(t) == 0

        return sorted(s) == sorted(t)       #O(nlogn)


