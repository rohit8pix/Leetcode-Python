from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for element in strs:
            temp[str(sorted(element))].append(element)
        res = (list(temp.values()))
        return res
        
      
