class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        maxEndingHere = nums[0]
        for i in range(1,len(nums)):
            maxEndingHere = max(maxEndingHere+nums[i], nums[i])
            maxSoFar = max(maxSoFar,maxEndingHere)
        return maxSoFar