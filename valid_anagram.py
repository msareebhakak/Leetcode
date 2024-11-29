# Leetcode 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # assuming the strings are lower
        # Time complexity O(nlogn)
        if len(s) != len(t):
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        else:
            return False

    def isAnagram_hashmap(self, s: str, t: str) -> bool:
        # O(n) complexity
        if len(s) != len(t):
            return False

        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            if s[i] in hash_s.keys():
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
            if t[i] in hash_t.keys():
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1

        return hash_s == hash_t


if __name__ == '__main__':
    valid = Solution()
    print(valid.isAnagram("rat", "car"))
    print(valid.isAnagram_hashmap("rat", "car"))