# Leetcode 409. Longest Palindrome
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = defaultdict(int)

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2

        for cnt in count.values():
            if cnt % 2 != 0:
                res += 1
                break

        return res


if __name__ == '__main__':
    long = Solution()
    print(long.longestPalindrome("abccccdd"))
    print(long.longestPalindrome("a"))
