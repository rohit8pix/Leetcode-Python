# this solution is naive and takes 608 ms in Leetcode 
# non optimized

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ans=[]
        if len(arr)>=3:
            for j in range(len(arr)-1):
                if arr[j]<arr[j+1]:
                    ans.append(1)
                elif arr[j+1]<arr[j]:
                    ans.append(-1)
                elif arr[j+1]==arr[j]:
                    ans.append(0)
            zero =0
            if zero in ans:
                return False
                
            else:

                count=0
                for i in range(len(ans)):
                    if ans[i]==-1:
                        count=i
                        
                        break

                bef = ans[:i]
                aft= ans[i:]
            
                f = -1
                fno = 1

                if (not f in bef) and (not fno in aft) and len(bef)>0 and len(aft)>0:
                    return True
                else:
                    return False
        else:
            return False



