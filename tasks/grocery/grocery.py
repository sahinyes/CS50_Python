l = []
c = {}


while True:
    try:
        a = input().upper()
        l.append(a)
    except EOFError:
        print("")
        for i in l:
            if not i in c:
                c[i] = 1
            else:
                c[i] += 1

        for key, value in sorted(c.items()):
            print(value,key)
        exit()