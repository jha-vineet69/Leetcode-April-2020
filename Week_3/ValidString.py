class Solution:
    def checkValidString(self, s: str) -> bool:
        lower=0
        upper=0
        for ch in s:
            if ch=='(':
                lower+=1
                upper+=1
            elif ch ==')':
                lower-=1
                upper-=1
                if lower< 0:
                    lower=0
            elif ch =='*':
                lower-=1
                upper+=1
                if lower<0:
                    lower=0
            if upper<0:
                return False
        return lower==0
        