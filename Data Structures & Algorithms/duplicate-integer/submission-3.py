# With Sorting method

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

sol = Solution()
nums=[1, 2, 3, 3]
print(sol.hasDuplicate(nums))