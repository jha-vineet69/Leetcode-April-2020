class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in range(len(nums)):
            res^= nums[x]
        return res