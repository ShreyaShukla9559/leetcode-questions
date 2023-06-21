class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        h={}
        temp=sorted(nums)
        l=len(nums)
        r=[]
        
        for i in range(len(temp)):
            if temp[i] not in h:
                h[temp[i]]=i
        for i in range(len(nums)):
            r.append(h[nums[i]])
        return r            


