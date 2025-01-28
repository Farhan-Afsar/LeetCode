class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}

        for i in range(len(nums)):              #O(n) + Extra Space
            if nums[i] in freq:
                res.append(nums[i])
            else:
                freq[nums[i]] = 1
        return res

        res = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if(nums[index]) < 0:
                res.append(abs(nums[i]))            #O(n) + No Space
            else:
                nums[index] = -nums[index]
        return res