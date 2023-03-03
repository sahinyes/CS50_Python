import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    counter = 3
    score = 0
    for i in range(10):
        if level == 1:
            a = random.randint(0,9)
            b = random.randint(0,9)
        elif level == 2:
            a = random.randint(10,99)
            b = random.randint(10,99)
        elif level == 3:
            a = random.randint(100,999)
            b = random.randint(100,999)
        while True:
            try:
                answer = input(f"{a} + {b} = ")
                if int(answer) == (a+b):
                    score += 1
                    break
                elif answer != (a+b):
                    counter -= 1
                    print("EEE")
                if counter <= 0:
                    print(f"{a} + {b} = {a+b}")
                    break
            except ValueError:
                pass
    else:
        print(f"Score: {score}")

if __name__ == "__main__":
    main()