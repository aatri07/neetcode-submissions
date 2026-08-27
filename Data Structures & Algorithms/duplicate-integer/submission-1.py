class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set()
        for elem in nums:
            if elem in check_set:
                return True
            else:
                check_set.add(elem)

        return False