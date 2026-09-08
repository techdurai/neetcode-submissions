class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums and nums.index(diff) != i:
                j = nums.index(diff)
                return [min(i, j), max(i, j)]  # ✅ Always return smaller index first

        return []
