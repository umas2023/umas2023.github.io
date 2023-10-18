
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def has_duplicate_chars(s):
            return len(set(s)) < len(s)
        max_len = 0
        cur_len = 0
        start_index = 0

        for index in range(len(s)):
            cur_len += 1
            while has_duplicate_chars(s[start_index:index]):
                cur_len -= 1
                start_index += 1
            max_len = max(max_len, cur_len)
            
        return max_len
    

print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("abcd"))










