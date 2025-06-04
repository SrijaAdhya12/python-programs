def revaluation(x,y,n,arr):
    arr[x-1] = y
    ans = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            ans += 1
    return "Number of students in merit list are: ",ans



n = int(input("Enter number of Students: "))
reval = int(input("Enter number of revaluations: "))

my_list = []

for _ in range(n):
    my_list.append(int(input(f"Enter marks of student {_+1}: ")))

for i in range(reval):
    x = int(input("Enter position to be updated: "))
    y = int(input("Enter revaluated marks: "))
    print(revaluation(x,y,n,my_list))

