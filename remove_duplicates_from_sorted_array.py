from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            if not nums:
                return 0

            i = 0  
            n = len(nums)

            for j in range(1, n):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]

            nums[i+1:] = "_" * (n - i - 1)
            return i + 1

if __name__ == "__main__":
    nums1 = [1, 1, 2]
    k1 = Solution().removeDuplicates(nums1)
    print(f"Output: {k1}, nums = {nums1}")

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = Solution().removeDuplicates(nums2)
    print(f"Output: {k2}, nums = {nums2}")
        