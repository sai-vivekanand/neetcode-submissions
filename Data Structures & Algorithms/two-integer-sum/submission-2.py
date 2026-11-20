class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in sumMap:
                return [sumMap[complement],i]
            sumMap[num]=i
        return []
        