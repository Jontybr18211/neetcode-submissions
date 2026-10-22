class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need,have = {},{}
        l,start,res = 0,0,float('inf')
        for ch in t:
            need[ch]=need.get(ch,0)+1
        for r in range(len(s)):
            have[s[r]]=have.get(s[r],0)+1
            while self.helper(have,need):
                if res>r-l+1:
                    res=r-l+1
                    start=l
                have[s[l]]-=1
                l+=1
        return s[start:start+res] if res!=float('inf') else ""
    def helper(self,have,need):
        for ch,required_index in need.items():
            if have.get(ch,0)<required_index:
                return False
        return True