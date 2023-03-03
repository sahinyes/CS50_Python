def main():
    text = input("Input: ")
    shorten(text)

def shorten(word):
    #text = input("Input: ")
    l = ["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"]
    out = ""

    for i in word:
            if not i in l[:]:
                    out += i
    return out

if __name__ == "__main__":
    main()