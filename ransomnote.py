# Leetcode 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # both strings are lower case
        # solution is O(N)
        base_dict = {}
        for char in magazine:
            if char in base_dict.keys():
                base_dict[char] += 1
            else:
                base_dict[char] = 1
        # print(base_dict)

        for char in ransomNote:
            if char in base_dict.keys():
                if base_dict[char] == 1:
                    base_dict.pop(char)
                else:
                    base_dict[char] -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    valid = Solution()
    print(valid.canConstruct("rat", "car"))
    print(valid.canConstruct("a", "b"))
    print(valid.canConstruct("aa", "ab"))
    print(valid.canConstruct("aa", "aab"))
