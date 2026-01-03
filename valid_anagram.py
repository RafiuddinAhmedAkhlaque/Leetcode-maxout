from typing import List

class Solution: 
    def valid_anagram(self, s: str, t: str) -> bool: 
        hashmap1 = {}
        hashmap2 = {}
        if len(s) != len(t): 
            return False
        for char in s: 
            if char in hashmap1: 
                hashmap1[char] += 1
            else: 
                hashmap1[char] = 1
        for char in t: 
            if char in hashmap2: 
                hashmap2[char] += 1
            else: 
                hashmap2[char] = 1
        if hashmap1 == hashmap2: 
            return True
        return False
    
instance = Solution()
print(instance.valid_anagram("string","ringst"))