from typing import List
##Brute force method
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: 
                    return [i,j]

instance = Solution1()
print(instance.twoSum([1,2,3,5],7))
##O(n) solution
class Solution2: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dictionary: 
                return [dictionary[complement], i]
            else: 
                dictionary[nums[i]] = i
test = Solution2()
print(test.twoSum([1,2,3,4],7))
