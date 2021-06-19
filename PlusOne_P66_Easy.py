class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        digits[-1] += 1
        while digits[-i] == 10:
            if i != len(digits):
                digits[-i] = 0
                digits[-i-1] += 1
                i += 1
            else:
                digits[-i] = 0
                digits = [1] + digits 
                break
        return digits
        
