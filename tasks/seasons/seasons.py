from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
        birthday = input("Date: ")
        return diff(birthday)

def diff(birthday):
    try:
        year, month, day = birthday.split("-")
        birthday = date(int(year), int(month), int(day))
    except:
        return sys.exit("Invalid")
    difference =  (date.today() - birthday).days * 24 * 60
    result = p.number_to_words(difference, andword="").capitalize()
    print(result + " minutes")
    return result + " minutes"


if __name__ == "__main__":
    main()