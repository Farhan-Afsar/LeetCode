class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a = set(nums)
        longest = 0

        for num in a:
            if num - 1 not in a:
                current = num
                streak = 1

                while current + 1 in a:
                    current +=1
                    streak += 1
                longest = max(longest,streak)        
        return longest