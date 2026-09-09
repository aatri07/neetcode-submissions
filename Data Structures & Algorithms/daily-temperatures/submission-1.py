class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of temperatures

        for i in range(n):
            # While current temperature is warmer than the top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            # Push current day's index to check against future days
            stack.append(i)

        return result
        
        