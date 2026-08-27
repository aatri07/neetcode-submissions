class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # prefix pass
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        
        # suffix pass
        suffixProd = 1
        for j in reversed(range(len(nums))):
            output[j] = suffixProd * output[j]
            suffixProd = suffixProd * nums[j]
        
        return output




        