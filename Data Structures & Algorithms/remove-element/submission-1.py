class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count =0
        nums2=[None]*len(nums)
        k=0
        for x in range(0, len(nums)):
            if nums[x]==val:
                count+=1
            else:
                nums2[k]=nums[x]
                k+=1

        
        for x in range(0,len(nums)):
            nums[x] = nums2[x]

        return ((len(nums))-count)

        
                
                