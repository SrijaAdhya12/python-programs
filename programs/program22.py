url = input("Enter an url: ")
print("url" if url.startswith("https://") or url.startswith("http://") else "Not url")
