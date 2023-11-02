class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=[0]*len(pref)
        l[0]=pref[0]
        for i in range(1,len(pref)):
            l[i]=pref[i]^pref[i-1]
        return l    

            
        