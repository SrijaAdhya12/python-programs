my_dict = {"a":1, "b":2, "c":3, "d": 4}
my_dict["e"] = 5
print(my_dict.pop("e"))
print(my_dict.values())
print(my_dict.items())
print(my_dict.get("f", "Not found"))
print(my_dict.get("d", "Not found"))
print(my_dict.popitem())


print("using items")
for k,v in my_dict.items():
    print(k,v)

print("using values method")
for i in my_dict.values():
    print(i)

print("using keys")
for i in my_dict:
    print(my_dict[i])

print("using getitem dunder method")
for i in my_dict:
    print(my_dict.__getitem__(i))
    

