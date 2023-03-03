import inflect

l = []
p = inflect.engine()

while True:
    try:
        a = str(input("Input: "))
        l.append(a)
    except EOFError:
        print()
        break

result = p.join(l)
print("Adieu, adieu, to",result)
