class Solution:#test

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[i]!='#':
                i+=1
            size = int(s[j:i])
            j=i+1
            i=j+size
            res.append(s[j:i])
            
        return res   