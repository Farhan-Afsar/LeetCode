class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        # s = set()

        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if (nums[i]+nums[j]+nums[k] == 0):
        #                 triple = tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 s.add(triple)
        
        # return list(s)
        # ans = set()
        # for i in range(n):
        #     s = set()
        #     for j in range(i+1,n):
        #         third = -(nums[i] + nums [j])
        #         if third in s:
        #             triple = tuple(sorted([nums[i],nums[j],third]))
        #             ans.add(triple)
        #         s.add(nums[j])
        # return list(ans)
        nums.sort()
        ans = set()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j+=1
                elif sum > 0:
                    k -= 1
                else:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
        return list(ans)
