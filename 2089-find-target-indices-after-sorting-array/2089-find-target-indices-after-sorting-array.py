class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = [ ]
        for index in range(0,len(nums)):
            if target == nums[index]:
                result += [index]
        return result

