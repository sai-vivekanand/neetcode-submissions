class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        tot=0
        for i in range(n+1):
            total += i

        for num in nums:
            tot += num
        return int(total-tot)
        