# Leetcode 169. Majority Element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums) // 2]

    def majorityElement_hashmap(self, nums: List[int]) -> int:
        hashmap = {}
        res, count = 0, 0
        for i in nums:
            if i in hashmap.keys():
                hashmap[i] += 1
                if hashmap[i] > count:
                    res = i
                else:
                    res = res
                count = max(count, hashmap[i])
            else:
                hashmap[i] = 1

        return res


if __name__ == '__main__':
    valid = Solution()
    print(valid.majorityElement([3, 2, 3]))
    print(valid.majorityElement([2, 2, 1, 1, 1, 2, 2]))

    print(valid.majorityElement_hashmap([3, 2, 3]))
    print(valid.majorityElement_hashmap([2, 2, 1, 1, 1, 2, 2]))
