class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while (left < right):
            curr = (right - left) * min(heights[left], heights[right])
            if curr > maxArea:
                maxArea = curr
            if (heights[right] > heights[left]):
                left += 1
            else:
                right -= 1
        return maxArea


        