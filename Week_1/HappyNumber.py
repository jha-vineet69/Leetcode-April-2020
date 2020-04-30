class Solution:
    def isHappy(self, n: int) -> bool:
        dict={}
        while n!=1 and n not in dict:
            sum=0
            dict[n]=1
            while n!=0:
                temp=n%10
                sum+=(temp)**2
                n=n//10
            n=sum
        if n==1:
            return True
        return False
        