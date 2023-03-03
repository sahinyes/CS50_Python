import sys
import requests
import json

def main():
    g = get_coin()
    req_coin(g)

def get_coin():
    #print(sys.argv)
    if len(sys.argv) == 2:
        try:
            if float(sys.argv[1]):
                return sys.argv[1]
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

def req_coin(gcoin):
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = req.json()
    usd = data["bpi"]["USD"]["rate_float"]
    result = float(usd) * float(gcoin)
    print(gcoin)
    print(f"${result:,.4f}")

main()