class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x =[]
        for i in nums:
            if i not in x:
                x.append(i)
        x.sort(reverse=True)
        if len(nums)>=3 and len(x)>=3:
            return(x[2])
        elif len(nums)==2:
            return(x[0])
        elif len(x)==1:
            return(x[0])
        elif len(nums)>=3 and len(x)==2:
            return(x[0])
                                
         
