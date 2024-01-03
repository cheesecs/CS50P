import requests
import sys

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
else:
    sys.exit("Missing command-line argument")

try:
    resp = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    result = resp.json()
    price = result['bpi']['USD']['rate_float']
    print(f"${price * n:,.4f}")
except requests.RequestException:
    pass