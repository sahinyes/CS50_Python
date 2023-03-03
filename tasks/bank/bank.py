a = input("Greeting:")

b = a.lower().replace(" ","")

if not b.find("hello"):
        print("$0")

elif b[0] == "h":
        print("$20")

else:
        print("$100")