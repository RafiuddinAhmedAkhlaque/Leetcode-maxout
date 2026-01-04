from typing import List

class Solution: 
    def two_sum_II(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        while left < right: 
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left,right]
            elif current_sum < target: 
                left += 1
            else:
                right -= 1


instance = Solution()
print(instance.two_sum_II([1,2,3,4],7))