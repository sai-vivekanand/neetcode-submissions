class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k =0
        l = len(nums)

        while k < l:
            if nums[k]==val:
                nums[k]= nums[l-1]
                l-=1
            else:
                k+=1
        return k
                
                

        
                
                