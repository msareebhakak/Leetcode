# Leetcode 169. Majority Element

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_p = 0
        for r_p in range(len(nums)):
            if nums[r_p] > 0:
                k = nums[l_p]
                nums[l_p] = nums[r_p]
                nums[r_p] = k
                l_p += 1

        print(nums)


if __name__ == '__main__':
    valid = Solution()
    print(valid.moveZeroes([0, 1, 0, 3, 12]))
    print(valid.moveZeroes([0]))
