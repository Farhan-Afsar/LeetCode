class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        val_map = {0:1}
        count = 0

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        for i in range(len(nums)):
            if prefix[i] - k in val_map:
                count += val_map[prefix[i] - k]
            if prefix[i] in val_map:
                val_map[prefix[i]] += 1
            else:
                val_map[prefix[i]] = 1
        return count
            