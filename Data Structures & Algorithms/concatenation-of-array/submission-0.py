class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None]*2*len(nums)
        for x in range(0,len(nums)):
            ans[x] = nums[x]
            ans[x+len(nums)]= nums[x]

        return ans