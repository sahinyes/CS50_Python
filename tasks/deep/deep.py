a = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

b = a.lower().replace("-","").replace(" ","")

if b == "fortytwo" or b == "42":
        print("Yes")
else:
        print("No")