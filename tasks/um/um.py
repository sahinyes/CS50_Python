import re

def main():
    print(count(input("Text: ")))

def count(s):
    text = re.findall(r"\b([U-u]m)\b", s)
    return len(text)

if __name__ == "__main__":
    main()