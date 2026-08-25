class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        i=0
        j=len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1

        return []

nums = [3,4,5,6]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))