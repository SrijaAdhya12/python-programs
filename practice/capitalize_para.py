#take a para input. Capitalise the first letter of the each sentence


def capitalize_para(para):
    filtered_para= para.rstrip(".")
    lines = filtered_para.split(".")
    newpara = ""
    for line in lines:
        newpara += f"{line.capitalize()}."
    return newpara
    

my_para = input("Enter a paragraph: ")
print(capitalize_para(my_para))

