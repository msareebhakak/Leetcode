# Leetcode 977. Squares of a sorted array

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l_p = 0
        r_p = len(nums) - 1
        res = []

        while l_p <= r_p:
            if nums[l_p] * nums[l_p] > nums[r_p] * nums[r_p]:
                res.append(nums[l_p] * nums[l_p])
                l_p += 1
            else:
                res.append(nums[r_p] * nums[r_p])
                r_p -= 1

        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))
    print(sol.sortedSquares([-7, -3, 2, 3, 11]))
