class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x]+nums[y]) == target:
                    return [x, y]
        return []


print(Solution.twoSum(Solution, [12, 7, 11, 2], 9))
