# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            last_element = nums.pop()
            nums.insert(0, last_element)
            
    def rotate(self, nums: List[int], k: int) -> None:
        mod = k % len(nums)
        sliced_list = nums[:-mod]
        remaining_list = nums[-mod:]
        nums.clear()
        new_list = remaining_list + sliced_list
        nums.extend(new_list)   

    