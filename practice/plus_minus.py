# def plus_minus(my_numlist):
#     positives = 0
#     negatives = 0
#     zero = 0
#     length = len(my_numlist)
#     for i in my_numlist:
#         if i > 0:
#             positives += 1  
#         elif i < 0:
#             negatives+= 1
#         else:
#             zero+= 1
#     print(f"Positives: {positives/length:.6f}")
#     print(f"Negatives: {negatives/length:.6f}")
#     print(f"Zeros: {zero/length:.6f}")
            
def plus_minus(my_numlist):
    zeros = my_numlist.count(0) / len(my_numlist)
    positives =  sum(1 for num in my_numlist if num > 0) / len(my_numlist)
    negatives = 1 - (zeros + positives) 
    print(f"Positives: {positives:6f}")
    print(f"Negatives: {negatives:.6f}")
    print(f"Zeros: {zeros:.6f}")

my_numlist =  list(map(int,input("Enter a list: ").split()))
plus_minus(my_numlist)