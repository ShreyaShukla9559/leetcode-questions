class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        x=n
        while(n!=0):
            s=s+(n%10)
            n=n//10
        m=1
        while(x!=0):
            m=m*(x%10)
            x=x//10
        return m-s