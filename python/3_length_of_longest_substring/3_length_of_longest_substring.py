# -*- coding=utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        compare = set({})
        slide_size = 0
        max_size = 0
        left_pos = 0
        for i in range(len(s)):
            while s[i] in compare:
                compare.remove(s[left_pos])
                left_pos += 1
                slide_size -= 1
            slide_size += 1
            if slide_size > max_size:
                max_size = slide_size
            compare.add(s[i])
        return max_size

sol = Solution()
string = "pwwkewcf"
print(sol.lengthOfLongestSubstring(string))