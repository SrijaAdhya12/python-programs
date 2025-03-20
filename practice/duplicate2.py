class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i,n in enumerate(nums):
            if n in my_dict and i - my_dict[n] <= k:
                return True
            my_dict[n] = i
        return False

        