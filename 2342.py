class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = {}
        max_sum = -1

        for num in nums:
            d_sum = sum(int(i) for i in str(num))

            if d_sum in digit_sum:
                max_sum = max(max_sum,num+digit_sum[d_sum])
                digit_sum[d_sum] = max(digit_sum[d_sum],num)
            else:
                digit_sum[d_sum] = num

        return max_sum