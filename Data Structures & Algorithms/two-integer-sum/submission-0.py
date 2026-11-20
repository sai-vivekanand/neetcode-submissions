class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        net = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in net:
                return [net[diff], i]
            net[num]=i
        