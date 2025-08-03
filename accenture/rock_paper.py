def find_winning_move(m):
    if m == "rock":
        return "paper"
    elif m == "scissor":
        return "rock"
    else:
        return "paper"


m = input()
print(find_winning_move(m))