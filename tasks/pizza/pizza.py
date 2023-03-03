import sys
import tabulate
import csv

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].rsplit(".")[1] != "csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
except:
    raise FileNotFoundError

