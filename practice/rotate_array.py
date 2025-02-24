# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            last_element = nums.pop()
            nums.insert(0, last_element)
        