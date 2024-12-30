age = 25
smokes = True

health = "poor" if age >60 else ("Good" if age < 30 else "fair")
print(health)