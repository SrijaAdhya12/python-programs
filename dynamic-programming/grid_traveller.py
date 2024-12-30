#Say you are a traveller on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right. In how many ways can you travel to the goal on a grid with dimensions m*n?

def grid_traveller(m,n):
    if m == 1 and n==1:
        return 1
    if m ==0 or n==0:
        return 0
    return grid_traveller(m-1,n) + grid_traveller(m,n-1)

#time complexity of O(2^n+m) and space complexity of O(n+m)

print(grid_traveller(1,1))
print(grid_traveller(2,3))
print(grid_traveller(3,2))
print(grid_traveller(3,3))

#memorization
def grid_travellermemo(m,n, memo={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[key] = grid_travellermemo(m-1,n, memo) + grid_travellermemo(m,n-1, memo)
    return memo[key]

#time complexity of O(n*m) and space complexity of O(n+m)