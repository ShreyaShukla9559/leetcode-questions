class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        for i in range(len(accounts)):
           tw=sum(accounts[i])
           s=max(s,tw)
        return s    