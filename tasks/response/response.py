from validator_collection import checkers

def main():
    print(is_valid(input("email: ")))


def is_valid(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()