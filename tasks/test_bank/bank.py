def main():
    a = input("Greeting: ")
    print(value(a))

def value(a):
    b = a.lower().strip()

    if not b.find("hello"):
        return 0

    elif b[0] == "h":
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
