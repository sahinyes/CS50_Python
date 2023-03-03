text = input("camelCase: ")
text = "".join(["_" + a.lower() if a.isupper() else a for a in text]).strip("_")
print(f"snake_case: {text}")