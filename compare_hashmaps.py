from typing import List

class Solution: 
    def hashmap_equal_comparison(self, h1: dict, h2: dict) -> bool: 
        if len(h1) != len(h2): 
            return False
        for key in h1: 
            if key not in h2: 
                return False
            if h1[key] != h2[key]:
                return False
        return True
        
instance = Solution()
print(instance.hashmap_equal_comparison({'a':1,'b':2,'c':3},{'a':1,'b':2,'c':3}))