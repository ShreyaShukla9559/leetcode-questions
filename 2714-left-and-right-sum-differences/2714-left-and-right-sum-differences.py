class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        ans = [0]
        for i in range(1, len(nums)):
            pre_sum += nums[i - 1]
            ans.append(pre_sum)
        suf_sum = 0
        for i in range(len(nums) - 2, -1, -1):
            suf_sum += nums[i + 1]
            ans[i] = abs(ans[i] - suf_sum)
        return ans