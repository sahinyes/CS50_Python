def main():
    i = input("a: ")
    gauge(convert(i))

def convert(fraction):
    while True:
        try:
            x = fraction.split("/")
            c = (int(x[0]) / int(x[1])) *100
            if int(x[0]) <= int(x[1]):
                return c
            else:
                continue
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()