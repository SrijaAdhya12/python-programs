def find_plots(plot_list):
    count = 0
    for i in plot_list:
        sqrt = i**0.5
        if sqrt*sqrt == i:
            count+=1
    return count


plot_list = list(map(int, input().split()))
print(find_plots(plot_list))