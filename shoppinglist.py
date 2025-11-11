import sys
import argparse

def add(name, quantity, price, category):
	print(f"Add: {name}, quantity {quantity}, price {price}, category {category}")
	pass


def main():
	mainparser = argparse.ArgumentParser()
	subparsers = mainparser.add_subparsers(dest="command", required=True, help="Comenzi disponibile:")
	mainparser_add = subparsers.add_parser("add", help = "Add item")
	mainparser_add.add_argument("name", help = "Item name")
	mainparser_add.add_argument("quantity", type=int, help = "Quantity")
	mainparser_add.add_argument("price", type = float, help = "Price")
	mainparser_add.add_argument("category", help = "Category")	
	if len(sys.argv) == 1:
		mainparser.print_help(sys.stderr)
		sys.exit(1)
		
	args = mainparser.parse_args()
	if args.command == "add":
		add(args.name, args.quantity, args.price, args.category)
	else:
		print(f"{args.command} not yet")

if __name__ == "__main__":
	main()
