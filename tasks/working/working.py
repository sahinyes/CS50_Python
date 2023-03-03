import re


def main():
    print(convert(input("Hours: ")))

def convert(s):

    if hours := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$",s):
        if int(hours.group(1)) > 12 or int(hours.group(4)) > 12:
            raise ValueError

        first = create(int(hours.group(1)), hours.group(2), hours.group(3))
        second = create(int(hours.group(4)), hours.group(5), hours.group(6))
        return first + " to " + second

    else:
        raise ValueError

def create(hour,minute,time):
    if time == "PM":
        if hour == 12:
            hour = 12
        else:
            hour += 12
    else:
        if hour == 12:
            hour = 0

    if minute == None:
        minute = ":00"
        result = f"{hour:02}{minute:02}"

    else:
        result = f"{hour:02}:{minute:02}"

    return result

if __name__ == "__main__":
    main()
