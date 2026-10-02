class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count=defaultdict(int)
        prefix_sum_count[0]=1 # base case (empty prefix) for returning whole subarray if they reach k
        cur_sum=res=0
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += prefix_sum_count.get(diff,0) # returns 0 rather than boolean
            prefix_sum_count[cur_sum] += 1
        return res