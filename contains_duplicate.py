# Leetcode 217. Contains duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    def containsDuplicate_hashmap(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                return True
            else:
                hashmap[i] = 1
        return False


if __name__ == '__main__':
    valid = Solution()
    print(valid.containsDuplicate([1, 2, 3, 1]))
    print(valid.containsDuplicate([1, 2, 3, 4]))
    print(valid.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    print(valid.containsDuplicate_hashmap([1, 2, 3, 1]))
    print(valid.containsDuplicate_hashmap([1, 2, 3, 4]))
    print(valid.containsDuplicate_hashmap([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
