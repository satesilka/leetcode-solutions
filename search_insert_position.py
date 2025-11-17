from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

if __name__ == "__main__":
    s = Solution()

    tests = [
        ([1, 3, 5, 6], 5), 
        ([1, 3, 5, 6], 2),  
        ([1, 3, 5, 6], 7), 
        ([1, 3, 5, 6], 0), 
        ([1], 1),          
        ([1], 0),         
        ([1], 2),          
    ]

    for nums, target in tests:
        result = s.searchInsert(nums, target)
        print(f"nums={nums}, target={target} → {result}")