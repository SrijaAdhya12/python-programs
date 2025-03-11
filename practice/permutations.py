def get_permutations(string, i=0):
    for j in range (i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        get_permutations(words, i+1)
    if i == len(string):
        print("".join(string))
        
str = input("Enter a string: ")
print(get_permutations(str))
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        permutations = []
        for i, element in enumerate(nums):
            remaining_list = nums[:i] + nums[i+1:]
            for perm in self.permute(remaining_list):
                permutations.append([element] + perm)
        return permutations

        