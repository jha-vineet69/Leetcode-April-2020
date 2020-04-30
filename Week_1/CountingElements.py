class Solution:
    def countElements(self, arr: List[int]) -> int:
        arrdic = {}
        length = 0
        for num in arr:
            if num in arrdic:
                arrdic[num]+=1
            else:
                arrdic[num] = 1
        for num in arr:
            if arrdic.get(num+1)!=None:
                length+= 1
                
        return length
            