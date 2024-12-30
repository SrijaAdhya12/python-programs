people: list[str] = ['Srija', 'Pritam' , 'Mario', 'Stephanny']

long_names: list[str] = [p for p in  people if len(p) > 5] 
print(f"Long Names: {long_names}")