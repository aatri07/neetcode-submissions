class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 1
        sorted_nums = sorted(nums)
        streak = 1
        max_streak = 0
        for i in range(1, len(nums)):
            if sorted_nums[i] == 1 + sorted_nums[i - 1]:
                streak += 1
            elif sorted_nums[i] == sorted_nums[i - 1]:
                pass
            else:
                streak = 1
            if streak > max_streak:
                max_streak = streak

        return max_streak 