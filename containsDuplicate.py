from typing import List

class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool: 
        hashmap={}
        for i in range (len(nums)):
            if nums[i] in hashmap:
                return True
            else: 
                hashmap[nums[i]] = i
        return False
    
instance = Solution()
print(instance.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

class Solution2:
    def test(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
sol = Solution2()
print(Solution2().test([1,2,3]))