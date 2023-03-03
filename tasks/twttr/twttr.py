text = input("Input: ")
l = ["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"]
out = ""

for i in text:
        if not i in l[:]:
                out += i
print(out)