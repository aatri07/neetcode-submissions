class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
            
        # Left max peak seen so far for each index
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        # Right max peak seen so far for each index
        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        # Water at index i is determined by the highest peaks
        # to its left and right
        currVol = 0
        for i in range(n):
            currVol += min(left_max[i], right_max[i]) - height[i]
            
        return currVol