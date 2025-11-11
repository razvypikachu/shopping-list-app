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
	print(f"Added {quantity} x {name}, unit price ${price} to category '{category}', total ${itemtotal}")

def listitems(sortby=None):
	shoppinglist = load()
	if sortby:
		print(f"(will sort, not yet implemented)")
	for item in shoppinglist:
		total = item["quantity"] * item["price"]
		print(f'{item["name"]} ({item["category"]}) - {item["quantity"]} x {item["price"]} = {total}')

def remove(name):
	shoppinglist = load()
	newlist = [item for item in shoppinglist if item["name"] != name]
	if(len(newlist) == len(shoppinglist)):
		print(f"Item '{name}' not found")
	else:
		save(newlist)
		print(f"Removed '{name}'")

def search(category):
	shoppinglist = load()
	for item in shoppinglist:
		if item["category"] == category:
			total = item["quantity"] * item["price"]
			print(f'{item["name"]} ({item["category"]}) - {item["quantity"]} x {item["price"]} = {total}')

def total():
	shoppinglist = load()
	totalcost = 0
	categorytotals = {}
	for item in shoppinglist:
		itemtotal = item["quantity"] * item["price"]
		totalcost += itemtotal
		if item["category"] in categorytotals:
			categorytotals[item["category"]] += itemtotal
		else:
			categorytotals[item["category"]] = itemtotal
	print(f"Total cost of shopping list:{totalcost}")
	for category, cat_total in categorytotals.items():
		print(f"Category '{category}':{cat_total}")

def main():
	mainparser = argparse.ArgumentParser()
	subparsers = mainparser.add_subparsers(dest="command", required=True, help="Available commands:")
	mainparser_add = subparsers.add_parser("add", help = "Add item")
	mainparser_add.add_argument("name", help = "Item name")
	mainparser_add.add_argument("quantity", type=int, help = "Quantity")
	mainparser_add.add_argument("price", type = float, help = "Price")
	mainparser_add.add_argument("category", help = "Category")	
	mainparser_remove = subparsers.add_parser("remove", help = "Remove item")
	mainparser_remove.add_argument("name", help = "Item name")
	mainparser_list = subparsers.add_parser("list", help = "List items")
	mainparser_list.add_argument("--sortby", choices=["name", "category", "price"], help="Sort by field")
	mainparser_search = subparsers.add_parser("search", help = "Search by category")
	mainparser_search.add_argument("category", help = "Category")
	mainparser_total = subparsers.add_parser("total", help = "Total cost")
	if len(sys.argv) == 1:
		mainparser.print_help(sys.stderr)
		sys.exit(1)
		
	args = mainparser.parse_args()
	if args.command == "add":
		add(args.name, args.quantity, args.price, args.category)
	elif args.command == "list":
		listitems(args.sortby)
	elif args.command == "remove":
		remove(args.name)
	elif args.command == "search":
		search(args.category)
	elif args.command == "total":
		total()
	else:
		print(f"{args.command} not yet")

if __name__ == "__main__":
	main()
