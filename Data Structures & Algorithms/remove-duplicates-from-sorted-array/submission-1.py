class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0;
        
        for x in range(0, len(nums)-1):
            if nums[x]!=nums[x+1]:
                count+=1
                y=nums[x]
                nums[count-1]=y
        
        count+=1
        nums[count-1]=nums[len(nums)-1]
        
        return count
            
