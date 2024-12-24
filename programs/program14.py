# sentence=input("enter a sentence")
# words= (sentence.split())
# for word in words:
#     if word[0] == "w" or word[0]== "W":
#         print(word)

# print()

for word in  input("enter a sentence").split(): print(word) if word[0] in ["w" , "W"]  else None
for word in  input("enter a sentence").split(): print(word) if word[0].lower() == "w"  else None
