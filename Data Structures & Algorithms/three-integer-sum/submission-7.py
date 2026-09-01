class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets_arr = []
        already_accounted = set()
        for i in range(len(sorted_nums)):
            sum_of_pair = -1 * sorted_nums[i]
            left = 0
            right = len(sorted_nums) - 1
            triplet = []
            while (left < right):
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue
                curr = sorted_nums[left] + sorted_nums[right]
                if curr > sum_of_pair:
                    right -= 1
                elif curr < sum_of_pair:
                    left += 1
                else:
                    triplet.append(sorted_nums[i])
                    triplet.append(sorted_nums[left])
                    triplet.append(sorted_nums[right])
                    sorted_triplet = sorted(triplet)
                    if (sorted_triplet not in triplets_arr):
                        triplets_arr.append(sorted_triplet)
                    triplet = []
                    left += 1
                    right -= 1
        return triplets_arr

        