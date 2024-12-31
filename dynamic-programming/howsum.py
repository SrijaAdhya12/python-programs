# CODE: WAF 'howsum(target,numbers)' that returns an array containing any combination of elements that add up to exactly the target sum. If there is no combination that adds up to the target sum, then return null. If there are multiple combinations possible, you may return any single one.

def howsum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        reminder = targetSum - num
        result = howsum(reminder, numbers)
        if result is not None:
            return [num, *result]
    return None

print(howsum(7,[5,3,4,7]))

# time complexity: O(n^m)
# space complexity: O(m)


