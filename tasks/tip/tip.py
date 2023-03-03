def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
        #TODO
        return float(dollars.strip("$"))

def percent_to_float(percent):
        # TODO
        return float(percent.strip("%")) / 100

main()