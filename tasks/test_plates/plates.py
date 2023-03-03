def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False

def is_valid(s):
    if len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for i in s:
            if i.isdigit():
                result = s.index(i)
                if s[result:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
        return True
    else:
        return False