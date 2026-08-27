class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in num_freqs:
                num_freqs[nums[i]] += 1
            else:
                num_freqs[nums[i]] = 1
        
        sorted_freqs = dict(sorted(num_freqs.items(), key=lambda item: item[1], reverse=True))

        for key in sorted_freqs:
            res.append(key)
            if len(res) == k:
                return res
        
        return res
            

        