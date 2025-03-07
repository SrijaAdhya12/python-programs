class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        return max(my_dict.keys(), key=my_dict.get)
        