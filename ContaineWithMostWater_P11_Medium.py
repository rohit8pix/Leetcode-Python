class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        start = 0
        end = len(height)-1
        while start!=end:
            l = min(height[start],height[end])
            a = (end-start)*l
            maxarea = max(a,maxarea)
            if height[start]<height[end]:
                start = start+1
            else:
                end =end-1
        return maxarea
