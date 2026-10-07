class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                del_l, del_r = s[l+1:r+1], s[l:r]
                return del_l==del_l[::-1] or del_r==del_r[::-1]
            l,r = l+1,r-1
        return True