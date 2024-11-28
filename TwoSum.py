# Leetcode 1. Two Sum
from typing import List


class Solution:
    def two_sum_brute(self, ar, target):
        # brute force O(n^2)
        for index_1, i in enumerate(ar):
            for index_2, j in enumerate(ar[i:]):
                if i + j == target:
                    return index_1, index_2 + i
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap.keys():
                return [hashmap[target - num], index]
            else:
                hashmap[num] = index


if __name__ == '__main__':
    nums = [2, 1, 5, 3]
    sol = Solution()
    print(sol.two_sum_brute(nums, 4))
    print(sol.twoSum(nums, 4))
