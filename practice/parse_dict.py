def parse_dict(string):
    string = string.strip("{").strip("}")
    return {element.split(":")[0]:int(element.split(": ")[1]) for element in string.split(", ")}

text = "{srija: 100, pritam: 0}"
print(parse_dict(text))
