import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--principal", type=int)
args, unknown = parser.parse_known_args()
if len(sys.argv) == 5 and args.type in ["annuity", "diff"] and "interest" in sys.argv[4]:
    i = args.interest / (12 * 100)
    if args.type == "annuity":
        if "payment" in sys.argv[2] and "periods" in sys.argv[3]:
            print(f"Your loan principal = {math.floor((args.payment - args.payment / math.pow(1 + i, args.periods)) / i)}!\nOverpayment = {args.payment * args.periods - math.floor((args.payment - args.payment / math.pow(1 + i, args.periods)) / i)}")
        elif "principal" in sys.argv[2] and "payment" in sys.argv[3]:
            n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
            print(f"It will take {math.floor(n / 12)} years" + (f" and {n - 12 * math.floor(n / 12)} months" if n - 12 * math.floor(n / 12) != 0 else "") + f" to repay this loan!\nOverpayment = {n * args.payment - args.principal}")
        elif "principal" in sys.argv[2] and "periods" in sys.argv[3]:
            print(f"Your annuity payment = {math.ceil((i * args.principal * math.pow(i + 1, args.periods)) / (math.pow(i + 1, args.periods) - 1))}!\nOverpayment = {math.ceil((i * args.principal * math.pow(i + 1, args.periods)) / (math.pow(i + 1, args.periods) - 1)) * args.periods - args.principal}")
        else:
            print("Incorrect parameters.")
    if args.type == "diff":
        if "principal" in sys.argv[2] and "periods" in sys.argv[3]:
            for m in range(1, args.periods + 1):
                print(f"Month {m}: payment is {math.ceil(args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods))}")
            print(f"\nOverpayment = {sum(math.ceil(args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods)) for m in range(1, args.periods + 1)) - args.principal}")
        else:
            print("Incorrect parameters.")
else:
    print("Incorrect parameters.")