class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_list = []
        for i,n in enumerate(nums):
            if n == target:
                target_list.append(i)
        if not target_list:
            return [-1,-1]           
        else:
            return [min(target_list), max(target_list)]
        