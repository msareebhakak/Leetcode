# Leetcode 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        if len(num) == 1:
            return True
        return num == num[::-1]

    def isPalindrome_twoPointer(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        if len(num) == 1:
            return True
        l = 0
        r = len(num) - 1
        while l < r:
            if not num[l] == num[r]:
                return False
            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    valid = Solution()
    print(valid.isPalindrome(121))
    print(valid.isPalindrome(-121))
    print(valid.isPalindrome(10))
    print(valid.isPalindrome(0))

    print(valid.isPalindrome_twoPointer(121))
    print(valid.isPalindrome_twoPointer(-121))
    print(valid.isPalindrome_twoPointer(10))
    print(valid.isPalindrome_twoPointer(0))
