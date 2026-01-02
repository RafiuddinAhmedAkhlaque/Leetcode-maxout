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

#using set (no need index-value here, just the values here work)
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
print(sol.test([1,2,3]))

class Solution3:
    def test2(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
sol2 = Solution3()
print(sol2.test2([1,2,3]))