class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        low=0
        need = [0]*26
        give = [0]*26
        for ch in s1:
            need[ord(ch)-ord('a')]+=1
        for high in range(len(s2)):
            give[ord(s2[high])-ord('a')]+=1
            while high-low+1>len(s1):
               give[ord(s2[low])-ord('a')]-=1
               low+=1
            if give==need:
                return True
        return False