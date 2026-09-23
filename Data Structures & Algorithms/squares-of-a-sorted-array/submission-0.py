class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos,neg=[],[]
        for n in nums:
            if n<0:
                neg.append(n)
            else:
                pos.append(n)

        res=[]
        if len(pos)==0:
            res = [n*n for n in neg]
            res.reverse()
            return res    
        if len(neg)==0:
            return [x*x for x in pos]


        pos = [x*x for x in pos]
        neg = [n*n for n in neg][::-1]
        i=j=0

        while i<len(pos) and j<len(neg):
            if pos[i]<neg[j]:
                res.append(pos[i])
                i+=1
            else:
                res.append(neg[j])
                j+=1
        
        while i<len(pos):
            res.append(pos[i])
            i+=1
        while j<len(neg):
            res.append(neg[j])
            j+=1
        return res