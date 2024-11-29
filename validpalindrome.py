# Leetcode 125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pythonic way which creates a new string,
        # uses .isalnum (alphanumeric number) and .lower()
        # and [::-1] to reverse
        filter_str = ""
        for char in s:
            if char.isalnum():
                filter_str += char.lower()

        return filter_str == filter_str[::-1]

    def isPalindrome_twopointer(self, s: str) -> bool:
        # checks with left and right side extreme pointers
        # without creating extra string - O(1) memory
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isAlNum(s[left]):
                left += 1
            while right > left and not self.isAlNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isAlNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


if __name__ == '__main__':
    valid = Solution()
    print(valid.isPalindrome("A man, a plan, a canal: Panama"))
    print(valid.isPalindrome_twopointer("A man, a plan, a canal: Panama"))