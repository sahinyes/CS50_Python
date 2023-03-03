def main():
        time = input("What time is it? ")
        meal = convert(time)
        if meal >= 7 and meal <=8:
                print("breakfast time")
        elif meal >= 12 and meal <=13:
                print("lunch time")
        elif meal >= 18 and meal <= 19:
                print("dinner time")

def convert(time):
        hour, min = time.split(":")
        hour = float(hour) + (float(min) / 60)
        return hour

if __name__ == "__main__":
    main()