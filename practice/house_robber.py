class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rob1, rob2 = 0,0
        for n in nums:
            max_rob = max(rob1, rob2+n)
            rob2 = rob1
            rob1 = max_rob
        return rob1


                    
        