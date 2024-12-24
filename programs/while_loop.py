i = 1
while i <= 10:  # basic while loop
    print(i, end=" ")
    i += 1

print()
# continue and break
i = 1
while i<=10:
    print(i)
    if i==5:
        i +=2
        continue
    if i==7:
        break
    i += 1

print()

i=1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i) 
    i+=1

print()



while True: #do_while loop
    print("Hello world")
    i+=1
    if i>10:
        break
        

