class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1+freq.get(i,0)
        
        sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_freq[i][0])
        return result