class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
            
        low, start = 0, 0
        res = float('inf')
        
        # Replaced 256-element arrays with dictionaries (hashmaps)
        have = {}
        need = {}
        
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
            
        for high in range(len(s)):
            char = s[high]
            have[char] = have.get(char, 0) + 1
            
            while self.helper(have, need):
                if res > high - low + 1:
                    res = high - low + 1
                    start = low
                    
                left_char = s[low]
                have[left_char] -= 1
                low += 1
                
        return "" if res == float('inf') else s[start:start+res]

    def helper(self, have, need):
        # We now only scan the unique characters that exist in 't', 
        # instead of a hardcoded 256 array
        for char, required_count in need.items():
            if have.get(char, 0) < required_count:
                return False
        return True