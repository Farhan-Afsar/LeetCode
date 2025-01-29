class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = set()

        for num in nums:
            if num in a:                 #Set Solution
                a.remove(num)               
            else:
                a.add(num)
        return a.pop()

        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1       #Dictinary
 
        for index,val in freq.items():
            if val == 1:
                return index

        res = 0

        for num in nums:              #XOR
            res ^= num
        return res