class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = {}
        frequency = len(nums)/3
        new_list = []
        for n in nums:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1
        for k,v in my_dict.items():
            if v > frequency:
                new_list.append(k)
        return new_list        