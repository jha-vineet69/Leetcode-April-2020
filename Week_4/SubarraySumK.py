class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return  0
        d = collections.Counter()
        d[0] = 1
        cnt = 0
        res = 0
        
        for num in nums:
            cnt+= num
            
            if (cnt-k) in d:
                res+=d[cnt-k]
                
            d[cnt]+=1
            
        return res
        