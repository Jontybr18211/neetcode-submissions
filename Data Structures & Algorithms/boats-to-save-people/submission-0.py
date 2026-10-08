class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0,len(people)-1
        res=0
        while left<=right:
            diff = limit - people[right]
            right-=1
            res+=1
            if left<=right and diff>=people[left]:
                left+=1
        return res