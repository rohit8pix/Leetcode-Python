class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        j=1
        for j in range(0,len(nums)):
            if nums[j]!=nums[count]:
                count+=1
                nums[count]=nums[j]
                
        return count+1
        
