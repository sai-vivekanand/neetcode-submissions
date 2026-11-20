class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap={}
        for i,num in enumerate(nums):
            if num in countMap:
                return True
            else:
                countMap[num]=i
        return False
         