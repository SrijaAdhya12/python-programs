# CODE: WAF 'cansum(target,numbers)' that returns a boolean indicating whether or not it is possible to generate the target sum using the numbers in the array. You may use an element of the array as many times as needed. You may assume that all input numbers are nonnegative.

# canSum(7,[5,3,4,7]) -> true
# canSum(7,[2,4]) -> false

def canSum(targetSum,numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
      reminder =  targetSum - num
      if canSum(reminder,numbers):
        return True
    return False

print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))

# time complexity: O(n^m)
# space complexity: O(m)

#memoization

def cansum(targetSum, numbers, memo=None):
   if memo is None:
      memo = {}
   if targetSum in memo:
      return memo[targetSum]
   if targetSum == 0:
      return True
   if targetSum < 0:
      return False
   for num in numbers:
      reminder = targetSum - num
      if cansum(reminder, numbers):
         memo[targetSum] = True
         return True
   memo[targetSum] = False
   return False

print(cansum(7,[5,3,4,7]))
print(cansum(7,[2,4]))

# time complexity: O(n*m)
# space complexity: O(m)

#memoization for howsum 

def howsum(targetSum, numbers, memo=None):
   if memo is None:
      memo = {}
   if targetSum in memo:
      return memo[targetSum]
   if targetSum == 0:   
      return []
   if targetSum < 0:
      return None
   for num in numbers:
      reminder = targetSum - num
      result = howsum(reminder, numbers, memo)
      if result is not None:
         memo[targetSum] = [num, *result]
         return memo[targetSum]
   memo[targetSum] = None
   return None
