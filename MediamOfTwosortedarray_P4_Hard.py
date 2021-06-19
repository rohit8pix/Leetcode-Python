class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 +nums2
        nums1.sort()
        if len(nums1) % 2!=0:
            #x = int((len(nums1)-1)/2)
            return(nums1[int((len(nums1)-1)/2)])
        if len(nums1) % 2==0:
            #x = int((size-1)/2)
            return((nums1[int((len(nums1)-1)/2)]+nums1[int((len(nums1)-1)/2)+1])/2)
        
