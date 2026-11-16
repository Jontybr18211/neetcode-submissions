class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        countT,window = {},{}
        for ch in t:
            countT[ch]=countT.get(ch,0)+1
        need,have = len(countT),0
        start,res = 0,float('inf')
        low = 0
        for high in range(len(s)):
            window[s[high]]=window.get(s[high],0)+1
            if s[high] in countT and window[s[high]]==countT[s[high]]:
                have+=1
            while have==need:
                if res>high-low+1:
                    res=high-low+1
                    start=low
                window[s[low]]-=1
                if s[low] in countT and window[s[low]]<countT[s[low]]:
                    have-=1
                low+=1
        return s[start:start+res] if res!=float('inf') else ""