class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        solution = [0] * 2
        for i in range(len(nums)):
            need = target - nums[i]
            if (need in index_map):
                solution[0] = index_map[need]
                solution[1] = i
                return solution
            else:
                index_map[nums[i]] = i
            
        
        return solution
        
        