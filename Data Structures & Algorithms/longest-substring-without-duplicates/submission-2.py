class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        last_idx = {}
        max_len = 0
        for high,ch in enumerate(s):
            if ch in last_idx and last_idx[ch]>=low:
                low = last_idx[ch]+1
            last_idx[ch]=high
            max_len = max(max_len,high-low+1)
        return max_len