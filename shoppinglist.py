import sys
import argparse
import json
import os
slfile = "shoppinglist.json"

def load():
	if os.path.exists(slfile):
		with open (slfile, "r") as f:
			return json.load(f)
	return []
def save(shoppinglist):
	with open (slfile, "w") as f:
		json.dump(shoppinglist, f, indent=4)

def add(name, quantity, price, category):
	if quantity <= 0:
		print("Quantity must be positive")
		return
	if price < 0:
		print("Price cannot be negative")
		return
	shoppinglist = load()
	item = {
		"name": name,
		"quantity": quantity,
		"price": price,
		"category": category
	}
	shoppinglist.append(item)
	save(shoppinglist)
	itemtotal = quantity * price
	print(f"Added {quantity} x {name}, unit price ${price} to category '{category}'. Total: ${itemtotal}")




def main():
	mainparser = argparse.ArgumentParser()
	subparsers = mainparser.add_subparsers(dest="command", required=True, help="Available commands:")
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
