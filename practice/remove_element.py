# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)


    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j,v in enumerate(nums):
            if v != val:
                nums[i] = nums[j]
                i += 1
        return i