class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,k = 0,0,0
        res=[0]*(len(word1)+len(word2))
        while i<len(word1) and j<len(word2):
            res[k]=word1[i]
            res[k+1]=word2[j]
            i,j,k = i+1,j+1,k+2
        while i<len(word1):
            res[k]=word1[i]
            i,k=i+1,k+1
        while j<len(word2):
            res[k]=word2[j]
            j,k=j+1,k+1
        return ''.join(res)